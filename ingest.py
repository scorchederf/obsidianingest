#!/usr/bin/env python3
"""
ingest.py
Watches an inbox folder, and for every new file: extracts text, sends it
to a local Ollama model for classification + extraction, resolves entity
links against the existing vault (creating stubs as needed), writes the
resulting note into the vault, and archives the source file.

Usage:
    python ingest.py                # process everything currently in inbox, then exit
    python ingest.py --watch        # keep running, poll inbox every N seconds
"""

import argparse
import json
import shutil
import subprocess
import time
import traceback
from datetime import datetime
from pathlib import Path

import yaml

from chunking import split_into_chunks, outline as build_outline
from extract import extract_text
from ollama_client import call_ollama_json
from prompts import (
    SYSTEM_PROMPT,
    SYSTEM_PROMPT_METADATA,
    SYSTEM_PROMPT_SECTIONS,
    build_user_prompt,
    build_metadata_prompt,
    build_chunk_prompt,
)
from render import render_note, resolve_entities, slugify, merge_sections
from vault_index import VaultIndex, parse_frontmatter

CONFIG_PATH = Path(__file__).parent / "config.yaml"


def load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text())


def log_event(log_path: Path, event: dict):
    event["timestamp"] = datetime.now().isoformat()
    with open(log_path, "a") as f:
        f.write(json.dumps(event) + "\n")


def extract_document(text: str, filename: str, cfg: dict, vault_tree: str) -> dict:
    """
    Small files: one combined call (metadata + entities + sections).
    Large files: split on headings, get metadata once from a cheap
    outline pass, then extract entities+sections per chunk and merge.
    """
    chunk_max_chars = cfg.get("chunk_max_chars", 6000)
    chunks = split_into_chunks(text, max_chars=chunk_max_chars)

    if len(chunks) == 1:
        return call_ollama_json(
            host=cfg["ollama_host"],
            model=cfg["model_summarize"],
            system_prompt=SYSTEM_PROMPT,
            user_prompt=build_user_prompt(chunks[0], vault_tree),
        )

    print(f"    -> large file, splitting into {len(chunks)} chunks")

    outline_text = build_outline(text)
    metadata = call_ollama_json(
        host=cfg["ollama_host"],
        model=cfg["model_summarize"],
        system_prompt=SYSTEM_PROMPT_METADATA,
        user_prompt=build_metadata_prompt(outline_text, filename),
    )

    merged_entities: dict[str, list[str]] = {}
    merged_sections: list[dict] = []
    merged_references: list[str] = []

    for i, chunk in enumerate(chunks):
        print(f"    -> extracting chunk {i + 1}/{len(chunks)}")
        chunk_data = call_ollama_json(
            host=cfg["ollama_host"],
            model=cfg["model_summarize"],
            system_prompt=SYSTEM_PROMPT_SECTIONS,
            user_prompt=build_chunk_prompt(chunk, vault_tree, i + 1, len(chunks)),
        )

        for key, values in chunk_data.get("entities", {}).items():
            bucket = merged_entities.setdefault(key, [])
            for v in values:
                if v not in bucket:
                    bucket.append(v)

        merged_sections.extend(chunk_data.get("sections", []))

        for ref in chunk_data.get("references", []):
            if ref not in merged_references:
                merged_references.append(ref)

    metadata["entities"] = merged_entities
    metadata["sections"] = merge_sections(merged_sections)
    metadata["references"] = merged_references
    return metadata


def process_file(filepath: Path, cfg: dict, index: VaultIndex):
    vault_path = Path(cfg["vault_path"])
    processed_path = Path(cfg["processed_path"])
    log_path = Path(cfg["log_path"])
    category_folders = cfg["categories"]

    print(f"[+] Processing {filepath.name}")

    text = extract_text(filepath)
    if not text.strip():
        raise ValueError("Extracted text is empty — nothing to file.")

    data = extract_document(text, filepath.name, cfg, index.tree_summary())
    data["source"] = filepath.name

    relations, created_stubs = resolve_entities(data, index, category_folders)

    template_path = Path(cfg["template_path"])
    category = data.get("category", "study_notes")
    folder = category_folders.get(category, "study-notes")

    # Reuse an existing note's path if this title already exists in the
    # vault (as a real note OR a stub) instead of always deriving a fresh
    # slug — this is what lets a stub get upgraded in place rather than
    # ending up with a duplicate empty stub sitting next to a new file.
    existing_rel_path = index.find(category, data["title"]) or index.find_anywhere(data["title"])
    if existing_rel_path:
        out_path = vault_path / existing_rel_path
    else:
        slug = slugify(data["title"])
        out_path = vault_path / f"{folder}/{slug}.md"

    out_path.parent.mkdir(parents=True, exist_ok=True)

    date_created_override = None
    if out_path.exists():
        existing_fm = parse_frontmatter(out_path.read_text(errors="ignore"))
        if existing_fm.get("status") == "stub":
            print(f"    -> upgrading existing stub note: {out_path.relative_to(vault_path)}")
            date_created_override = existing_fm.get("date_created")
        else:
            # Real content already lives here — don't clobber it.
            out_path = out_path.with_stem(out_path.stem + f"-{int(time.time())}")

    note_md = render_note(data, relations, template_path, date_created_override=date_created_override)
    out_path.write_text(note_md)
    index.register(category, data["title"], str(out_path.relative_to(vault_path)))

    processed_path.mkdir(parents=True, exist_ok=True)

    # disable move whilst working on it.
    # shutil.move(str(filepath), str(processed_path / filepath.name))

    log_event(log_path, {
        "source_file": filepath.name,
        "note_path": str(out_path.relative_to(vault_path)),
        "category": category,
        "title": data["title"],
        "stubs_created": created_stubs,
        "status": "ok",
    })

    print(f"    -> {out_path.relative_to(vault_path)}")
    if created_stubs:
        print(f"    -> created {len(created_stubs)} stub note(s): {created_stubs}")


def run_once(cfg: dict):
    inbox = Path(cfg["inbox_path"])
    vault_path = Path(cfg["vault_path"])
    index = VaultIndex(vault_path)

    files = [f for f in inbox.rglob("*") if f.is_file()]
    if not files:
        print("Inbox is empty.")
        return

    for filepath in files:
        try:
            process_file(filepath, cfg, index)
            subprocess.run(
                f"cd /home/scorchederf/dev/obsidianingest && git add --all && git commit -m 'auto-updated {filepath}' && git push",
                shell=True,
            )

        except Exception as e:
            print(f"[!] Failed on {filepath.name}: {e}")
            traceback.print_exc()
            log_event(Path(cfg["log_path"]), {
                "source_file": filepath.name,
                "status": "error",
                "error": str(e),
            })
            # Leave the file in place so it's retried / can be inspected.


def watch(cfg: dict, interval_seconds: int = 30):
    print(f"Watching {cfg['inbox_path']} every {interval_seconds}s. Ctrl+C to stop.")
    while True:
        run_once(cfg)
        time.sleep(interval_seconds)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", action="store_true", help="keep running and poll the inbox")
    parser.add_argument("--interval", type=int, default=30, help="poll interval in seconds (with --watch)")
    args = parser.parse_args()

    config = load_config()

    if args.watch:
        watch(config, args.interval)
    else:
        run_once(config)
