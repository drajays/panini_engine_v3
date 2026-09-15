"""
tools/firing_coverage.py — produce the Article 16 firing ledger.
────────────────────────────────────────────────────────────────

Conditions 1 and 2 of Art. 16 (*invoked*, *moves the state*) are facts about
execution, so they are measured by running the suite once with ``apply_rule``
wrapped, and written to ``sig/firing_coverage.json``::

    python3 -m tools.firing_coverage              # run the suite, write the ledger
    python3 -m tools.firing_coverage -k subanta   # any pytest args pass through

The wrapper is installed as a pytest plugin *before* collection, so pipelines
that bind ``apply_rule`` at import time still see it. Every firing route in the
engine reaches ``engine.dispatcher.apply_rule`` (Art. 7/11), so the ledger is
complete by construction.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

LEDGER_PATH = _ROOT / "sig" / "firing_coverage.json"
SUITE_SIG_PATH = _ROOT / "sig" / "suite_sig.json"

INVOKED: set[str] = set()
MOVED: set[str] = set()
# Suite-wide sūtra interaction graph: what fired, with what outcome, after what.
STATUS: dict[str, dict[str, int]] = {}
EDGES: dict[str, int] = {}


def _surface(state: Any) -> str | None:
    try:
        return state.flat_slp1()
    except Exception:
        return None


def install() -> None:
    """Wrap the dispatcher so every rule application is recorded."""
    import engine
    import engine.dispatcher as dispatcher

    original = dispatcher.apply_rule

    def recording_apply_rule(sutra_id: str, state: Any, *args: Any, **kwargs: Any) -> Any:
        before = _surface(state)
        result = original(sutra_id, state, *args, **kwargs)
        INVOKED.add(sutra_id)
        if _surface(result) != before:
            MOVED.add(sutra_id)
        _record_interaction(sutra_id, result)
        return result

    dispatcher.apply_rule = recording_apply_rule
    engine.apply_rule = recording_apply_rule


def _record_interaction(sutra_id: str, result: Any) -> None:
    """Outcome of this firing, and which sūtra it followed in the same derivation."""
    trace = getattr(result, "trace", None)
    if not trace:
        return
    last = trace[-1]
    if last.get("sutra_id") != sutra_id:      # the rule appended nothing of its own
        return
    bucket = STATUS.setdefault(sutra_id, {})
    status = last.get("status", "UNKNOWN")
    bucket[status] = bucket.get(status, 0) + 1
    if len(trace) >= 2:
        prev = trace[-2].get("sutra_id")
        if prev:
            key = f"{prev}>{sutra_id}"
            EDGES[key] = EDGES.get(key, 0) + 1


def write_suite_sig(path: Path = SUITE_SIG_PATH) -> dict[str, Any]:
    """The interaction graph as the *whole suite* exercises it.

    ``sig/`` also holds a curated, timed graph built from the gold corpora
    (``make sig``). This one is wider and untimed: every rule firing in every
    test, with its outcome and its predecessor. Art. 15's health shows up here
    directly — a grammar that settles conflicts by rule has BLOCKED rows.
    """
    totals: dict[str, int] = {}
    for bucket in STATUS.values():
        for status, n in bucket.items():
            totals[status] = totals.get(status, 0) + n
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "the full pytest suite via tools.firing_coverage",
        "totals": {
            "sutras_invoked": len(INVOKED),
            "sutras_moving": len(MOVED),
            "edges": len(EDGES),
            "status": totals,
        },
        "nodes": {
            sid: {
                "status": STATUS.get(sid, {}),
                "moves": sid in MOVED,
            }
            for sid in sorted(INVOKED)
        },
        "edges": dict(sorted(EDGES.items(), key=lambda kv: (-kv[1], kv[0]))),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload


def write_ledger(path: Path = LEDGER_PATH) -> dict[str, Any]:
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "invoked": sorted(INVOKED),
        "moved": sorted(MOVED),
        "counts": {"invoked": len(INVOKED), "moved": len(MOVED)},
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload


# ── pytest plugin hooks (used via `-p tools.firing_coverage`) ──────────────

def pytest_configure(config: Any) -> None:  # noqa: ARG001
    install()


def pytest_sessionfinish(session: Any, exitstatus: int) -> None:  # noqa: ARG001
    payload = write_ledger()
    sig = write_suite_sig()
    print(
        f"\n[firing_coverage] invoked={payload['counts']['invoked']} "
        f"moved={payload['counts']['moved']} → {LEDGER_PATH.relative_to(_ROOT)}"
        f"\n[suite_sig] edges={sig['totals']['edges']} "
        f"status={sig['totals']['status']} → {SUITE_SIG_PATH.relative_to(_ROOT)}"
    )


def print_report() -> int:
    """Print the Article 16 report from the committed ledger (no suite run)."""
    import sutras  # noqa: F401 — fills SUTRA_REGISTRY
    from engine import SUTRA_REGISTRY
    from engine.coverage import honest_coverage

    r = honest_coverage(SUTRA_REGISTRY)
    c = r["conditions"]
    print("Pāṇini engine — coverage (CONSTITUTION Art. 16)")
    print(f"  registered   : {r['registered']:>5}   records in SUTRA_REGISTRY")
    print(f"  implemented  : {r['implemented']:>5}   ({r['implemented_pct']} %)"
          "   invoked + moved + cited + tested")
    print(f"    invoked    : {c['invoked']:>5}")
    print(f"    moves state: {c['moved']:>5}")
    print(f"    cited      : {c['cited']:>5}   (Art. 14)")
    print(f"    tested      : {c['tested']:>5}")
    print(f"  worklist     : {len(r['moving_but_uncited']):>5}   move the tape but are not cited")
    print(f"  ledger       : {r['ledger']}  ({r['ledger_generated_at']})")
    return 0


def main(argv: list[str] | None = None) -> int:
    import pytest

    args = list(argv if argv is not None else sys.argv[1:])
    if "--report" in args:
        return print_report()
    return pytest.main([*args, "-p", "tools.firing_coverage", "-q"])


if __name__ == "__main__":
    raise SystemExit(main())
