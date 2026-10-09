"""tools/stage_order.py — P1 shadow: the empirical order in which prakaraṇa modules first fire in a derivation.

    python3 -m tools.stage_order [--write]    # docs/ratchet_prakarana_stage_order.json
Observation only. For each derivation, modules are ranked by the step where one of their sūtras first APPLIED. A pair (A,B) with A
always first is a *candidate* stage edge for L2 (to be confirmed by a concept card, Art. 23); pairs seen both ways are loops/shared.
"""
from __future__ import annotations

import itertools
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from types import SimpleNamespace as NS

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
OUT = ROOT / "docs" / "ratchet_prakarana_stage_order.json"

LAK = ["laT", "liT", "luT", "lfT", "loT", "laG", "viDiliG", "ASIrliG", "luG", "lfG"]


def first_seen(state) -> dict[str, int]:
    from engine import prakarana
    seen: dict[str, int] = {}
    for i, t in enumerate(x for x in state.trace if x.get("status") == "APPLIED" and x.get("form_before") != x.get("form_after")):
        for m in prakarana.of(t["sutra_id"]):
            seen.setdefault(m, i)
    return seen


def main(roots_per_gana: int = 3) -> dict:
    import sutras  # noqa: F401
    from pipelines.dhatupatha import iter_dhatu_entries
    from pipelines.tinanta import derive
    from tools.autonomy_report import run_autonomously, start_state
    rows = defaultdict(list)
    for r in iter_dhatu_entries():
        rows[r.get("gana")].append(r.get("id") or r["upadesha_slp1"])
    runs, before, touched = 0, Counter(), Counter()
    for gana, roots in sorted(rows.items(), key=lambda kv: str(kv[0])):
        for root in roots[:roots_per_gana]:
            for lak in LAK:
                try:
                    expect = derive(root, lak, "kartari", 3, 1).flat_slp1()
                    run = run_autonomously(start_state(NS(kind="tinanta", args=(root, lak, 3, 1))), expect, root, 120)
                except Exception:
                    continue
                if run.outcome != "reached":
                    continue
                fs = first_seen(run.state)
                runs += 1
                touched.update(fs)
                for a, b in itertools.permutations(fs, 2):
                    if fs[a] < fs[b]:
                        before[(a, b)] += 1
    edges = sorted(((a, b, n) for (a, b), n in before.items() if not before.get((b, a))), key=lambda e: -e[2])
    mixed = sorted({tuple(sorted(k)) for k in before if before.get((k[1], k[0]))})
    return {"runs": runs, "modules_touched": dict(touched), "always_before": [list(e) for e in edges], "seen_both_ways": [list(m) for m in mixed]}


if __name__ == "__main__":
    r = main()
    print(r["runs"], "runs;", len(r["modules_touched"]), "modules;", len(r["always_before"]), "one-way pairs;", len(r["seen_both_ways"]), "two-way pairs")
    if "--write" in sys.argv:
        OUT.write_text(json.dumps(r, ensure_ascii=False, indent=0) + "\n")
