"""tools/build_ganapatha_full.py — data/inputs/ganapatha_full.json: every gaṇa of the Gaṇapāṭha (ashtadhyayi.com, via the brain) in SLP1.

A gaṇa is a lexical fact like the dhātupāṭha (engine/lexicon.py): a sūtra that says ``gargādibhyaḥ`` reads its members from here. The brain is read
once, at build time, never from a ``cond`` (Art. 6). Notes in <<…>> and the vārttika marks are dropped from ``members``; an ākṛtigaṇa stays open (the file says so).

``data/inputs/ganapatha_overlay.json`` (tools/intake_patha.py, Kāśikā-verified) is applied on top: sūtra-id fixes, ākṛtigaṇa flags (``akrti``), the
gaṇasūtras that only enumerate members expanded in place (sarvādi), the notes kept as ``gaNasUtra`` (rules) and ``members_restricted`` (member +
sense, candidates), ``derived`` (vargyādi), and the sub-gaṇas the Kāśikā names as a stretch of another gaṇa (haritādi, kaṇvādi, pūrvādi, ḍatarādi)."""
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
OVERLAY = ROOT / "data" / "inputs" / "ganapatha_overlay.json"


def main() -> int:
    from phonology.tokenizer import devanagari_to_slp1_flat

    con = sqlite3.connect(DB)
    out: dict = {"_doc": __doc__.strip().splitlines()[0], "source": "ashtadhyayi-ai/db/ashtadhyayi.db table ganapath", "ganas": {}}
    ov = json.loads(OVERLAY.read_text(encoding="utf-8")) if OVERLAY.exists() else {}
    for _id, name_slp1, sutra, words in con.execute("select id, name_slp1, sutra, words from ganapath order by id"):
        key = name_slp1 if name_slp1 not in out["ganas"] else f"{name_slp1}#{sutra}"      # two gaṇas may share a name (SarAdiH of 4.3.144 and of 6.3.120)
        expand = ov.get("expansions", {}).get(key, {})
        members = []
        for seg in re.split(r"(<<.*?>>)", words or ""):
            if seg.startswith("<<"):
                note = "".join(devanagari_to_slp1_flat(w) for w in seg[2:-2].split())
                members.extend(expand.get(note, []))        # an enumerating gaṇasūtra, spelled out by the overlay
                continue
            for w in re.split(r"[।॥\n]+", seg):
                w = w.strip()
                if not w or "(" in w:
                    continue
                members.append(devanagari_to_slp1_flat(w))
                if members[-1] == "tAlAdDanuzi":
                    members.append("tAla")          # the gaṇasūtra tālād dhanuṣi names its first member (S18: the dhanus restriction is not modelled)
        g = {"sutra": ov.get("sutra_fix", {}).get(key, {}).get("sutra", sutra), "members": members, "akrti": "AkftigaRa" in (name_slp1 or "") or key in ov.get("akrti", {})}
        g.update({k: v for k, v in ov.get("extra", {}).get(key, {}).items() if v})
        out["ganas"][key] = g
    for key, sg in ov.get("sub_ganas", {}).items():      # a stretch of another gaṇa, named by the Kāśikā: members read off the parent in its own order
        parent = out["ganas"][sg["of"]]["members"]
        i = parent.index(sg["from"])
        members = parent[i:i + sg["size"]] if sg["size"] else parent[i:]
        assert sg["size"] is None or len(members) == sg["size"], key
        out["ganas"][key] = {"sutra": sg["sutra"], "members": members, "akrti": False, "sub_gana_of": sg["of"], "evidence": sg["evidence"]}
    for k in ("open_not_in_patha", "sutra_aliases"):
        if ov.get(k):
            out[k] = ov[k]
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(out['ganas'])} gaṇas → {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
