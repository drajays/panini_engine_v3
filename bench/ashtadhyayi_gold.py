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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--lakara", action="append")
    ap.add_argument("--prayoga", action="append", choices=["kartari", "karmani"])
    ap.add_argument("--workers", type=int, default=os.cpu_count())
    ap.add_argument("--dump", type=Path, help="write every non-agreeing cell as JSONL")
    a = ap.parse_args(argv)
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
