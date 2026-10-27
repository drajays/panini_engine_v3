"""tools/build_ganapatha_full.py — data/inputs/ganapatha_full.json: every gaṇa of the Gaṇapāṭha (ashtadhyayi.com, via the brain) in SLP1.

A gaṇa is a lexical fact like the dhātupāṭha (engine/lexicon.py): a sūtra that says ``gargādibhyaḥ`` reads its members from here. The brain is read
once, at build time, never from a ``cond`` (Art. 6). Notes in <<…>> and the vārttika marks are dropped; an ākṛtigaṇa stays open (the file says so)."""
from __future__ import annotations

import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
OUT = ROOT / "data" / "inputs" / "ganapatha_full.json"
DB = Path.home() / "data-master" / "ashtadhyayi-ai" / "db" / "ashtadhyayi.db"


def main() -> int:
    from phonology.tokenizer import devanagari_to_slp1_flat

    con = sqlite3.connect(DB)
    out: dict = {"_doc": __doc__.strip().splitlines()[0], "source": "ashtadhyayi-ai/db/ashtadhyayi.db table ganapath", "ganas": {}}
    for _id, name_slp1, sutra, words in con.execute("select id, name_slp1, sutra, words from ganapath order by id"):
        raw = re.sub(r"<<.*?>>", " ", words or "")
        members = []
        for w in re.split(r"[।॥\n]+", raw):
            w = w.strip()
            if not w or "(" in w:
                continue
            members.append(devanagari_to_slp1_flat(w))
        key = name_slp1 if name_slp1 not in out["ganas"] else f"{name_slp1}#{sutra}"      # two gaṇas may share a name (SarAdiH of 4.3.144 and of 6.3.120)
        out["ganas"][key] = {"sutra": sutra, "members": members, "akrti": "AkftigaRa" in (name_slp1 or "")}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(out['ganas'])} gaṇas → {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
