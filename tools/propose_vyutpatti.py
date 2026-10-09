"""tools/propose_vyutpatti.py — build data/inputs/subanta_lexicon.json (AMENDMENT 22, Art. 17).

*Analysis proposes, generation verifies.* For each stem of the ashtadhyayi.com noun list (the vocabulary only — never its forms,
Art. 19) a pattern proposes components; an entry is written **only if the forward engine reproduces the stem string from them**
(``engine.lexicon.compose``). Stems that cannot be reproduced are printed as the Art. 18 worklist: each names the sūtra or
component the engine lacks.

    .venv/bin/python -m tools.propose_vyutpatti            # write the lexicon
    .venv/bin/python -m tools.propose_vyutpatti --dry-run
Classes proposed: matup/vatup (-mat/-vat after a base that is itself a listed stem), tṛc/tṛn agent nouns (-tṛ/-ṭṛ from a dhātu found
by consonant skeleton and proved by the loop), and the curated list below (scholar-authored, each with its source).
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))

OUT = _ROOT / "data" / "inputs" / "subanta_lexicon.json"
LINGA = {"P": "pulliṅga", "S": "strīliṅga", "N": "napuṃsaka"}

# Curated: the compound-with-han stems whose second member is the root *han* (kvip, 3.2.87 brahmabhrūṇavṛtreṣu kvip; Kāśikā
# adds śatru- etc. under the same affix). plīhan / ahan / dīrghāhan are *not* these and are left unanalysed.
CURATED = [
    ("vftrahan", "vftra", "Kāśikā 3.2.87 brahmabhrūṇavṛtreṣu kvip"),
    ("vIrahan", "vIra", "Kāśikā 3.2.87 (vīrahan: han + kvip)"),
    ("tamisrahan", "tamisra", "han + kvip (tamisrahā 'destroyer of darkness')"),
    ("Satruhan", "Satru", "Kāśikā 3.2.87 / 3.2.? śatruhan: han + kvip"),
]


# Curated matup stems the unit tests pin (listed only if not already proposed from the noun list).
CURATED_MATUP = [("guRavat", "guRa", "SK 5.2.94 / 7.1.70: guṇavān")]


def _vocab():
    from phonology.tokenizer import devanagari_to_slp1_flat
    from tools.fetch_ashtadhyayi_data import path
    rows = json.loads(path("shabda/data2.txt").read_text())["data"]
    out = []
    for r in rows:
        if r.get("linga") in LINGA:
            try:
                out.append((devanagari_to_slp1_flat(r["word"]), LINGA[r["linga"]]))
            except Exception:
                pass
    return sorted(set(out))


def _gen_job(row):
    """Generate tṛc from one dhātu row; returns (surface, dhatu_id, upadesha) or None."""
    from engine import lexicon
    e = {"stem": "?", "linga": "pulliṅga",
         "components": [{"kind": "dhatu", "upadesha": row["upadesha_slp1"], "dhatu_id": row["dhatupatha_id"]}, {"kind": "krt", "upadesha": "tfc"}]}
    try:
        surface, _ = lexicon.generate(e)
    except Exception:
        return None
    return surface, row["dhatupatha_id"], row["upadesha_slp1"]


def _try(entry):
    from engine import lexicon
    try:
        lexicon.compose(entry)
        return entry
    except Exception as e:                                   # LexiconGap or a rule that does not exist yet
        return {"gap": f"{entry['stem']}: {type(e).__name__}: {e}"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    import sutras  # noqa: F401
    from pipelines.dhatupatha import iter_dhatu_entries
    vocab = _vocab()
    stems = {s for s, _ in vocab}
    entries, gaps = [], []

    for stem, linga in vocab:                                 # matup / vatup
        if stem.endswith(("mat", "vat")) and len(stem) > 4:
            base = stem[:-3]
            if base in stems and len(base) >= 3:       # (a two-letter base like Ba is not a noun that took matup: Bavat is ḍavatu)
                e = {"stem": stem, "linga": linga, "source": "matup 5.2.94 (+ 8.2.9 / 8.2.10 vatva)",
                     "components": [{"kind": "prakriti", "upadesha": base},
                                    {"kind": "taddhita", "upadesha": "matu~p", "artha": "tadasyAstyasminniti"}]}
                r = _try(e)
                (gaps if "gap" in r else entries).append(r["gap"] if "gap" in r else r)

    seen = {(e["stem"], e["linga"]) for e in entries}
    for stem, base, src in CURATED_MATUP:
        if (stem, "pulliṅga") not in seen:
            r = _try({"stem": stem, "linga": "pulliṅga", "source": src,
                      "components": [{"kind": "prakriti", "upadesha": base}, {"kind": "taddhita", "upadesha": "matu~p", "artha": "tadasyAstyasminniti"}]})
            (gaps if "gap" in r else entries).append(r["gap"] if "gap" in r else r)

    for stem, base, src in CURATED:
        for linga in ("pulliṅga", "napuṃsaka"):
            if (stem, linga) in set(vocab) or (stem, linga) == (stem, "pulliṅga"):
                e = {"stem": stem, "linga": linga, "source": src,
                     "components": [{"kind": "prakriti", "upadesha": base},
                                    {"kind": "dhatu", "upadesha": "han", "dhatu_id": "02.0002"},
                                    {"kind": "krt", "upadesha": "kvip"}]}
                r = _try(e)
                (gaps if "gap" in r else entries).append(r["gap"] if "gap" in r else r)

    # tṛc: enumerate what the loop generates from every dhātu, then match listed stems *exactly*. A listed stem that merely ends in a
    # generated one (alaṅkartṛ = alam + kartṛ, utpatitṛ = ut + patitṛ) is a compound/upasarga stem: Phase 4 of AMENDMENT 22.
    rows = [r for r in iter_dhatu_entries() if r.get("dhatupatha_id") and r.get("upadesha_slp1")]
    gen: dict[str, list] = {}
    with ProcessPoolExecutor() as ex:
        for res in ex.map(_gen_job, rows, chunksize=8):
            if res:
                gen.setdefault(res[0], []).append(res)
    for stem, linga in vocab:
        if linga != "pulliṅga" or not stem.endswith(("tf", "wf")) or len(stem) <= 3:
            continue
        if stem in gen:
            _, dhid, up = sorted(gen[stem], key=lambda r: r[1])[0]
            entries.append({"stem": stem, "linga": linga, "source": "tṛc 3.1.133 — the stem is generated from the dhātu by the loop",
                            "components": [{"kind": "dhatu", "upadesha": up, "dhatu_id": dhid}, {"kind": "krt", "upadesha": "tfc"}]})
        else:
            tail = [g for g in gen if stem.endswith(g) and len(stem) - len(g) >= 2 and len(g) >= 4]
            why = f"= {stem[:-len(max(tail, key=len))]!r} + {max(tail, key=len)!r}: an upapada/upasarga compound (Phase 4)" if tail else "no dhātu generates it (kinship / 6.4.11-named stem, or a rule is missing)"
            gaps.append(f"{stem}: {why}")

    entries.sort(key=lambda e: (e["stem"], e["linga"]))
    print(f"{len(entries)} entries verified by generation; {len(gaps)} gaps (Art. 18 worklist):")
    for g in gaps[:60]:
        print("  gap:", g)
    if not a.dry_run:
        OUT.write_text(json.dumps({"_doc": "AMENDMENT 22 — Lexicon of stem vyutpatti. Written by tools/propose_vyutpatti.py; every entry reproduces its stem "
                                          "through engine.lexicon.compose. Lexical facts only (components); never a derived property.",
                                   "version": 1, "entries": entries}, ensure_ascii=False, indent=1), encoding="utf-8")
        print("wrote", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
