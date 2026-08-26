"""
chunking.py
Splits large source documents into model-sized pieces on markdown
heading boundaries (so each chunk is a coherent unit, not an arbitrary
character cut mid-sentence). Falls back to paragraph splitting for
source text with no heading structure (e.g. plain-text dumps, some PDFs).
"""

import re

HEADING_RE = re.compile(r"^(#{1,3})\s+.*$", re.MULTILINE)


def split_into_chunks(text: str, max_chars: int = 6000) -> list[str]:
    if len(text) <= max_chars:
        return [text]

    headings = list(HEADING_RE.finditer(text))
    if len(headings) >= 2:
        return _split_on_headings(text, headings, max_chars)
    return _split_on_paragraphs(text, max_chars)


def _split_on_headings(text: str, headings: list[re.Match], max_chars: int) -> list[str]:
    boundaries = [h.start() for h in headings] + [len(text)]
    chunks = []
    current = text[:boundaries[0]]  # anything before the first heading

    for i in range(len(boundaries) - 1):
        section = text[boundaries[i]:boundaries[i + 1]]

        if len(section) > max_chars:
            # A single heading's section is itself too big (e.g. one huge
            # h1 with no sub-headings) — fall back to paragraph splitting
            # just for this section. Re-prepend the heading line to each
            # resulting piece so the model still has that context — without
            # this, a chunk deep inside an oversized section has no idea
            # what heading it belongs under.
            if current:
                chunks.append(current)
                current = ""
            heading_line = section.split("\n", 1)[0]
            sub_chunks = _split_on_paragraphs(section, max_chars)
            for j, sub in enumerate(sub_chunks):
                if j == 0:
                    chunks.append(sub)
                else:
                    chunks.append(f"{heading_line} (continued)\n{sub}")
            continue

        if len(current) + len(section) > max_chars and current:
            chunks.append(current)
            current = section
        else:
            current += section

    if current:
        chunks.append(current)
    return chunks


def _split_on_paragraphs(text: str, max_chars: int) -> list[str]:
    paragraphs = text.split("\n\n")
    chunks = []
    current = ""

    for p in paragraphs:
        if len(current) + len(p) > max_chars and current:
            chunks.append(current)
            current = p
        else:
            current += ("\n\n" if current else "") + p

    if current:
        chunks.append(current)
    return chunks


def outline(text: str, max_chars: int = 3000) -> str:
    """
    A cheap heading-only outline of a large document, used for the
    metadata pass (title/category/tags/mitre fields) so that call doesn't
    need the entire document — just enough structure to classify it.
    Falls back to the document's opening text if it has no headings.
    """
    headings = [m.group(0).strip() for m in HEADING_RE.finditer(text)]
    if not headings:
        return text[:max_chars]
    return "\n".join(headings)[:max_chars]
