"""
tools/fetch_shabda.py — vendor attested śabda-rūpa tables as a gold corpus.

ashtadhyayi.com publishes the full declension of ~9,000 stems
(``shabda/data2.txt`` in github.com/ashtadhyayi-com/data). Those tables are
*attested paradigms*: exactly the reference a subanta derivation should be
checked against, and a second opinion alongside Vidyut (Art. 19).

Only the stems this engine can be asked about are vendored — bulk upstream
data stays out of the repository (Art. 6), and the slice carries its
provenance. The tables land in ``data/reference/shabda_gold/``, which is
test-only by the same Article.

    python3 -m tools.fetch_shabda --list-local
    python3 -m tools.fetch_shabda            # refresh the slice from the network

Cell order in the source is vibhakti 1–7 × vacana 1–3, then sambodhana ×3;
this tool rewrites it as ``{"1-1": "रामः", …, "8-3": "रामाः"}`` to match the
engine's own (vibhakti, vacana) addressing, strips the सम्बोधन particle हे,
and keeps alternatives (``रामाद्-रामात्``) as a list.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

SOURCE_URL = (
    "https://raw.githubusercontent.com/ashtadhyayi-com/data/master/shabda/data2.txt"
)
OUT_DIR = _ROOT / "data" / "reference" / "shabda_gold"

LINGA = {"P": "pulliṅga", "S": "strīliṅga", "N": "napuṃsaka"}

# (urlid in the source, stem in SLP1 as this engine names it). The upstream ids
# use their own romanisation — @zambhu1 for शम्भु, @jJAna1 for ज्ञान — so the
# mapping is explicit rather than derived.
WANTED: tuple[tuple[str, str], ...] = (
    ("@rAma1", "rAma"),
    ("@hari1", "hari"),
    ("@zambhu1", "SamBu"),
    ("@guru1", "guru"),
    ("@sarva1", "sarva"),
    ("@anya1", "anya"),
    ("@jJAna1", "jYAna"),
    ("@nadI1", "nadI"),
    ("@vAyu1", "vAyu"),
    ("@agni1", "agni"),
    ("@latA1", "latA"),
    ("@phala1", "Pala"),
    ("@rAdhA1", "rADA"),
)


def _cells(forms: str) -> dict[str, list[str]]:
    """The source's flat 24 into (vibhakti, vacana) keys."""
    parts = [f.strip() for f in forms.split(";")]
    if len(parts) != 24:
        raise ValueError(f"expected 24 forms, got {len(parts)}")
    cells: dict[str, list[str]] = {}
    for index, raw in enumerate(parts):
        vibhakti, vacana = divmod(index, 3)
        text = raw.removeprefix("हे ").strip()
        cells[f"{vibhakti + 1}-{vacana + 1}"] = [v for v in text.split("-") if v]
    return cells


def fetch(url: str = SOURCE_URL) -> list[dict[str, Any]]:
    with urllib.request.urlopen(url) as response:          # noqa: S310 — pinned host
        return json.loads(response.read().decode("utf-8"))["data"]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Vendor attested śabda paradigms.")
    ap.add_argument("--list-local", action="store_true")
    ap.add_argument("--source", default=SOURCE_URL)
    args = ap.parse_args(argv)

    if args.list_local:
        for path in sorted(OUT_DIR.glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            print(f"  {path.stem:<22} {data['word']:<10} {data['linga']:<12} "
                  f"{len(data['cells'])} cells")
        return 0

    rows = {row.get("urlid"): row for row in fetch(args.source)}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    for urlid, stem in WANTED:
        row = rows.get(urlid)
        if row is None:
            print(f"  gap: {urlid} not in the source")
            continue
        payload = {
            "_provenance": {
                "source_repo": "github.com/ashtadhyayi-com/data",
                "source_path": "shabda/data2.txt",
                "urlid": urlid,
                "fetched": "2026-09-15",
                "note": (
                    "Attested paradigm, vendored as a test-only reference "
                    "(CONSTITUTION Art. 6). Upstream publishes no licence file; "
                    "only the stems this engine is asked about are kept."
                ),
            },
            "stem_slp1": stem,
            "word": row["word"],
            "linga": LINGA[row["linga"]],
            "artha": row.get("artha", ""),
            "cells": _cells(row["forms"]),
        }
        path = OUT_DIR / f"{stem}_{LINGA[row['linga']]}.json"
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
        written += 1
        print(f"  {stem:<8} {row['word']:<10} {LINGA[row['linga']]:<12} → "
              f"{path.relative_to(_ROOT)}")
    print(f"\n  {written}/{len(WANTED)} paradigms vendored")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
