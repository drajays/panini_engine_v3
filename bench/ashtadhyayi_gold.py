"""
bench/ashtadhyayi_gold.py — the whole engine against ashtadhyayi.com's tiṅanta tables.

Gold: dhatu/dhatuforms_vidyut_shuddha_{kartari,karmani}.txt (every root × 10
lakāras × 9 cells; kartari in the root's padas, karmaṇi in ātmanepada), fetched
at a pinned commit by ``tools.fetch_ashtadhyayi_data``. Data © ashtadhyayi.com.

A cell agrees when our Devanāgarī form is one of the table's alternatives.
The engine is only *tested* here — nothing in the rule path reads this file
(tests/constitutional/test_engine_is_rule_based.py).

    python3 -m bench.ashtadhyayi_gold                  # all roots (parallel)
    python3 -m bench.ashtadhyayi_gold --sample 200     # a random slice
    python3 -m bench.ashtadhyayi_gold --lakara laT --prayoga karmani
    python3 -m bench.ashtadhyayi_gold --kind subanta   # shabda/data2.txt: 9,007 nouns × 24
    python3 -m bench.ashtadhyayi_gold --kind prakriya  # shabdaprakriya.txt: sūtra paths
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tools.fetch_ashtadhyayi_data import path as ref_path  # noqa: E402

REPORT = _ROOT / "bench" / "report" / "ashtadhyayi_gold.json"
SUB_REPORT = _ROOT / "bench" / "report" / "ashtadhyayi_gold_subanta.json"
PATH_REPORT = _ROOT / "bench" / "report" / "ashtadhyayi_gold_prakriya.json"
LINGA = {"P": "pulliṅga", "S": "strīliṅga", "N": "napuṃsaka"}
SUB_CELLS = [(vi, va) for vi in (1, 2, 3, 4, 5, 6, 7, 8) for va in (1, 2, 3)]   # 8 = sambodhana
LAKARA = {"lat": "laT", "lit": "liT", "lut": "luT", "lrut": "lRT", "lot": "loT", "lang": "laG",
          "vidhiling": "liG", "ashirling": "AsIrliG", "lung": "luG", "lrung": "lRG"}
CELLS = [(3, 1), (3, 2), (3, 3), (2, 1), (2, 2), (2, 3), (1, 1), (1, 2), (1, 3)]


def gold_jobs(prayogas: set[str], lakaras: set[str] | None, sample: int | None, seed: int):
    """(dhātu id, prayoga, pada, engine lakāra, [9 alternative-sets])."""
    tables = {"kartari": json.loads(ref_path("dhatu/dhatuforms_vidyut_shuddha_kartari.txt").read_text()),
              "karmani": json.loads(ref_path("dhatu/dhatuforms_vidyut_shuddha_karmani.txt").read_text())}
    ids = sorted(set(tables["kartari"]) | set(tables["karmani"]))
    if sample:
        ids = random.Random(seed).sample(ids, min(sample, len(ids)))
    for did in ids:
        for prayoga in sorted(prayogas):
            for key, cells in (tables[prayoga].get(did) or {}).items():
                pada = {"p": "parasmai", "a": "atmane"}[key[0]]
                lak = LAKARA.get(key[1:])
                if lak is None or (lakaras and lak not in lakaras):
                    continue
                alts = [set(c.split(",")) for c in cells.split(";")]
                if len(alts) == 9:
                    yield did, prayoga, pada, lak, alts


def _run(job):
    did, prayoga, pada, lak, alts = job
    from pipelines.tinanta import derive
    out = []
    for (pu, va), gold in zip(CELLS, alts):
        try:
            kw = {"pada": pada} if prayoga == "kartari" else {}
            ours = derive(did, lak, prayoga, pu, va, **kw).flat_dev()
            out.append(("agree" if ours in gold else "differ", ours))
        except Exception as ex:                      # a gap, not a crash of the bench
            out.append(("error", f"{type(ex).__name__}"))
    return did, prayoga, pada, lak, out, [sorted(g) for g in alts]


def subanta_jobs(sample: int | None, seed: int):
    """(stem SLP1, liṅga, [24 alternative-sets]) — sambodhana without its हे."""
    from phonology.tokenizer import devanagari_to_slp1_flat
    rows = [r for r in json.loads(ref_path("shabda/data2.txt").read_text())["data"]
            if r.get("linga") in LINGA and r.get("forms")]
    if sample:
        rows = random.Random(seed).sample(rows, min(sample, len(rows)))
    for r in rows:
        cells = r["forms"].split(";")
        if len(cells) != 24:
            continue
        try:
            stem = devanagari_to_slp1_flat(r["word"])
        except Exception:
            continue
        yield stem, LINGA[r["linga"]], [{a.removeprefix("हे ").strip() for a in c.split("-")} for c in cells]


def _run_sub(job):
    stem, linga, alts = job
    from pipelines.subanta import derive
    out = []
    for (vi, va), gold in zip(SUB_CELLS, alts):
        if gold <= {""}:                     # no such form (e.g. a plural-only noun)
            out.append(("absent", ""))
            continue
        try:
            ours = derive(stem, vi, va, linga=linga).flat_dev()
            out.append(("agree" if ours in gold else "differ", ours))
        except Exception as ex:
            out.append(("error", type(ex).__name__))
    return stem, linga, out, [sorted(g) for g in alts]


def main_subanta(a) -> int:
    by, words, examples = Counter(), Counter(), []
    per_linga = defaultdict(Counter)
    with ProcessPoolExecutor(max_workers=a.workers) as ex:
        for stem, linga, out, gold in ex.map(_run_sub, subanta_jobs(a.sample, a.seed), chunksize=16):
            st = Counter(x for x, _ in out)
            by.update(st - Counter({"absent": st["absent"]})); per_linga[linga].update(st)
            words["full paradigm" if st["agree"] + st["absent"] == 24 else "some error" if st["error"] else "partial"] += 1
            for (status, ours), (vi, va), g in zip(out, SUB_CELLS, gold):
                if status == "differ" and len(examples) < 40:
                    examples.append([stem, linga, f"{vi}/{va}", ours, g])
    n = sum(by.values())
    summary = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "sample": a.sample, "cells": n, **by, "agree_pct": round(100 * by["agree"] / max(n, 1), 1),
               "words": dict(words), "by_linga": {k: dict(v) for k, v in per_linga.items()},
               "examples": examples}
    print(f"ashtadhyayi.com subanta gold — {n} cells: agree {by['agree']} ({summary['agree_pct']} %), "
          f"differ {by['differ']}, error {by['error']}; words {dict(words)}")
    if not a.sample:
        SUB_REPORT.write_text(json.dumps(summary, ensure_ascii=False, indent=1) + "\n")
        print(f"→ {SUB_REPORT.relative_to(_ROOT)}")
    return 0


def _norm_index(ix: str) -> str:
    return ".".join(str(int(x)) for x in ix.split("."))


def prakriya_jobs(sample: int | None, seed: int):
    """(stem SLP1, liṅga, vibhakti, vacana, gold form, gold sūtra set) — liṅga via data2."""
    from phonology.tokenizer import devanagari_to_slp1_flat
    linga = {_norm_index(r["zbaseindex"]): LINGA.get(r.get("linga"))
             for r in json.loads(ref_path("shabda/data2.txt").read_text())["data"] if r.get("zbaseindex")}
    rows = json.loads(ref_path("shabda/shabdaprakriya.txt").read_text())["data"]
    if sample:
        rows = random.Random(seed).sample(rows, min(sample, len(rows)))
    for r in rows:
        lg = linga.get(_norm_index(r["baseindex"]))
        try:
            stem = devanagari_to_slp1_flat(r["word"])
        except Exception:
            continue
        if lg:
            yield (stem, lg, int(r["vibhakti"]), int(r["vachan"]), r["form"].removeprefix("हे ").strip(),
                   sorted({x for st in r["steps"] for x in st["sutras"]}))


def _run_path(job):
    stem, linga, vi, va, form, theirs = job
    from pipelines.subanta import derive
    try:
        st = derive(stem, vi, va, linga=linga)
    except Exception as ex:
        return job, "error", type(ex).__name__, []
    ours = sorted({r.get("sutra_id") for r in st.trace
                   if (r.get("status") or "").upper().startswith("APPLIED") and r.get("sutra_id")})
    return job, ("agree" if st.flat_dev() == form else "differ"), st.flat_dev(), ours


def main_prakriya(a) -> int:
    status, missed, extra, hits, tot = Counter(), Counter(), Counter(), 0, 0
    examples = defaultdict(list)
    with ProcessPoolExecutor(max_workers=a.workers) as ex:
        for job, stt, ours_form, ours in ex.map(_run_path, prakriya_jobs(a.sample, a.seed), chunksize=16):
            status[stt] += 1
            if stt != "agree":
                continue                       # a path is only comparable on a matching surface
            theirs, mine = set(job[5]), set(ours)
            hits += len(theirs & mine); tot += len(theirs)
            for x in theirs - mine:
                missed[x] += 1
                if len(examples[x]) < 4:
                    examples[x].append(f"{job[0]} {job[1]} {job[2]}/{job[3]} {job[4]}")
    recall = round(100 * hits / max(tot, 1), 1)
    summary = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "sample": a.sample, "forms": dict(status), "sutra_recall_pct": recall,
               "note": "share of ashtadhyayi.com's sūtras (on forms we derive identically) that our trace also applies",
               "most_missed": [{"sutra": k, "forms": n, "examples": examples[k]} for k, n in missed.most_common(40)]}
    print(f"ashtadhyayi.com prakriyā paths — forms {dict(status)}; sūtra recall on agreeing forms {recall} %")
    for r in summary["most_missed"][:15]:
        print(f"  {r['sutra']:9} missed on {r['forms']:4} forms  e.g. {r['examples'][0]}")
    if not a.sample:
        PATH_REPORT.write_text(json.dumps(summary, ensure_ascii=False, indent=1) + "\n")
        print(f"→ {PATH_REPORT.relative_to(_ROOT)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--lakara", action="append")
    ap.add_argument("--prayoga", action="append", choices=["kartari", "karmani"])
    ap.add_argument("--workers", type=int, default=os.cpu_count())
    ap.add_argument("--dump", type=Path, help="write every non-agreeing cell as JSONL")
    ap.add_argument("--kind", choices=["tinanta", "subanta", "prakriya"], default="tinanta")
    a = ap.parse_args(argv)
    if a.kind == "subanta":
        return main_subanta(a)
    if a.kind == "prakriya":
        return main_prakriya(a)
    jobs = list(gold_jobs(set(a.prayoga or ["kartari", "karmani"]), set(a.lakara or []) or None,
                          a.sample, a.seed))
    by = defaultdict(Counter)
    examples = defaultdict(list)
    dump = a.dump.open("w") if a.dump else None
    with ProcessPoolExecutor(max_workers=a.workers) as ex:
        for did, prayoga, pada, lak, out, gold in ex.map(_run, jobs, chunksize=8):
            for (status, ours), (pu, va), g in zip(out, CELLS, gold):
                by[(prayoga, lak)][status] += 1
                if status != "agree" and len(examples[(prayoga, lak)]) < 12:
                    examples[(prayoga, lak)].append([did, pada, f"{pu}/{va}", ours, g])
                if status != "agree" and dump:
                    dump.write(json.dumps([did, prayoga, pada, lak, pu, va, status, ours, g],
                                          ensure_ascii=False) + "\n")
    rows = []
    tot = Counter()
    for (prayoga, lak), c in sorted(by.items()):
        n = sum(c.values()); tot.update(c)
        rows.append({"prayoga": prayoga, "lakara": lak, "cells": n, **c,
                     "agree_pct": round(100 * c["agree"] / n, 1)})
    n = sum(tot.values())
    summary = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "source": json.loads(ref_path("SOURCE.json").read_text()) if ref_path("SOURCE.json").exists() else {},
               "sample": a.sample, "cells": n, **tot,
               "agree_pct": round(100 * tot["agree"] / max(n, 1), 1), "by": rows,
               "examples": {f"{k[0]}:{k[1]}": v for k, v in examples.items()}}
    print(f"ashtadhyayi.com gold — {n} cells: agree {tot['agree']} ({summary['agree_pct']} %), "
          f"differ {tot['differ']}, error {tot['error']}")
    for r in rows:
        print(f"  {r['prayoga']:8} {r['lakara']:8} {r['agree_pct']:5} %  ({r['cells']})")
    if not a.sample and not a.lakara and not a.prayoga:
        REPORT.write_text(json.dumps(summary, ensure_ascii=False, indent=1) + "\n")
        print(f"→ {REPORT.relative_to(_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
