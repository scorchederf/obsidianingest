"""
vault_index.py
Scans the existing vault and builds a lookup so new notes can link to
existing ones by exact title/entity match, without needing embeddings
for the common case.
"""

import re
from pathlib import Path

import yaml

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


class VaultIndex:
    """
    index.by_title[category] = {lowercase_title: relative_path}
    Also keeps a flat title->path map across all categories for
    general lookups, and the raw category tree (as a list of relative
    paths) to hand to the LLM for classification context.
    """

    def __init__(self, vault_path: Path):
        self.vault_path = vault_path
        self.by_title: dict[str, dict[str, str]] = {}
        self.flat_titles: dict[str, str] = {}
        self.all_paths: list[str] = []
        self._build()

    def _build(self):
        for md_file in self.vault_path.rglob("*.md"):
            rel_path = str(md_file.relative_to(self.vault_path))
            self.all_paths.append(rel_path)

            text = md_file.read_text(errors="ignore")
            fm = parse_frontmatter(text)
            title = fm.get("title") or md_file.stem
            category = fm.get("category") or rel_path.split("/")[0]

            title_key = title.strip().lower()
            self.by_title.setdefault(category, {})[title_key] = rel_path
            self.flat_titles[title_key] = rel_path

    def find(self, category: str, entity_name: str) -> str | None:
        """Exact (case-insensitive) match within a category."""
        return self.by_title.get(category, {}).get(entity_name.strip().lower())

    def find_anywhere(self, entity_name: str) -> str | None:
        """Exact match across the whole vault, ignoring category."""
        return self.flat_titles.get(entity_name.strip().lower())

    def tree_summary(self, max_entries: int = 400) -> str:
        """
        A compact text listing of the vault, given to the LLM so it can
        decide where a new note belongs and whether related notes exist.
        Truncated for large vaults to keep the prompt small.
        """
        paths = sorted(self.all_paths)[:max_entries]
        return "\n".join(paths)

    def register(self, category: str, title: str, rel_path: str):
        """Call after creating a new (or stub) note so later notes in the
        same batch can link to it without re-scanning the vault."""
        title_key = title.strip().lower()
        self.by_title.setdefault(category, {})[title_key] = rel_path
        self.flat_titles[title_key] = rel_path
        self.all_paths.append(rel_path)
