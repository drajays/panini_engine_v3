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


# Kāśikā 4.4.75: yat governs up to (not incl.) 5.1.5 tasmai hitam; the brain edges stop at the pāda end 4.4.144.
# 3.3.141 vā lṛṅ (to 3.3.151, prāk 3.3.152) and 5.1.78 kālāt (yāvat 5.1.97) are missing from the brain edges, same source.
EXTEND = {"4.4.75": ["5.1.1", "5.1.2", "5.1.3", "5.1.4"],
          "3.3.141": [f"3.3.{n}" for n in range(142, 152)],
          "5.1.78": ["5.1.97"]}


def _key(s: str) -> tuple[int, ...]:
    return tuple(int(p) for p in s.split("."))


def main() -> dict:
    c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    heads: dict[str, list[str]] = defaultdict(list)
    for src, dst in c.execute("select src, dst from edges where rel='adhikara'"):
        h, m = src.removeprefix("s:"), dst.removeprefix("s:")
        if h != m:
            heads[m].append(h)
    for h, ms in EXTEND.items():
        for m in ms:
            heads[m].append(h)
    ids = [r[0] for r in c.execute("select id from sutras")]
    c.close()
    idx = {s: sorted(set(heads.get(s, [])), key=_key) for s in sorted(ids, key=_key)}
    OUT.write_text(json.dumps({"note": "sutra -> governing adhikara heads (brain edges rel=adhikara); generated, do not edit",
                               "scope": idx}, ensure_ascii=False, indent=0) + "\n")
    return idx


if __name__ == "__main__":
    i = main()
    print(f"{len(i)} sutras, {sum(1 for v in i.values() if v)} governed by >=1 head, {len({h for v in i.values() for h in v})} heads")
