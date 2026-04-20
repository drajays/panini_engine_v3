"""
tools/validate_engine_against_source.py
─────────────────────────────────────────

Runs the subanta pipeline for every cell of a gold corpus JSON
(default: data/reference/subanta_gold/rama_pullinga.json) and reports
match / mismatch with the classical gold.

Usage:
    python -m tools.validate_engine_against_source
    python -m tools.validate_engine_against_source --corpus path/to/gold.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import sutras  # noqa: F401
from pipelines.subanta import derive
from phonology.joiner  import slp1_to_devanagari


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument(
        "--corpus",
        type=Path,
        default=_ROOT / "data" / "reference" / "subanta_gold" / "rama_pullinga.json",
    )
    args = p.parse_args(argv)

    with args.corpus.open(encoding="utf-8") as f:
        gold = json.load(f)

    stem_slp1 = gold["stem_slp1"]
    linga     = gold.get("linga", "pulliṅga")

    ok = fail = 0
    rows = []

    for cell, data in gold["cells"].items():
        v, vv = cell.split("-")
        state = derive(stem_slp1, int(v), int(vv), linga=linga)
        produced = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
        expected = data["form_dev"]
        match = (produced == expected)
        rows.append((cell, produced, expected, match))
        if match: ok += 1
        else:     fail += 1

    # Summary.
    w = max(len(r[1]) for r in rows) if rows else 10
    print(f"{'cell':<6} {'produced':<{w}}  {'gold':<{w}}  match")
    print("-" * (14 + 2 * w))
    for cell, produced, expected, match in rows:
        mark = "✓" if match else "✗"
        print(f"{cell:<6} {produced:<{w}}  {expected:<{w}}  {mark}")

    print(f"\n{ok} / {ok + fail} cells match")
    return 0 if fail == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
