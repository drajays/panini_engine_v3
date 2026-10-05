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


from engine.scheduler import effective_candidates  # noqa: E402,F401  (C2 moved it into the engine)


def run_autonomously(state: Any, expected: str, case: str, budget: int) -> Run:
    from engine import apply_rule
    from engine.resolver import resolve_with_reason
    from engine.core_loop import apply_pratishedhas, note_tripadi_progress, open_adhikaras
    from engine.scheduler import enumerate_candidates, operational_paribhasha_candidates

    result = Run(case=case, expected=expected)
    for _ in range(budget):
        open_adhikaras(state)
        state = apply_pratishedhas(state)
        candidates = enumerate_candidates(state) + operational_paribhasha_candidates(state)
        usable = effective_candidates(candidates, state)
        result.offered, result.effective = len(candidates), len(usable)
        if not usable:
            from engine.core_loop import advance_phase

            if advance_phase(state):     # this stratum is exhausted — Art. 3 moves on
                continue
            result.outcome = "halted"
            result.blocked_at = state.flat_slp1()
            break
        decision = resolve_with_reason(usable, state)
        before = state.flat_slp1()
        state = apply_rule(decision.winner, state)
        note_tripadi_progress(state, decision.winner)
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

    if case.kind == "tinanta":
        return _tinanta_start(case)
    from pipelines.subanta import build_initial_state, run_subanta_preflight_through_1_4_7

    stem, vibhakti, vacana, linga = case.args
    state = build_initial_state(stem, vibhakti, vacana, linga)
    state = run_subanta_preflight_through_1_4_7(state)
    return apply_rule("4.1.2", state)


# The lakāra vivakṣā: which attach sūtra the *meaning* selects. Only the lakāras whose attach sūtra
# really attaches (act appends the placeholder) are listed; the others join as their sūtras are written.
_LAKARA_ATTACH = {
    "laT": "3.2.123", "liT": "3.2.115", "luT": "3.3.15", "lRT": "3.3.13", "loT": "3.3.162",
    "laG": "3.2.111", "liG": "3.3.161", "AsIrliG": "3.3.173", "luG": "3.2.110", "lRG": "3.3.139",
}


def _tinanta_start(case: Any) -> Any:
    """The tape a recipe hands the loop for a bhvādi kartari verb: dhātu + the lakāra the meaning chose
    + the tiṅ that vivakṣā (puruṣa · vacana) selects. Everything after — it-lopa, the atideśa 3.4.85,
    3.4.113, the vikaraṇa, guṇa, sandhi — is the loop's."""
    import sutras  # noqa: F401
    from engine import apply_rule
    from pipelines.tinanta import (
        P00_lac_lat_attach, P00_parasmai_tin_adesha, P06a_pratyaya_adhikara_3_1_1_to_3,
        _bootstrap_tinanta_derivation, _dhatu_row_by_upadesha, _select_tin_adesha,
    )

    dhatu, lakara, purusha, vacana = case.args
    state, _gana, pada_key, _done = _bootstrap_tinanta_derivation(
        _dhatu_row_by_upadesha(dhatu), lakara, "kartari", purusha=purusha, vacana=vacana)
    if getattr(case, "pada", None) in ("parasmai", "atmane"):
        pada_key = case.pada            # an ubhayapadī root: the caller picks the pada (the vivakṣā), as for puruṣa and vacana
    if lakara == "laT":
        state = P00_lac_lat_attach(state)
    elif lakara in _LAKARA_ATTACH:
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        state = apply_rule(_LAKARA_ATTACH[lakara], state)
        # the lakāra's own it-letter (loṭ's ṭ, laṅ/luṅ/liṅ's ṅ) goes *before* 3.4.78 puts a tiṅ in its place, and
        # the ādeśa inherits that it-ness (1.1.56) — which is how a ṅit lakāra's tiṅ blocks guṇa (1.1.5)
        if lakara == "liT":                # ijādi gurumān (3.1.36): ām, liṭ luk (2.4.81), then kṛ + liṭ (3.1.40, anuprayoga)
            for sid in ("3.1.36", "2.4.81", "3.1.40"):
                state = apply_rule(sid, state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
    else:
        raise NotImplementedError(f"lakāra {lakara!r}: its attach sūtra does not attach on its own yet")
    state = P00_parasmai_tin_adesha(state, _select_tin_adesha(lakara, pada_key, purusha, vacana))
    if getattr(case, "ashis", False):      # the blessing sense (7.1.35): an input the caller proposes
        next(x for x in state.terms if "dhatu" in x.tags).tags.add("ashis")
    state.phase = "pratyaya"       # the stratum we are in: affixes are being attached (3.1–3.4)
    return state


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="How far does the loop get alone?")
    ap.add_argument("--case")
    ap.add_argument("--steps", type=int, default=MAX_STEPS)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args(argv)

    from tools.show_prakriya import CASES, derive

    cases = [c for c in CASES if c.kind in ("subanta", "tinanta")]
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
