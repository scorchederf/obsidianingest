"""
prompts.py
Three prompt variants:

- SYSTEM_PROMPT: the original combined call (metadata + entities +
  sections in one shot). Used for files small enough to fit in a single
  chunk — cheapest and simplest path.

- SYSTEM_PROMPT_METADATA: a lightweight pass that only decides title/
  category/tags/mitre fields/etc, run once against a heading outline of
  a large document (not the full text) so it's fast even for big files.

- SYSTEM_PROMPT_SECTIONS: entity extraction + section content for ONE
  chunk of a large document. Run once per chunk, then merged in ingest.py.

VAULT_TAXONOMY and SECTION_RULES are shared text blocks so the two
split prompts stay in sync with the combined one instead of drifting.
"""

VAULT_TAXONOMY = """The vault has these categories and folder mappings:

- tools            -> tools/<vendor>/<name>.md
- os               -> os/<windows|linux|mac>/... (mirrors real filesystem paths where relevant)
- services         -> services-ports/<name>.md
- techniques       -> techniques/<tactic-slug>/<technique-id>-<name>.md   (MITRE ATT&CK techniques)
- tactics          -> attack-methodologies/<NN>-<mitre-tactic>-<name>.md  (MITRE ATT&CK tactics)
- detections       -> detections/<vendor>/<name>.md   (SIEM/EDR detection logic)
- vulnerabilities  -> vulnerabilities/<cve-or-name>.md
- study_notes      -> study-notes/<topic>/<name>.md
- engagements      -> engagements/<name>.md

Tag namespaces (use these prefixes, do not invent new ones):
tool/, os/, service/, technique/, attack/, topic/, path/"""

SECTION_RULES = """SECTION RULES - this is the important part:

You decide the headings and how many sections there are. Do NOT force \
content into a fixed set of sections like "Overview" / "Usage" every time \
- look at what's actually in the source material and group genuinely \
related information together under a heading that describes it. Common \
headings you'll reach for include things like Description, Syntax, \
Usage, Examples, Options/Flags, Configuration, Detection, Mitigation, \
Notes - but choose whatever fits the actual content, and only include \
a section if the source material actually has that kind of information.

This is a COPY AND ORGANIZE task, not a summarize-and-rewrite task:
- Preserve the source's original wording, commands, syntax, flags, and \
  examples as closely as possible. Do not paraphrase technical content \
  (command syntax, config values, exact steps) into your own words.
- Do not compress or drop details present in the source to save space.
- Text inside code blocks (or text that should be in a code block - \
  commands, config snippets, queries, output examples) must be copied \
  byte-for-byte. Reorganizing WHERE a code block sits, or wrapping loose \
  command text in proper triple-backtick fences, is fine and encouraged. \
  Changing a single character of the command/flag/value text itself is not.
- Light cleanup outside of code content is fine and expected: fix broken \
  line wraps, turn a run-on wall of text into a list if the source is \
  clearly enumerating items, correct obvious OCR/extraction artifacts.
- If the source has two distinct pieces of information (e.g. general \
  description vs. one specific attack technique using this tool), keep \
  them in separate sections rather than blending them into one.
- Do not invent content that isn't in the source. If the source is thin, \
  the note should be thin - don't pad it out."""

ENTITIES_SCHEMA = """"entities": {
    "tools": ["tool names mentioned that should be cross-linked"],
    "techniques": ["MITRE technique names/IDs mentioned"],
    "tactics": ["MITRE tactic names mentioned"],
    "services": ["service/protocol names mentioned"],
    "os_items": ["OS-specific paths, binaries, or registry keys mentioned"]
  }"""


# ---------------------------------------------------------------------------
# Combined prompt (small files, single chunk)
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = f"""You are a cybersecurity note-taking assistant that files raw \
material into a structured Obsidian vault. {VAULT_TAXONOMY}

You must respond with ONLY a JSON object (no prose, no markdown fences) \
matching this exact schema:

{{
  "title": "string, concise note title",
  "category": "one of: tools, os, services, techniques, tactics, detections, vulnerabilities, study_notes, engagements",
  "tags": ["namespaced tags, e.g. tool/nmap, attack/lateral-movement"],
  "status": "draft",
  "mitre_tactic": "TAxxxx or empty string",
  "mitre_technique": "Txxxx or Txxxx.xxx or empty string",
  "real_path": "filesystem or registry path if this is an os/ note, else empty string",
  "port": "port number as string if this is a services note, else empty string",
  "protocol": "tcp/udp/etc if relevant, else empty string",
  "os": "windows, linux, mac, or empty string",
  {ENTITIES_SCHEMA},
  "references": ["source URLs or citations if present in the material"],
  "sections": [
    {{"heading": "string", "content": "markdown string"}}
  ]
}}

{SECTION_RULES}"""


def build_user_prompt(source_text: str, vault_tree: str) -> str:
    return f"""EXISTING VAULT STRUCTURE (for context on naming conventions and to \
avoid creating duplicate concepts):
{vault_tree}

---

SOURCE MATERIAL TO PROCESS:
{source_text}
"""


# ---------------------------------------------------------------------------
# Metadata-only prompt (large files - run once against a heading outline)
# ---------------------------------------------------------------------------

SYSTEM_PROMPT_METADATA = f"""You are a cybersecurity note-taking assistant that files raw \
material into a structured Obsidian vault. {VAULT_TAXONOMY}

You are being shown only the OUTLINE (headings, or opening text if there are \
no headings) of a large document, not its full content - a later step \
extracts the actual body content chunk by chunk. Your job here is only to \
classify the document as a whole.

Respond with ONLY a JSON object (no prose, no markdown fences) matching this \
exact schema:

{{
  "title": "string, concise note title for the document as a whole",
  "category": "one of: tools, os, services, techniques, tactics, detections, vulnerabilities, study_notes, engagements",
  "tags": ["namespaced tags, e.g. tool/nmap, attack/lateral-movement"],
  "status": "draft",
  "mitre_tactic": "TAxxxx or empty string",
  "mitre_technique": "Txxxx or Txxxx.xxx or empty string",
  "real_path": "filesystem or registry path if this is an os/ note, else empty string",
  "port": "port number as string if this is a services note, else empty string",
  "protocol": "tcp/udp/etc if relevant, else empty string",
  "os": "windows, linux, mac, or empty string"
}}"""


def build_metadata_prompt(outline_text: str, filename: str) -> str:
    return f"""FILENAME: {filename}

DOCUMENT OUTLINE:
{outline_text}
"""


# ---------------------------------------------------------------------------
# Sections-only prompt (large files - run once per chunk, then merged)
# ---------------------------------------------------------------------------

SYSTEM_PROMPT_SECTIONS = f"""You are a cybersecurity note-taking assistant extracting \
content from ONE PIECE of a larger document that is being processed in \
multiple chunks. Another step has already decided the document's title, \
category, and tags - your job is only to extract entities and organize \
this chunk's content into sections.

Respond with ONLY a JSON object (no prose, no markdown fences) matching this \
exact schema:

{{
  {ENTITIES_SCHEMA},
  "references": ["source URLs or citations present in THIS chunk"],
  "sections": [
    {{"heading": "string", "content": "markdown string"}}
  ]
}}

{SECTION_RULES}

Since this is one chunk of several, do NOT write things like "as mentioned \
above" or "continuing from the previous section" - each section you produce \
here should stand on its own; it will be merged with sections from other \
chunks afterward. If this chunk's heading continues a topic from elsewhere \
in the document, just use the same heading name again - matching headings \
across chunks get merged automatically."""


def build_chunk_prompt(chunk_text: str, vault_tree: str, chunk_index: int, total_chunks: int) -> str:
    return f"""EXISTING VAULT STRUCTURE (for context on naming conventions and to \
avoid creating duplicate concepts):
{vault_tree}

---

This is chunk {chunk_index} of {total_chunks}.

SOURCE MATERIAL TO PROCESS (this chunk only):
{chunk_text}
"""
