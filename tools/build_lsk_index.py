"""
tools/build_lsk_index.py — sūtra → pages of the LSK study guides that cite it.
──────────────────────────────────────────────────────────────────────────────

Medhā Michika's *Study Guide to Pāṇini-Sūtra through Laghusiddhāntakaumudī*
(Parts 1–12, Arsha Avinash Foundation) print their Devanāgarī in a legacy
font, but sūtra numbers are plain ASCII in the text layer, so ``pdftotext``
recovers every citation exactly. Only ids and page numbers are stored — never
the books' text (all rights reserved).

    python3 -m tools.build_lsk_index [--src ~/read_panini]

Writes ``data/reference/lsk/sutra_pages.json``:
    {"7.1.15": [[2, 60], [2, 61], [3, 12]], ...}   # [part, pdf page]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
OUT = _ROOT / "data" / "reference" / "lsk" / "sutra_pages.json"

PARTS = {
    "LSK_1.pdf": 1, "LSK_2.pdf": 2, "LSK3.pdf": 3, "LSK_4.pdf": 4,
    "LSK_5.pdf": 5, "Laghu_6.pdf": 6, "LaghuSK_7.pdf": 7, "LSK_8.pdf": 8,
    "LSK_9.pdf": 9, "LSK_10.pdf": 10, "LSK_11.pdf": 11, "LSK12.pdf": 12,
}
_SID = re.compile(r"(?<![\d.])([1-8])\.([1-4])\.(\d{1,3})(?![\d.])")


def known_sutras() -> set[str]:
    """Ids with a file in sutras/ — drops OCR-ish noise like 1.1.155."""
    return {".".join(p.stem.split("_")[1:]) for p in (_ROOT / "sutras").rglob("sutra_*.py")}


def build(src: Path) -> dict[str, list[list[int]]]:
    known = known_sutras()
    index: dict[str, set[tuple[int, int]]] = defaultdict(set)
    for name, part in PARTS.items():
        text = subprocess.run(["pdftotext", "-enc", "UTF-8", str(src / name), "-"],
                              capture_output=True, text=True, check=True).stdout
        for page_no, page in enumerate(text.split("\f"), 1):
            for m in _SID.findall(page):
                sid = ".".join(m)
                if sid in known:
                    index[sid].add((part, page_no))
    key = lambda s: tuple(map(int, s.split(".")))
    return {s: [list(p) for p in sorted(index[s])] for s in sorted(index, key=key)}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, default=Path.home() / "read_panini")
    args = ap.parse_args(argv)
    index = build(args.src)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"{len(index)} sūtras → {OUT.relative_to(_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
