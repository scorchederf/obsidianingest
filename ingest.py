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
import time
import traceback
from datetime import datetime
from pathlib import Path
import subprocess

import yaml

from extract import extract_text
from ollama_client import call_ollama_json
from prompts import SYSTEM_PROMPT, build_user_prompt
from render import render_note, resolve_entities, slugify
from vault_index import VaultIndex

CONFIG_PATH = Path(__file__).parent / "config.yaml"


def load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text())


def log_event(log_path: Path, event: dict):
    event["timestamp"] = datetime.now().isoformat()
    with open(log_path, "a") as f:
        f.write(json.dumps(event) + "\n")


def process_file(filepath: Path, cfg: dict, index: VaultIndex):
    vault_path = Path(cfg["vault_path"])
    processed_path = Path(cfg["processed_path"])
    log_path = Path(cfg["log_path"])
    category_folders = cfg["categories"]

    print(f"[+] Processing {filepath.name}")

    text = extract_text(filepath)
    if not text.strip():
        raise ValueError("Extracted text is empty — nothing to file.")

    user_prompt = build_user_prompt(text, index.tree_summary())
    data = call_ollama_json(
        host=cfg["ollama_host"],
        model=cfg["model_summarize"],
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt,
    )
    data["source"] = filepath.name

    relations, created_stubs = resolve_entities(data, index, category_folders)

    template_path = Path(cfg["template_path"])
    note_md = render_note(data, relations, template_path)

    category = data.get("category", "study_notes")
    folder = category_folders.get(category, "study-notes")
    slug = slugify(data["title"])
    rel_path = f"{folder}/{slug}.md"
    out_path = vault_path / rel_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if out_path.exists():
        # Don't silently overwrite — append a suffix and flag it for review.
        out_path = out_path.with_stem(out_path.stem + f"-{int(time.time())}")

    out_path.write_text(note_md)
    index.register(category, data["title"], str(out_path.relative_to(vault_path)))

    processed_path.mkdir(parents=True, exist_ok=True)
    shutil.move(str(filepath), str(processed_path / filepath.name))

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
            subprocess.run(f"cd /home/scorchederf/dev/obsidianingest && git add --all && git commit -m 'auto-updated {filepath}' && git push", shell=True)

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
