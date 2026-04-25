"""
tools/validate_engine_against_source.py
─────────────────────────────────────────

Runs the subanta pipeline for every cell of one or more gold corpus JSONs
under ``data/reference/subanta_gold/`` (and optionally checks tinanta gold),
reporting match / mismatch with the classical gold.

By default, **all** ``*.json`` files in those directories are used so new
paradigms are picked up without editing this tool.

Usage:
    python -m tools.validate_engine_against_source
    python -m tools.validate_engine_against_source --corpus path/to/one_gold.json
    python -m tools.validate_engine_against_source --subanta-only
    python -m tools.validate_engine_against_source --no-tinanta
"""
from __future__ import annotations

import argparse
import importlib
import json
import sys
from pathlib import Path
from typing import Any, List, Optional

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import sutras  # noqa: F401
from phonology.joiner  import slp1_to_devanagari
from pipelines.subanta import derive
from tools.gold_corpora import list_subanta_gold_jsons, list_tinanta_gold_jsons, subanta_gold_dir, tinanta_gold_dir


def _validate_subanta_file(path: Path) -> tuple[int, int, list]:
    with path.open(encoding="utf-8") as f:
        gold = json.load(f)
    stem = gold["stem_slp1"]
    linga = gold.get("linga", "pulliṅga")
    if "cells" not in gold:
        raise ValueError(f"{path}: not a subanta gold file (missing 'cells')")

    ok = fail = 0
    rows: list = []
    # Deterministic: sort cell keys
    for cell in sorted(gold["cells"], key=lambda k: (int(k.split("-")[0]), int(k.split("-")[1]))):
        data = gold["cells"][cell]
        v, vv = (int(x) for x in cell.split("-"))
        state = derive(stem, v, vv, linga=linga)
        produced = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
        expected = data["form_dev"]
        match = (produced == expected)
        rows.append((str(path.name), cell, produced, expected, match))
        if match:
            ok += 1
        else:
            fail += 1
    return ok, fail, rows


def _call_tinanta_recipe(recipe: str, recipe_args: Optional[List[Any]]) -> Any:
    if ":" not in recipe:
        raise ValueError(f"recipe {recipe!r} must be 'module:callable'")
    mod_name, fn_name = recipe.rsplit(":", 1)
    m = importlib.import_module(mod_name)
    fn = getattr(m, fn_name)
    if recipe_args is None:
        return fn()
    return fn(*tuple(recipe_args))


def _validate_tinanta_gold_file(path: Path) -> tuple[int, int, list]:
    with path.open(encoding="utf-8") as f:
        gold = json.load(f)
    target = (gold.get("surface_target_slp1") or "").strip()
    if not target:
        return 0, 0, []

    if isinstance(gold.get("recipe"), str):
        ra = gold.get("recipe_args")
        if ra is not None and not isinstance(ra, list):
            raise ValueError(f"{path}: recipe_args must be a JSON list or absent")
        s = _call_tinanta_recipe(gold["recipe"], ra)
    elif "steps" in gold:
        from pipelines.tinanta_jayati_gold import run_jayati_gold_through_step

        s = run_jayati_gold_through_step(9)
    else:
        return 0, 0, []

    trace = getattr(s, "trace", None)
    if trace is None:
        raise TypeError(f"{path}: recipe did not return a State-like object with .trace")

    got = s.flat_slp1()
    match = (got == target)
    if match:
        return 1, 0, [(path.name, "1-1", got, target, True)]
    return 0, 1, [(path.name, "1-1", got, target, False)]


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument(
        "--corpus",
        type=Path,
        default=None,
        help="single subanta or tinanta gold JSON; if set, only this file is used",
    )
    p.add_argument(
        "--subanta-dir",
        type=Path,
        default=None,
        help="override subanta_gold directory (default: data/reference/subanta_gold/)",
    )
    p.add_argument(
        "--subanta-only",
        action="store_true",
        help="only validate subanta_gold (skip tinanta)",
    )
    p.add_argument(
        "--no-tinanta",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    args = p.parse_args(argv)

    sub_dir = args.subanta_dir or subanta_gold_dir()
    all_ok = all_fail = 0
    all_rows: list = []
    if args.corpus is not None:
        paths = [args.corpus]
    else:
        paths = list_subanta_gold_jsons(sub_dir)
        if not paths:
            print(f"no subanta gold JSONs under {sub_dir}", file=sys.stderr)
            return 2

    for path in paths:
        try:
            ok, fail, rows = _validate_subanta_file(path)
        except ValueError as e:
            print(e, file=sys.stderr)
            return 2
        all_ok += ok
        all_fail += fail
        all_rows.extend(rows)
        print(f"  {path.name}: {ok} ok, {fail} fail  ({ok + fail} cells)")

    tin = args.subanta_only or args.no_tinanta
    if not args.corpus and not tin:
        tdir = tinanta_gold_dir()
        for tpath in list_tinanta_gold_jsons(tdir):
            ok, fail, rows = _validate_tinanta_gold_file(tpath)
            if not rows:  # skipped
                print(f"  {tpath.name}: skipped (non-jayati schema or empty)")
                continue
            all_ok += ok
            all_fail += fail
            all_rows.extend(rows)
            print(f"  {tpath.name} (tinanta): {ok} ok, {fail} fail")

    if not all_rows:
        return 0

    w1 = max(len(r[0]) for r in all_rows)
    w2 = max(len(r[1]) for r in all_rows)
    w3 = max(len(r[2]) for r in all_rows) if all_rows else 6
    w4 = max(len(r[3]) for r in all_rows) if all_rows else 6
    w3 = max(w3, 6)
    w4 = max(w4, 6)

    print()
    print(f"{'file':<{w1}}  {'cell':<{w2}}  {'produced':<{w3}}  {'gold':<{w4}}  match")
    print("-" * (w1 + w2 + w3 + w4 + 25))
    for name, cell, produced, expected, m in all_rows:
        mark = "✓" if m else "✗"
        print(f"{name:<{w1}}  {cell:<{w2}}  {produced:<{w3}}  {expected:<{w4}}  {mark}")

    print(f"\n{all_ok} / {all_ok + all_fail} checks match")
    return 0 if all_fail == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
