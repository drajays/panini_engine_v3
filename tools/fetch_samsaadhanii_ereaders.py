"""
tools/fetch_samsaadhanii_ereaders.py — Saṃsādhanī e-reader word analyses as test gold.
──────────────────────────────────────────────────────────────────────────────────────

Source #17 of the roster: Saṃsādhanī (IIIT-H / University of Hyderabad). Its
e-reader (http://ereaders.samsaadhanii.in/books/ereaders/) is served from a
JSON tree:

    /books/data/books/books.json                              catalogue
    /books/data/books/<book>[/<part1>[/<part2>]]/analysis.json one row per word
    /books/data/books/<book>[/<part1>[/<part2>]]/slokas.json   verse text

Each analysis row carries ``word``, ``sandhied_word``, ``morph_in_context``
(e.g. ``कृ3{कर्तरि;लङ्;प्र;बहु;आत्मनेपदी;डुकृञ्;तनादिः}``) and
``kaaraka_sambandha``. It is **reference only** (CONSTITUTION Art. 6): tests
and tools read it, the rule path never does.

    python3 -m tools.fetch_samsaadhanii_ereaders --list
    python3 -m tools.fetch_samsaadhanii_ereaders                 # Gītā: fetch + build
    python3 -m tools.fetch_samsaadhanii_ereaders --no-fetch      # rebuild from raw/
    python3 -m tools.fetch_samsaadhanii_ereaders --book रघुवंश --raw-only

Raw downloads land in data/reference/samsaadhanii/raw/ (gitignored). The
build step writes the committed ``gita_tinanta.jsonl``: one row per tiṅanta
occurrence with the tag, the attested word and the parsed ``derive()``
inputs — tags only, no glosses or verse text.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

from core.transliterate import dev_to_slp1
from tools.samsaadhanii_tags import parse_tinanta_tag, tinanta_alternative

_ROOT = Path(__file__).resolve().parent.parent
OUT = _ROOT / "data" / "reference" / "samsaadhanii"
RAW = OUT / "raw"
BASE = "http://ereaders.samsaadhanii.in/books/data/books/"
GITA = "श्रीमद्भगवद्गीता"
GITA_TINANTA = OUT / "gita_tinanta.jsonl"


def _get(path: str) -> bytes:
    url = BASE + urllib.parse.quote(path)
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def catalogue() -> list[dict]:
    return json.loads(_get("books.json"))


def _slug(*parts: str | None) -> str:
    return "__".join(p for p in parts if p).replace("/", "_").replace(" ", "_")


def raw_path(book: str, part1: str | None = None, part2: str | None = None) -> Path:
    return RAW / f"{_slug(book, part1, part2)}.analysis.json"


def fetch(book: str, part1: str | None = None, part2: str | None = None) -> Path:
    rel = "/".join(p for p in (book, part1, part2) if p)
    RAW.mkdir(parents=True, exist_ok=True)
    dest = raw_path(book, part1, part2)
    dest.write_bytes(_get(rel + "/analysis.json"))
    print(f"  {dest.name}  {dest.stat().st_size:,} B")
    return dest


def _clean(word: str) -> tuple[str, str | None]:
    """(form to derive, text surface if different).

    ``गमः(अगमः)`` — māṅ-yoga surface (6.4.74) with the full form in brackets;
    ``(अस्ति)`` — adhyāhṛta, supplied by the annotator. Both derive the
    bracketed form: the engine is not given the māṅ context.
    """
    w = word.replace("ऽ", "").strip()
    m = re.match(r"^(.*?)\((.+)\)$", w)
    if not m:
        return w, None
    return m.group(2).strip(), (m.group(1).strip() or None)


def build_tinanta(raw: Path, out: Path) -> dict:
    rows = json.loads(raw.read_text(encoding="utf-8"))
    n = resolved = 0
    with out.open("w", encoding="utf-8") as f:
        for r in rows:
            tag = tinanta_alternative(r.get("morph_in_context") or "")
            if not tag:
                continue
            cell = parse_tinanta_tag(tag)
            word, surface = _clean(r.get("word") or "")
            rec = {
                "ref": f"{r['chaptno'].lstrip('0')}.{r['slokano'].lstrip('0')}",
                "anvaya_no": r.get("anvaya_no"),
                "word": word,
                "word_slp1": dev_to_slp1(word),
                "text_surface": surface,
                **cell.as_dict(),
                "key": cell.key(),
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
            resolved += cell.unresolved is None
    return {"tinanta_rows": n, "resolved": resolved}


def write_source(stats: dict) -> None:
    (OUT / "SOURCE.json").write_text(json.dumps({
        "source": "Saṃsādhanī e-readers (IIIT-H / University of Hyderabad)",
        "url": "http://ereaders.samsaadhanii.in/books/ereaders/",
        "api": BASE + "<book>/analysis.json",
        "book": GITA,
        "fetched": _dt.date.today().isoformat(),
        "kept": "tiṅanta tags + attested word only; no glosses or verse text",
        "stats": stats,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="print the book catalogue")
    ap.add_argument("--book", default=GITA)
    ap.add_argument("--part1")
    ap.add_argument("--part2")
    ap.add_argument("--no-fetch", action="store_true", help="rebuild from raw/ only")
    ap.add_argument("--raw-only", action="store_true", help="download without building")
    a = ap.parse_args(argv)

    if a.list:
        for b in catalogue():
            for p1 in b["part1"]:
                for p2 in p1["part2"]:
                    print(" / ".join(x for x in (b["book"], p1["part"], p2["part"]) if x))
        return 0
    raw = raw_path(a.book, a.part1, a.part2) if a.no_fetch else fetch(a.book, a.part1, a.part2)
    if a.raw_only:
        return 0
    if a.book != GITA or a.part1 or a.part2:
        print("build step is wired for the Gītā only; raw file kept")
        return 0
    stats = build_tinanta(raw, GITA_TINANTA)
    write_source(stats)
    print(f"  {GITA_TINANTA.name}  {stats}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
