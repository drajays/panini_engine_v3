"""
tests/regression/test_sig_baseline.py
───────────────────────────────────────

SIG baseline regression oracle (v3.1 amendment).

For every rāma paradigm cell, the set of APPLIED sūtras must match the
baseline.  If the engine produces the correct surface form via a
DIFFERENT sūtra path than the baseline, this is flagged as a regression
even though surface-equality tests would pass.

The baseline is stored as part of the repo at tests/regression/sig_applied_paths_baseline.json
When a cell's path legitimately changes (because a new sūtra was added
and the derivation genuinely took a new route), update the baseline
file via:  pytest tests/regression/test_sig_baseline.py --update-baseline

This is exactly the truth-teller v2's SIG provided — surface-correct
but path-wrong is a silent regression.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from engine.sig        import extract_applied_path
from pipelines.subanta import derive


_BASELINE_PATH = Path(__file__).parent / "sig_applied_paths_baseline.json"

_CELLS = [(v, vv) for v in range(1, 9) for vv in range(1, 4)]


def _load_baseline():
    if not _BASELINE_PATH.exists():
        return {}
    return json.loads(_BASELINE_PATH.read_text(encoding="utf-8"))


def _save_baseline(paths):
    _BASELINE_PATH.write_text(
        json.dumps(paths, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def pytest_addoption(parser):
    # Hook only works if this module is loaded as a conftest; for a test
    # module, users drive updates via `python -m tools.sig_benchmark --freeze`
    # instead.  Kept here for doc purposes.
    pass


@pytest.mark.parametrize("v,vv", _CELLS)
def test_applied_path_matches_baseline(v, vv):
    baseline = _load_baseline()
    cell = f"{v}-{vv}"

    state = derive("rAma", v, vv)
    current_path = extract_applied_path(state.trace)

    if cell not in baseline:
        # First-time run — establish the baseline for this cell.
        pytest.skip(
            f"no baseline for cell {cell}; run 'python -m tools.sig_benchmark "
            f"--freeze' then commit the generated sig_applied_paths_baseline.json"
        )

    expected = baseline[cell]["applied_path"]
    assert current_path == expected, (
        f"SIG PATH REGRESSION on cell {cell}:\n"
        f"  baseline : {expected}\n"
        f"  current  : {current_path}\n"
        f"Surface equality may still pass, but the derivation path changed. "
        f"If this change is intentional, update the baseline via "
        f"'python -m tools.sig_benchmark --freeze'."
    )
