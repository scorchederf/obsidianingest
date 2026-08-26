"""
extract.py
Turns whatever file got dropped in the inbox into plain text.
Add new suffixes here as you need them (e.g. .eml, .csv).
"""

from pathlib import Path


def extract_text(filepath: Path) -> str:
    suffix = filepath.suffix.lower()

    if suffix in (".txt", ".md", ".log", ".conf", ".cfg", ".ini"):
        return filepath.read_text(errors="ignore")

    if suffix == ".pdf":
        return _extract_pdf(filepath)

    if suffix == ".docx":
        return _extract_docx(filepath)

    if suffix in (".html", ".htm"):
        return _extract_html(filepath)

    if suffix == ".json":
        return filepath.read_text(errors="ignore")

    raise ValueError(
        f"No extractor for '{suffix}' files. Add one in extract.py, "
        f"or convert '{filepath.name}' manually before dropping it in the inbox."
    )


def _extract_pdf(filepath: Path) -> str:
    import pypdf

    reader = pypdf.PdfReader(str(filepath))
    text_parts = []
    for page in reader.pages:
        text_parts.append(page.extract_text() or "")
    text = "\n".join(text_parts).strip()

    if not text:
        # Likely a scanned/image PDF. OCR fallback.
        text = _ocr_pdf(filepath)

    return text


def _ocr_pdf(filepath: Path) -> str:
    try:
        import pytesseract
        from pdf2image import convert_from_path
    except ImportError:
        raise RuntimeError(
            f"'{filepath.name}' looks like a scanned PDF with no extractable text. "
            "Install pytesseract + pdf2image (and the tesseract/poppler binaries) "
            "to enable OCR fallback, or provide a text-based version."
        )

    pages = convert_from_path(str(filepath))
    text_parts = [pytesseract.image_to_string(page) for page in pages]
    return "\n".join(text_parts).strip()


def _extract_docx(filepath: Path) -> str:
    import docx

    doc = docx.Document(str(filepath))
    return "\n".join(p.text for p in doc.paragraphs)


def _extract_html(filepath: Path) -> str:
    from bs4 import BeautifulSoup

    html = filepath.read_text(errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text(separator="\n").strip()
