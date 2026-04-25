#!/usr/bin/env python3
"""
Print *jayati* gold prakriyā: each engine step (1..9) with trace rows introduced in that
step only — **CONSTITUTION**: uses ``run_jayati_gold_through_step`` / ``sutras``; no
manual varṇa surgery.  The **post-step** ``flat_slp1`` checkpoint is printed **after**
the step’s slices (Issue 8) so the final string is not read before the rules that yield it.
"""
from __future__ import annotations

import argparse
import json
import sys
from io import StringIO
from pathlib import Path
from textwrap import indent
from typing import TextIO

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import sutras  # noqa: F401  — load SUTRA_REGISTRY

from engine.state import State, Term
from pipelines.tinanta_jayati_gold import run_jayati_gold_through_step, _gold_spec


def _term_tape_slp1(t: Term) -> str:
    """Current *varṇa* row for one ``Term`` (``flat_slp1`` = concat of these, in order)."""
    return "".join(v.slp1 for v in t.varnas)


def _print_post_step_checkpoint(out: TextIO, s: State) -> None:
    """
    *Post-step* string state — printed **after** this step’s trace slices so readers
    do not see the final ``flat_slp1`` (e.g. *jayati*) before the *vidhi* rows
    (Issue 8).
    """
    lex = [t.meta.get("upadesha_slp1") for t in s.terms]
    tape = [_term_tape_slp1(t) for t in s.terms]
    print("  ─── checkpoint  (POST-STEP — after all slices above)  ───", file=out)
    print(f"  flat_slp1()  =  {s.flat_slp1()!r}", file=out)
    print(f"  terms  (upadeśa, lexicon / pre-lopa name):  {lex!r}", file=out)
    print(f"  terms  (varṇa tape, current / post-lopa):   {tape!r}", file=out)


def _row(e: dict) -> str:
    """Single trace row — full JSON for audit."""
    d = {k: v for k, v in e.items() if not k.startswith("_")}
    return json.dumps(d, ensure_ascii=False, indent=2)


def _print_derivation(out: TextIO, applied_only: bool = False) -> State:
    spec = _gold_spec()
    steps = spec.get("steps") or []
    titles = {s.get("step", i + 1): s.get("title_hi", f"Step {i+1}") for i, s in enumerate(steps)}

    prev: list | None = None
    s_final = None
    for n in range(1, 10):
        s = run_jayati_gold_through_step(n)
        s_final = s
        cur = s.trace
        if prev is None:
            new_entries = list(cur)
        else:
            new_entries = cur[len(prev) :]
        prev = list(cur)

        title = titles.get(n) or f"Step {n}"
        print(file=out)
        print("-" * 72, file=out)
        print(f"  चरण (STEP) {n}:  {title}", file=out)
        print("-" * 72, file=out)
        if not new_entries:
            print("  (no new trace rows this step — should not happen)", file=out)
            _print_post_step_checkpoint(out, s)
            continue
        print(
            "  (slices: engine order for this step, top → bottom; "
            "post-step checkpoint follows.)",
            file=out,
        )
        shown = 0
        for j, e in enumerate(new_entries, 1):
            if applied_only and (e.get("status") or "").upper() == "SKIPPED":
                continue
            shown += 1
            if e.get("sutra_id") == "__PHASE__":
                print(
                    f"  … [{j}]  STRUCTURAL  {e.get('type_label', '')}  {e.get('status')}",
                    file=out,
                )
                print(indent(f"{e!r}", "     "), file=out)
                continue
            print(f"  ——— trace slice {j}/{len(new_entries)} ———", file=out)
            print(indent(_row(e), "  "), file=out)
        if applied_only and shown == 0 and new_entries:
            print("  (all entries SKIPPED in this step — re-run without --applied-only for full log)", file=out)
        _print_post_step_checkpoint(out, s)
    if s_final is None:
        raise RuntimeError("run_jayati_gold_through_step not executed")
    return s_final


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Print jayati gold prakriyā: trace rows per engine step (1..9). "
        "Uses run_jayati_gold_through_step only; no manual state surgery.",
    )
    ap.add_argument(
        "--applied-only",
        action="store_true",
        help="Omit trace rows with status=SKIPPED (shorter; full audit uses default).",
    )
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        metavar="FILE",
        help="Also write the same text to FILE (UTF-8).",
    )
    args = ap.parse_args()

    buf = StringIO()
    print("=" * 72, file=buf)
    print("  जयति — gold derivation (pānini_engine_v3) — sūtra trace by step (1..9)", file=buf)
    print("  Source: run_jayati_gold_through_step(n); Constitution: engine.dispatcher.apply_rule", file=buf)
    print("=" * 72, file=buf)

    s_final = _print_derivation(buf, applied_only=args.applied_only)
    print(file=buf)
    print("=" * 72, file=buf)
    print("  FINAL STATE (after step 9)", file=buf)
    print("=" * 72, file=buf)
    print(f"  flat_slp1:     {s_final.flat_slp1()!r}", file=buf)
    print(
        f"  upadeśa (lex): {[t.meta.get('upadesha_slp1') for t in s_final.terms]!r}",
        file=buf,
    )
    print(
        f"  varṇa tape:     {[_term_tape_slp1(t) for t in s_final.terms]!r}",
        file=buf,
    )
    print(f"  tripadi_zone:  {s_final.tripadi_zone}", file=buf)
    print(f"  phase:         {s_final.phase!r}", file=buf)
    adh = [e.get("id") for e in s_final.adhikara_stack]
    print(f"  adhikara_stack (ids, order):  {adh}", file=buf)
    print(f"  total trace rows:  {len(s_final.trace)}", file=buf)
    print("=" * 72, file=buf)

    text = buf.getvalue()
    print(text, end="")
    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
