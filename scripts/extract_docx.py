#!/usr/bin/env python3
"""Extract readable text from DOCX files into plain text files."""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def text_from_paragraph(paragraph: ET.Element) -> str:
    parts: list[str] = []
    for node in paragraph.iter():
        if node.tag == f"{{{NS['w']}}}t" and node.text:
            parts.append(node.text)
        elif node.tag == f"{{{NS['w']}}}tab":
            parts.append("\t")
        elif node.tag == f"{{{NS['w']}}}br":
            parts.append("\n")
    return "".join(parts).strip()


def text_from_table(table: ET.Element) -> str:
    rows: list[str] = []
    for row in table.findall(".//w:tr", NS):
        cells: list[str] = []
        for cell in row.findall("./w:tc", NS):
            paragraphs = [
                text
                for paragraph in cell.findall(".//w:p", NS)
                if (text := text_from_paragraph(paragraph))
            ]
            cells.append(" / ".join(paragraphs))
        if any(cells):
            rows.append(" | ".join(cells))
    return "\n".join(rows).strip()


def extract_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml")

    root = ET.fromstring(xml)
    body = root.find("w:body", NS)
    if body is None:
        return ""

    blocks: list[str] = []
    for child in body:
        if child.tag == f"{{{NS['w']}}}p":
            text = text_from_paragraph(child)
        elif child.tag == f"{{{NS['w']}}}tbl":
            text = text_from_table(child)
        else:
            text = ""

        if text:
            blocks.append(text)

    content = "\n\n".join(blocks)
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content.strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract DOCX text into .txt files.")
    parser.add_argument("input_dir", nargs="?", default="input", help="Directory with .docx files.")
    parser.add_argument("output_dir", nargs="?", default="extracted", help="Directory for extracted .txt files.")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    docx_files = sorted(input_dir.glob("*.docx"))
    if not docx_files:
        raise SystemExit(f"No DOCX files found in {input_dir}")

    for docx_file in docx_files:
        output_file = output_dir / f"{docx_file.stem}.txt"
        output_file.write_text(extract_docx(docx_file), encoding="utf-8")
        print(f"Extracted {docx_file} -> {output_file}")


if __name__ == "__main__":
    main()
