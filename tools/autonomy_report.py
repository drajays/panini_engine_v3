"""
tools/autonomy_report.py — how far can the engine derive *without* a recipe?

Phase C's goal is that the scheduler and resolver choose the rules and
``derive()`` becomes a thin router. This tool measures the distance to that
goal on real cases, and says what blocks it.

It drives the loop itself — ``enumerate_candidates`` → ``resolve_with_reason``
→ ``apply_rule`` — rather than importing a pipeline's loop, so the numbers
describe the tracked engine and nothing else.

    python3 -m tools.autonomy_report                 # the certain prakriyās
    python3 -m tools.autonomy_report --case ramah --steps 30 --verbose

Three outcomes are distinguished, because they need different fixes:

``reached``    the loop produced the same surface as the recipe
``halted``     no candidate would change the tape — the rule the derivation
               needs next is not in the candidate pool at all
``diverged``   the loop kept firing without progress until the budget ran out
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

OUT_PATH = _ROOT / "sig" / "autonomy.json"
MAX_STEPS = 60


@dataclass
class Run:
    case: str
    expected: str
    outcome: str = "halted"
    surface: str = ""
    steps: list[tuple[str, str, str, str]] = field(default_factory=list)
    offered: int = 0
    effective: int = 0
    blocked_at: str = ""


def effective_candidates(candidates: list[str], state: Any) -> list[str]:
    """A candidate that would not change the tape is not a candidate.

    The registry holds ~2,400 records whose ``cond`` is permissive and whose
    ``act`` does nothing. Without this filter the loop fires them in descending
    sūtra order — *para* picks the latest id first — and burns its whole budget
    rewriting the same form.
    """
    from engine import apply_rule

    before = state.flat_slp1()
    keep = []
    for sutra_id in candidates:
        try:
            if apply_rule(sutra_id, state.clone()).flat_slp1() != before:
                keep.append(sutra_id)
        except Exception:
            continue
    return keep


def run_autonomously(state: Any, expected: str, case: str, budget: int) -> Run:
    from engine import apply_rule
    from engine.resolver import resolve_with_reason
    from engine.scheduler import enumerate_candidates

    result = Run(case=case, expected=expected)
    for _ in range(budget):
        candidates = enumerate_candidates(state)
        usable = effective_candidates(candidates, state)
        result.offered, result.effective = len(candidates), len(usable)
        if not usable:
            result.outcome = "halted"
            result.blocked_at = state.flat_slp1()
            break
        decision = resolve_with_reason(usable, state)
        before = state.flat_slp1()
        state = apply_rule(decision.winner, state)
        result.steps.append((decision.winner, before, state.flat_slp1(), decision.layer))
    else:
        result.outcome = "diverged"
    result.surface = state.flat_slp1()
    if result.surface == expected:
        result.outcome = "reached"
    return result


def start_state(case: Any) -> Any:
    """The tape a recipe would hand the loop: stem + affix, nothing resolved."""
    import sutras  # noqa: F401
    from engine import apply_rule

    if case.kind != "subanta":
        raise NotImplementedError("tiṅanta start states land with C2")
    from pipelines.subanta import build_initial_state, run_subanta_preflight_through_1_4_7

    stem, vibhakti, vacana, linga = case.args
    state = build_initial_state(stem, vibhakti, vacana, linga)
    state = run_subanta_preflight_through_1_4_7(state)
    return apply_rule("4.1.2", state)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="How far does the loop get alone?")
    ap.add_argument("--case")
    ap.add_argument("--steps", type=int, default=MAX_STEPS)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args(argv)

    from tools.show_prakriya import CASES, derive

    cases = [c for c in CASES if c.kind == "subanta"]
    if args.case:
        cases = [c for c in cases if c.key == args.case]
        if not cases:
            print(f"no subanta case named {args.case!r}")
            return 2

    runs = []
    for case in cases:
        expected = derive(case).flat_slp1()
        run = run_autonomously(start_state(case), expected, case.key, args.steps)
        runs.append(run)
        mark = {"reached": "✓", "halted": "·", "diverged": "✗"}[run.outcome]
        print(f"  {mark} {case.key:<10} {run.outcome:<9} {run.surface:<14}"
              f" expected {expected:<14} ({run.offered} offered → {run.effective} effective)")
        if args.verbose:
            for sutra_id, before, after, layer in run.steps:
                print(f"        {sutra_id:<9} {before:<14} → {after:<14} [{layer}]")

    counts: dict[str, int] = {}
    for run in runs:
        counts[run.outcome] = counts.get(run.outcome, 0) + 1
    print(f"\n  {counts}   of {len(runs)} subanta cases")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps({
        "cases": len(runs),
        "outcomes": counts,
        "runs": [{"case": r.case, "outcome": r.outcome, "surface": r.surface,
                  "expected": r.expected, "offered": r.offered,
                  "effective": r.effective, "steps": r.steps} for r in runs],
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  written: {OUT_PATH.relative_to(_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
