"""tools/build_scope_index.py — P1: sūtra → governing adhikāra heads, from the brain (read-only).

    python3 -m tools.build_scope_index        # writes data/inputs/adhikara_scope_index.json
Source: brain `edges rel='adhikara'` (head → member, ashtadhyayi.com). Data only; the scheduler does not read it yet (shadow phase).
"""
from __future__ import annotations

import json
import sqlite3
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = Path.home() / "data-master" / "ashtadhyayi-ai" / "db" / "ashtadhyayi.db"
OUT = ROOT / "data" / "inputs" / "adhikara_scope_index.json"


def _key(s: str) -> tuple[int, ...]:
    return tuple(int(p) for p in s.split("."))


def main() -> dict:
    c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    heads: dict[str, list[str]] = defaultdict(list)
    for src, dst in c.execute("select src, dst from edges where rel='adhikara'"):
        h, m = src.removeprefix("s:"), dst.removeprefix("s:")
        if h != m:
            heads[m].append(h)
    ids = [r[0] for r in c.execute("select id from sutras")]
    idx = {s: sorted(set(heads.get(s, [])), key=_key) for s in sorted(ids, key=_key)}
    OUT.write_text(json.dumps({"note": "sutra -> governing adhikara heads (brain edges rel=adhikara); generated, do not edit",
                               "scope": idx}, ensure_ascii=False, indent=0) + "\n")
    return idx


if __name__ == "__main__":
    i = main()
    print(f"{len(i)} sutras, {sum(1 for v in i.values() if v)} governed by >=1 head, {len({h for v in i.values() for h in v})} heads")
