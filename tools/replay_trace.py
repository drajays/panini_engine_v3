"""
tools/replay_trace.py
──────────────────────

CLI: replay a saved trace JSON and print the reconstructed derivation.

Usage:
    python -m tools.replay_trace path/to/trace.json

The trace file is a list of TraceStep dicts (as produced by
engine.trace).  Fired steps (APPLIED, APPLIED_VACUOUS, AUDIT) are
re-applied; other rows are printed as context.  The initial state
is re-built from the trace's first step's form_before (crude
reverse-tokenization via phonology.tokenizer — good enough for inspection).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Ensure repo root on sys.path when run as a script.
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import sutras  # noqa: F401
from engine            import apply_rule
from engine.state      import State, Term
from phonology.tokenizer import devanagari_to_varnas


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("trace_json", type=Path)
    p.add_argument("--no-merge", action="store_true",
                   help="Skip __MERGE__ structural step during replay.")
    args = p.parse_args(argv)

    with args.trace_json.open(encoding="utf-8") as f:
        trace = json.load(f)

    if not trace:
        print("empty trace", file=sys.stderr)
        return 1

    # Reconstruct initial state from form_before of step 0.
    first_before = trace[0]["form_before"]
    varnas = devanagari_to_varnas(first_before)
    state = State(terms=[Term(kind="pada", varnas=varnas, tags={"upadesha"})])

    from engine.trace import TRACE_STATUSES_FIRED

    for step in trace:
        sid = step["sutra_id"]
        status = step.get("status", "APPLIED")
        if sid.startswith("__"):
            print(f"  [structural] {sid} :: {step.get('why_dev','')}")
            continue
        if status not in TRACE_STATUSES_FIRED:
            print(f"  [skipped  ] {sid} ({status}) :: {step.get('why_dev','')}")
            continue
        state = apply_rule(sid, state)
        tag = "fired" if status == "AUDIT" else "applied"
        print(f"  [{tag:7}] {sid} :: {state.render()}")

    print(f"\nFinal: {state.render()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
