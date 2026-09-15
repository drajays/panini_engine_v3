"""
tools/gaps_report.py — the Article 18 worklist.

Runs the benchmark grid under a gap probe and writes ``sig/gaps.json``:
every sūtra that wanted to fire and was never asked, every datum the engine
was refused for want of, and every cell an independent implementation
disagrees about — ranked by how often each shows up.

    python3 -m tools.gaps_report                  # full grid (slow, thorough)
    python3 -m tools.gaps_report --limit 60       # a sample
    python3 -m tools.gaps_report --no-oracle      # skip bench disagreements

The probe patches the dispatcher before any pipeline is imported, so nothing
in this file may import ``pipelines`` at module level.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

OUT_PATH = _ROOT / "sig" / "gaps.json"
BENCH_REPORT_DIR = _ROOT / "bench" / "report"

_LINGA = {"pum": "pulliṅga", "stri": "strīliṅga", "napumsaka": "napuṃsaka"}


def collect(limit: int | None, use_oracle: bool) -> dict[str, Any]:
    import sutras  # noqa: F401 — fills SUTRA_REGISTRY
    from bench.grids import all_cells
    from engine.gaps import Gap, GapProbe, gap_from_exception, oracle_gaps, rank

    cells = all_cells()
    if limit:
        cells = cells[:limit]

    gaps: list[Gap] = []
    derived = failed = 0
    with GapProbe() as probe:
        from pipelines.subanta import derive as sub_derive
        from pipelines.tinanta import derive as tin_derive

        for cell in cells:
            probe.reset()
            where = cell["key"]
            try:
                if cell["kind"] == "subanta":
                    sub_derive(cell["stem"], cell["vibhakti"], cell["vacana"],
                               linga=_LINGA[cell["linga"]])
                else:
                    tin_derive(cell["dhatu"], cell["lakara"], "kartari",
                               cell["purusha"], cell["vacana"])
                derived += 1
            except Exception as ex:
                failed += 1
                gap = gap_from_exception(ex, where)
                if gap:
                    gaps.append(gap)
                continue
            gaps.extend(probe.gaps(where))

    if use_oracle:
        reports = sorted(BENCH_REPORT_DIR.glob("*.json"))
        if reports:
            report = json.loads(reports[-1].read_text(encoding="utf-8"))
            gaps.extend(oracle_gaps(report))

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "cells": len(cells),
        "derived": derived,
        "refused": failed,
        "gaps": len(gaps),
        "worklist": rank(gaps),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Article 18 gap worklist.")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--no-oracle", action="store_true")
    ap.add_argument("--top", type=int, default=15)
    args = ap.parse_args(argv)

    result = collect(args.limit, not args.no_oracle)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n  gaps — CONSTITUTION Art. 18")
    print(f"  cells    : {result['cells']}   derived {result['derived']} · "
          f"refused {result['refused']}")
    print(f"  gaps     : {result['gaps']}")
    by_kind: dict[str, int] = {}
    for item in result["worklist"]:
        by_kind[item["kind"]] = by_kind.get(item["kind"], 0) + item["count"]
    print(f"  by kind  : {by_kind}")
    print("\n  worklist (most frequent first)")
    for item in result["worklist"][: args.top]:
        print(f"    {item['count']:>4}  {item['kind']:<20} {item['subject']}")
        print(f"          {item['detail'][:96]}")
    print(f"\n  written: {OUT_PATH.relative_to(_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
