"""tools/kashika_quote_check.py — is every Devanāgarī "Kāśikā:" quote in a sūtra docstring verbatim in the brain's Kāśikā?

    python3 -m tools.kashika_quote_check [-v]

Brain = final reference (docs/BRAIN_FINAL_REFERENCE_PLAN.md, B1). Compared per line (split at …), ignoring spacing,
punctuation, avagraha and svara marks. A paraphrase labelled "Kāśikā" is reported; tests/constitutional/
test_kashika_quotes_ratchet.py keeps the count from rising.
"""
from __future__ import annotations

import os
import re
import sqlite3
import sys
import unicodedata
from contextlib import closing
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRAIN_DB = Path(os.environ.get("PANINI_BRAIN", Path.home() / "data-master" / "ashtadhyayi-ai")) / "db" / "ashtadhyayi.db"
_END = re.compile(r"\n\s*(?:pratyudāharaṇa|Cross|Source|SK|Padamañjarī|Mahābhāṣya|Owner|- )")


def _sq(x: str) -> str:
    x = "".join(ch for ch in unicodedata.normalize("NFC", x or "") if ch not in "\u0951\u0952\u1cda")
    return re.sub(r"[\s।॥,;:.\-–—'\"?ऽ()\[\]]+", "", x)


def unverified() -> dict[str, list[str]]:
    with closing(sqlite3.connect(BRAIN_DB)) as db:
        kas = {s: c for s, c in db.execute("select sutra_id, content from texts where source='kashika'")}
    out: dict[str, list[str]] = {}
    for f in sorted((ROOT / "sutras").rglob("sutra_*.py")):
        src = f.read_text(encoding="utf-8")
        m = re.search(r"sutra_id\s*=\s*['\"](\d+\.\d+\.\d+)['\"]", src)
        if not m or not src.startswith('"""'):
            continue
        block = re.search(r"Kāśikā[^\n]*\n?((?:[ \t]{2,}[^\n]*\n?)*)", src.split('"""')[1])
        if not block or "Kāśikā on " in block.group(0)[:12]:
            continue
        text = _END.split(block.group(0))[0]
        frags = [x for part in re.split(r"\n|…|\.\.\.", text)
                 for x in re.findall(r"[ऀ-ॿ][ऀ-ॿ\s।॥,;:'\-ऽ]*", part) if len(_sq(x)) >= 6]
        k = _sq(kas.get(m[1], ""))
        miss = [x.strip() for x in frags if _sq(x) not in k]
        if miss:
            out[m[1]] = miss
    return out


def main(argv: list[str]) -> int:
    bad = unverified()
    print(f"sūtra files whose 'Kāśikā' text is not verbatim in the brain: {len(bad)}")
    if "-v" in argv:
        for s, v in sorted(bad.items(), key=lambda kv: tuple(map(int, kv[0].split(".")))):
            print(f"  {s} | {v[0][:70]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
