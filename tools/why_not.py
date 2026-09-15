"""
tools/why_not.py — why did this sūtra fire, or not fire, here?
──────────────────────────────────────────────────────────────

Article 15 asks every conflict to be declared rather than engineered. To
declare one you first have to see it, and reading 126 trace steps by hand to
find out who beat whom is how the 6.1.102 defect survived for months.

    python3 -m tools.why_not 6.1.102 --subanta rAma 1 2
    python3 -m tools.why_not 6.1.77  --subanta nadI 1 2 --linga strīliṅga
    python3 -m tools.why_not 7.3.77  --tinanta gam laT 3 1

For the named sūtra it reports, in this derivation: whether it was scheduled
at all, what happened at each appearance, the reason it declined, and — when
it was blocked — which प्रतिषेध declared the block and whether that rule fired.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

STATUS_NOTE = {
    "APPLIED": "fired and changed the tape",
    "APPLIED_VACUOUS": "fired; the form was already what it wanted",
    "BLOCKED": "was scheduled, but another sūtra had forbidden it",
    "SKIPPED": "was scheduled; its own condition was false",
    "AUDIT": "adhikāra / anuvāda — recorded, not an operation",
}


def _blockers(sutra_id: str) -> list[tuple[str, str]]:
    """Rules that declare a block on this sūtra."""
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY

    return [
        (sid, rec.text_dev or "")
        for sid, rec in SUTRA_REGISTRY.items()
        if sutra_id in tuple(getattr(rec, "blocks_sutra_ids", ()) or ())
    ]


def explain(state: Any, sutra_id: str) -> None:
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY

    rec = SUTRA_REGISTRY.get(sutra_id)
    trace = list(state.trace)
    print(f"\n  surface : {state.flat_dev()}   ({state.flat_slp1()})")
    print(f"  sūtra   : {sutra_id}  {getattr(rec, 'text_dev', '') or '(not registered)'}"
          f"   [{rec.sutra_type.name if rec else '—'}]")

    hits = [(i, s) for i, s in enumerate(trace) if s.get("sutra_id") == sutra_id]
    if not hits:
        print("\n  NEVER SCHEDULED in this derivation — the pipeline's rule list "
              "does not contain it, so its condition was never even asked.")
    for i, step in hits:
        status = step.get("status", "?")
        print(f"\n  step {i + 1:>3}  {status}  — {STATUS_NOTE.get(status, '')}")
        print(f"      form   {step.get('form_before')} → {step.get('form_after')}")
        if step.get("skip_reason"):
            print(f"      reason {step['skip_reason']}")
        if step.get("why_now_dev"):
            print(f"      why    {step['why_now_dev']}")
        for j in (i - 1, i + 1):
            if 0 <= j < len(trace):
                n = trace[j]
                where = "before" if j < i else "after "
                print(f"      {where} {n.get('sutra_id')} {n.get('status')}")

    blocked_now = sutra_id in getattr(state, "blocked_sutras", set())
    declared = _blockers(sutra_id)
    if declared or blocked_now:
        print("\n  who forbade it")
        if not declared:
            print("      nothing declares a block — it is in state.blocked_sutras "
                  "without a प्रतिषेध, which Art. 15 does not allow")
        for sid, text in declared:
            fired = any(
                s.get("sutra_id") == sid and s.get("status", "").startswith("APPLIED")
                for s in trace
            )
            mark = "fired here" if fired else "did not fire here"
            print(f"      {sid}  {text}  — {mark}")
        print(f"      state.blocked_sutras contains it: {blocked_now}")
    elif hits:
        print("\n  no sūtra declares a block on this one.")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Explain a sūtra's fate in one derivation.")
    ap.add_argument("sutra_id")
    ap.add_argument("--subanta", nargs=3, metavar=("STEM", "VIBHAKTI", "VACANA"))
    ap.add_argument("--linga", default="pulliṅga")
    ap.add_argument("--tinanta", nargs=4, metavar=("DHATU", "LAKARA", "PURUSHA", "VACANA"))
    args = ap.parse_args(argv)

    import sutras  # noqa: F401
    if args.subanta:
        from pipelines.subanta import derive
        stem, vibhakti, vacana = args.subanta
        state = derive(stem, int(vibhakti), int(vacana), linga=args.linga)
    elif args.tinanta:
        from pipelines.tinanta import derive as tin_derive
        dhatu, lakara, purusha, vacana = args.tinanta
        state = tin_derive(dhatu, lakara, "kartari", int(purusha), int(vacana))
    else:
        ap.error("give --subanta or --tinanta")
    explain(state, args.sutra_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
