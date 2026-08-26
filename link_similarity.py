#!/usr/bin/env python3
"""
link_similarity.py
Secondary linking pass, meant to run periodically (e.g. weekly cron), not
per-file. Finds conceptually related notes that don't share an explicit
entity — e.g. a study note and an engagement writeup that both involve
Kerberoasting but never say so in a way exact-match linking would catch.

This does NOT auto-insert links (fuzzy matches are more error-prone than
the exact-match pass in ingest.py) — it prints suggestions to review and
add by hand, or pipe into your own review step.

Usage:
    python link_similarity.py --rebuild   # re-embed every note (slow, run after big changes)
    python link_similarity.py             # embed only new/changed notes, then print suggestions
"""

import argparse
import json
from pathlib import Path

import numpy as np
import yaml

from ollama_client import call_ollama_embed
from vault_index import parse_frontmatter

CONFIG_PATH = Path(__file__).parent / "config.yaml"


def load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text())


def load_embedding_db(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {}


def save_embedding_db(path: Path, db: dict):
    path.write_text(json.dumps(db))


def note_body_for_embedding(text: str) -> str:
    # Strip frontmatter, keep body text — embeddings work better on
    # prose content than on YAML.
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].strip()
    return text.strip()


def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild", action="store_true", help="re-embed every note, not just new ones")
    args = parser.parse_args()

    cfg = load_config()
    if not cfg.get("embedding_enabled", False):
        print("Embedding pass disabled in config.yaml (embedding_enabled: false).")
        return

    vault_path = Path(cfg["vault_path"])
    db_path = Path(cfg["embedding_db_path"])
    db = {} if args.rebuild else load_embedding_db(db_path)

    md_files = list(vault_path.rglob("*.md"))
    print(f"Scanning {len(md_files)} notes...")

    for md_file in md_files:
        rel_path = str(md_file.relative_to(vault_path))
        text = md_file.read_text(errors="ignore")
        mtime = md_file.stat().st_mtime

        if rel_path in db and db[rel_path].get("mtime") == mtime:
            continue  # unchanged since last run

        body = note_body_for_embedding(text)
        if len(body) < 50:
            continue  # too thin to embed meaningfully (e.g. fresh stubs)

        vector = call_ollama_embed(cfg["ollama_host"], cfg["model_embed"], body)
        fm = parse_frontmatter(text)
        db[rel_path] = {
            "mtime": mtime,
            "title": fm.get("title", md_file.stem),
            "vector": vector,
        }
        print(f"  embedded: {rel_path}")

    save_embedding_db(db_path, db)

    # --- Suggest links ---
    threshold = cfg.get("similarity_threshold", 0.78)
    top_k = cfg.get("similarity_top_k", 5)

    paths = list(db.keys())
    vectors = {p: np.array(db[p]["vector"]) for p in paths}

    print("\n--- Suggested links (review and add manually) ---")
    for i, path_a in enumerate(paths):
        sims = []
        for path_b in paths:
            if path_a == path_b:
                continue
            sims.append((path_b, cosine_sim(vectors[path_a], vectors[path_b])))
        sims.sort(key=lambda x: x[1], reverse=True)

        matches = [(p, s) for p, s in sims[:top_k] if s >= threshold]
        if matches:
            print(f"\n{path_a} ({db[path_a]['title']}):")
            for p, s in matches:
                print(f"    -> {p} ({db[p]['title']})  similarity={s:.2f}")


if __name__ == "__main__":
    main()
