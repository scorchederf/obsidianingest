"""
render.py
Turns the LLM's JSON output into an actual markdown file with frontmatter,
resolving entity mentions into real wikilinks (creating stub notes for
anything new) rather than leaving them as bare text.
"""

import re
from datetime import date
from pathlib import Path

import yaml

from vault_index import VaultIndex

STUB_TEMPLATE = """---
title: "{title}"
aliases: []
tags: {tags}
category: "{category}"
status: stub
date_created: "{today}"
date_modified: "{today}"
source: "auto-generated stub (referenced by another note, not yet written)"
related_tools: []
related_techniques: []
related_tactics: []
related_services: []
related_os: []
related_notes: []
mitre_tactic: ""
mitre_technique: ""
real_path: ""
port: ""
protocol: ""
os: ""
---

# {title}

## Overview
*Stub note — auto-created because another note referenced "{title}". Fill in details when you have them.*
"""


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower())
    return slug.strip("-")


# Which category each entity-type in the LLM's "entities" block belongs to,
# and which namespace prefix / frontmatter field it maps to.
ENTITY_MAP = {
    "tools": ("tools", "tool/", "related_tools"),
    "techniques": ("techniques", "technique/", "related_techniques"),
    "tactics": ("tactics", "attack/", "related_tactics"),
    "services": ("services", "service/", "related_services"),
    "os_items": ("os", "os/", "related_os"),
}


def resolve_entities(data: dict, index: VaultIndex, category_folders: dict[str, str]) -> dict:
    """
    For every entity the LLM extracted, try an exact match against the
    existing vault. If found, record the wikilink. If not found, create
    a stub note so the graph doesn't dead-end, then link to that.

    Returns a dict of {relation_field: [wikilink strings]} plus a list
    of (path, was_new) for logging.
    """
    relations: dict[str, list[str]] = {}
    created_stubs: list[str] = []

    entities = data.get("entities", {})

    for entity_key, names in entities.items():
        if entity_key not in ENTITY_MAP or not names:
            continue
        category, tag_prefix, relation_field = ENTITY_MAP[entity_key]
        folder = category_folders.get(category, category)
        relations.setdefault(relation_field, [])

        for name in names:
            existing_path = index.find(category, name) or index.find_anywhere(name)

            if existing_path:
                note_title = Path(existing_path).stem
                relations[relation_field].append(f"[[{note_title}]]")
                continue

            # Not found -> create a stub note
            slug = slugify(name)
            rel_path = f"{folder}/{slug}.md"
            stub_content = STUB_TEMPLATE.format(
                title=name,
                tags=[f"{tag_prefix}{slug}"],
                category=category,
                today=date.today().isoformat(),
            )
            full_path = index.vault_path / rel_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(stub_content)

            index.register(category, name, rel_path)
            created_stubs.append(rel_path)
            relations[relation_field].append(f"[[{name}]]")

    return relations, created_stubs


def render_note(data: dict, relations: dict, template_path: Path) -> str:
    today = date.today().isoformat()

    frontmatter = {
        "title": data["title"],
        "aliases": [],
        "tags": data.get("tags", []),
        "category": data["category"],
        "status": data.get("status", "draft"),
        "date_created": today,
        "date_modified": today,
        "source": data.get("source", ""),
        "related_tools": relations.get("related_tools", []),
        "related_techniques": relations.get("related_techniques", []),
        "related_tactics": relations.get("related_tactics", []),
        "related_services": relations.get("related_services", []),
        "related_os": relations.get("related_os", []),
        "related_notes": relations.get("related_notes", []),
        "mitre_tactic": data.get("mitre_tactic", ""),
        "mitre_technique": data.get("mitre_technique", ""),
        "real_path": data.get("real_path", ""),
        "port": data.get("port", ""),
        "protocol": data.get("protocol", ""),
        "os": data.get("os", ""),
    }

    fm_yaml = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True)

    # Sections are model-decided: whatever headings it chose, in the order
    # it chose them. No fixed template here - the schema in prompts.py is
    # what constrains this, not this renderer.
    sections = data.get("sections", [])
    if not sections:
        # Fallback so a malformed/empty response still produces a usable
        # note rather than a blank body.
        sections = [{"heading": "Notes", "content": "(model returned no sections - check ingest_log.jsonl and the raw source file)"}]

    body_parts = []
    for sec in sections:
        heading = sec.get("heading", "Notes").strip()
        content = sec.get("content", "").strip()
        if content:
            body_parts.append(f"## {heading}\n{content}\n")

    references = data.get("references", [])
    if references:
        refs_md = "\n".join(f"- {r}" for r in references)
        body_parts.append(f"## References\n{refs_md}\n")

    body = f"""---
{fm_yaml}---

# {data['title']}

{chr(10).join(body_parts)}
"""
    return body
