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

INVOKED: set[str] = set()
MOVED: set[str] = set()


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
        return result

    dispatcher.apply_rule = recording_apply_rule
    engine.apply_rule = recording_apply_rule


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
    print(
        f"\n[firing_coverage] invoked={payload['counts']['invoked']} "
        f"moved={payload['counts']['moved']} → {LEDGER_PATH.relative_to(_ROOT)}"
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
