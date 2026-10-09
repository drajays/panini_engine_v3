"""tools/scan_stats.py — P0 baseline of the scheduler's scan cost (docs/PRAKARANA_MACHINE_PLAN.md).

    python3 -m tools.scan_stats [--write]   # registry records scanned / cond() calls per scheduler step
Observation only; P2 must keep every sweep identical while `scanned_per_step` drops.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace as NS

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
OUT = ROOT / "docs" / "ratchet_prakarana_p0.json"

CASES = [("BU", "laT", 1, 3), ("BU", "luG", 1, 3), ("gam", "liT", 1, 3), ("han", "laT", 1, 1)]


def main() -> dict:
    import sutras  # noqa: F401
    from engine.scheduler import SCAN_STATS
    from pipelines.tinanta import derive
    from tools.autonomy_report import run_autonomously, start_state
    rows = {}
    for root, lak, pur, vac in CASES:
        try:
            expect = derive(root, lak, "kartari", pur, vac).flat_slp1()
        except Exception as e:
            rows[f"{root}/{lak}/{pur}{vac}"] = {"error": type(e).__name__}
            continue
        for k in SCAN_STATS:
            SCAN_STATS[k] = 0
        run = run_autonomously(start_state(NS(kind="tinanta", args=(root, lak, pur, vac))), expect, root, 120)
        s = dict(SCAN_STATS)
        s["outcome"] = run.outcome
        from engine import prakarana
        fired = {t["sutra_id"] for t in run.state.trace if t.get("status") == "APPLIED"} if hasattr(run, "state") else set()
        mods = {m for f in fired for m in prakarana.of(f)}
        s["fired"], s["modules_touched"] = len(fired), sorted(mods)
        s["union_size"] = len({x for m in mods for x in prakarana.members(m)})  # P2 upper bound on scan, if blocks were exact
        s["scanned_per_step"] = round(s["scanned"] / max(s["steps"], 1), 1)
        rows[f"{root}/{lak}/{pur}{vac}"] = s
    return rows


if __name__ == "__main__":
    r = main()
    print(json.dumps(r, indent=1, ensure_ascii=False))
    if "--write" in sys.argv:
        OUT.write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n")
