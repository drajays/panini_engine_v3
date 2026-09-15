"""
bench/run.py — the report card (CONSTITUTION Art. 19).

Runs this engine over the grids in ``bench/grids.py``, compares each surface
against the committed Vidyut oracle, and writes a dated report. Nothing here
imports vidyut: the oracle is a CSV produced separately (see
``bench/oracle_vidyut.py``), so the comparison reproduces on a clean checkout
with no extra install.

    python3 -m bench.run                      # report card
    python3 -m bench.run --show-disagreements
    python3 -m bench.run --fail-under 0.60    # exit 1 below that agreement
    PANINI_ORACLE_PYTHON=.venv/bin/python3 python3 -m bench.run --refresh-oracle

A disagreement is a **work item, never a verdict**: the other implementation
may be wrong, and the investigation is the deliverable.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from bench.grids import all_cells  # noqa: E402

ORACLE_PATH = _ROOT / "bench" / "oracle" / "vidyut.csv"
REPORT_DIR = _ROOT / "bench" / "report"

_LINGA = {"pum": "pulliṅga", "stri": "strīliṅga", "napumsaka": "napuṃsaka"}


def our_form(cell: dict[str, Any]) -> tuple[str, str]:
    """(surface, error) from this engine."""
    import sutras  # noqa: F401
    try:
        if cell["kind"] == "subanta":
            from pipelines.subanta import derive
            state = derive(cell["stem"], cell["vibhakti"], cell["vacana"],
                           linga=_LINGA[cell["linga"]])
        else:
            from pipelines.tinanta import derive as tin_derive
            state = tin_derive(cell["dhatu"], cell["lakara"], "kartari",
                               cell["purusha"], cell["vacana"])
        return state.flat_slp1(), ""
    except Exception as ex:
        return "", f"{type(ex).__name__}: {ex}"


def load_oracle() -> dict[str, dict[str, str]]:
    if not ORACLE_PATH.exists():
        return {}
    with ORACLE_PATH.open(encoding="utf-8") as fp:
        return {row["key"]: row for row in csv.DictReader(fp)}


def refresh_oracle() -> None:
    python = os.environ.get("PANINI_ORACLE_PYTHON", ".venv/bin/python3")
    print(f"[bench] refreshing oracle with {python}")
    subprocess.run([python, "-m", "bench.oracle_vidyut"], cwd=_ROOT, check=True)


def run() -> dict[str, Any]:
    oracle = load_oracle()
    cells = all_cells()
    rows, agree, disagree, ours_missing, theirs_missing = [], 0, [], 0, 0

    for cell in cells:
        form, error = our_form(cell)
        ref = oracle.get(cell["key"], {})
        theirs = [f for f in (ref.get("forms") or "").split("|") if f]
        if not form:
            ours_missing += 1
        if not theirs:
            theirs_missing += 1
        verdict = "unmeasured"
        if form and theirs:
            verdict = "agree" if form in theirs else "disagree"
            if verdict == "agree":
                agree += 1
            else:
                disagree.append({"key": cell["key"], "ours": form,
                                 "theirs": theirs, "their_path": ref.get("path", "")})
        rows.append({"key": cell["key"], "ours": form, "error": error,
                     "theirs": theirs, "verdict": verdict})

    comparable = agree + len(disagree)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "oracle": "vidyut (MIT) via bench/oracle/vidyut.csv",
        "cells": len(cells),
        "we_derived": len(cells) - ours_missing,
        "oracle_derived": len(cells) - theirs_missing,
        "comparable": comparable,
        "agree": agree,
        "disagree": len(disagree),
        "agreement": round(agree / comparable, 4) if comparable else None,
        "disagreements": disagree,
        "rows": rows,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Differential report card.")
    ap.add_argument("--refresh-oracle", action="store_true")
    ap.add_argument("--show-disagreements", action="store_true")
    ap.add_argument("--fail-under", type=float, default=None)
    ap.add_argument("--write", action="store_true", help="save the report JSON")
    args = ap.parse_args(argv)

    if args.refresh_oracle:
        refresh_oracle()
    report = run()

    print("\n  bench — differential report card (Art. 19)")
    print(f"  oracle        : {report['oracle']}")
    print(f"  cells         : {report['cells']}")
    print(f"  we derived    : {report['we_derived']}")
    print(f"  oracle derived: {report['oracle_derived']}")
    print(f"  comparable    : {report['comparable']}")
    print(f"  agree         : {report['agree']}")
    print(f"  disagree      : {report['disagree']}")
    pct = report["agreement"]
    print(f"  AGREEMENT     : {pct:.1%}" if pct is not None else "  AGREEMENT     : —")

    if args.show_disagreements:
        print("\n  disagreements (work items, not verdicts)")
        for d in report["disagreements"][:40]:
            print(f"    {d['key']:<34} ours {d['ours']:<14} theirs {'|'.join(d['theirs'])}")

    if args.write:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        stamp = report["generated_at"][:10]
        path = REPORT_DIR / f"{stamp}.json"
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\n  written: {path.relative_to(_ROOT)}")

    if args.fail_under is not None and (pct is None or pct < args.fail_under):
        print(f"\n  ✗ agreement below {args.fail_under:.0%}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
