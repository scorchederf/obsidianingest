# Obsidian Cyber Vault Ingest Pipeline

Drop a file in the inbox, it gets read, understood by a local Ollama model,
filed into your vault with proper frontmatter, and linked to existing
notes (creating stub notes for anything new it references).

## Setup

```bash
pip install -r requirements.txt
ollama pull qwen2.5:7b-instruct
ollama pull nomic-embed-text
```

Edit `config.yaml`:
- `vault_path` — your actual Obsidian vault root
- `inbox_path` — folder you'll drop raw files into
- `processed_path` — where originals go after successful ingest

## Day-to-day use

```bash
# Process everything currently sitting in the inbox, then exit
python ingest.py

# Or leave it running, polling every 30s
python ingest.py --watch
```

Drop a PDF, docx, html, txt, or md file into the inbox. Within one poll
cycle it'll show up in your vault, correctly foldered, tagged, and linked.

Check `ingest_log.jsonl` afterward — every processed file logs its source,
where it landed, and any stub notes it created along the way. Worth a
skim periodically so you can flesh out stubs and catch misfiled notes.

## Weekly (or whenever): fuzzy linking pass

```bash
python link_similarity.py
```

This finds conceptually related notes that don't share an explicit named
entity (so the per-file pass wouldn't catch them) and prints suggestions.
It does **not** auto-insert these — fuzzy matches are more error-prone
than the exact-match linking that happens automatically during ingest, so
review before adding.

## How linking works

1. **Exact-match (automatic, on every file)** — the model extracts named
   entities (tools, techniques, tactics, services, OS items) from the new
   material. Each is looked up against your existing vault by title. A
   match becomes a `[[wikilink]]`. No match creates a `status: stub` note
   in the right folder so the graph doesn't dead-end, and links to that
   instead.
2. **Fuzzy/semantic (manual review, run periodically)** — `link_similarity.py`
   embeds every note's body and surfaces high-similarity pairs that don't
   share an entity. You decide whether to add the link.

## Files

| File | Purpose |
|---|---|
| `config.yaml` | Paths, model names, category/folder mapping |
| `extract.py` | Pulls plain text out of pdf/docx/html/txt/md |
| `ollama_client.py` | Thin wrapper for `/api/chat` (JSON mode) and `/api/embeddings` |
| `prompts.py` | The classification/extraction system prompt + schema |
| `vault_index.py` | Scans the vault, builds title lookups for exact-match linking |
| `render.py` | Fills the note template, resolves entities into links/stubs |
| `ingest.py` | Main loop — ties it all together |
| `link_similarity.py` | Secondary embedding-based fuzzy-link suggestions |
| `note-template.md` | Reference template (ingest.py renders inline via `render.py`, this is for manual notes) |

## Things worth tuning as you use it

- **Model swap**: `qwen2.5:7b-instruct` is the default given your 8GB VRAM.
  If classification quality frustrates you on complex material, try
  `llama3.1:8b-instruct-q4_0` — swap in `config.yaml`, no code changes needed.
- **Overwrite behavior**: if a note with the same slug already exists,
  `ingest.py` writes a timestamped duplicate rather than overwriting —
  check `ingest_log.jsonl` for these and merge manually.
- **Failed files stay in the inbox** (not moved to `_processed`) so you
  can fix the issue and it'll retry next run.
