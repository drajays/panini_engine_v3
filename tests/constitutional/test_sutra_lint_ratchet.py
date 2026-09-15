"""
tests/constitutional/test_sutra_lint_ratchet.py
───────────────────────────────────────────────

The lint is the gate; this is the gate's gate.

Three counts may only fall — arm-gated conds (Art. 13 §1), paradigm
coordinates in conds (Art. 2 §2c), and निषेध-shaped sūtras typed VIDHI with no
declared block (Art. 15). One count must stay zero: a प्रतिषेध that never
blocks anything is dead code.
"""
from __future__ import annotations

import io
import json
from contextlib import redirect_stdout

import pytest

from tools.sutra_lint import BASELINE_PATH, ERRORS, RATCHETED, lint


@pytest.fixture(scope="module")
def findings():
    return lint()["findings"]


def test_baseline_is_committed():
    assert BASELINE_PATH.exists(), "run 'python3 -m tools.sutra_lint --freeze'"
    baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    assert set(RATCHETED) <= set(baseline)


@pytest.mark.parametrize("name", RATCHETED)
def test_ratchet_never_rises(findings, name):
    baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    assert len(findings[name]) <= baseline[name], (
        f"{name} rose to {len(findings[name])} (baseline {baseline[name]}). "
        "A constitutional violation may be repaired, never added."
    )


@pytest.mark.parametrize("name", ERRORS)
def test_errors_stay_empty(findings, name):
    assert findings[name] == [], f"{name}: {findings[name][:5]}"


def test_why_not_names_the_rule_that_blocked(capsys=None):
    """The रामौ conflict must be explainable in one command (Art. 15)."""
    import sutras  # noqa: F401
    from pipelines.subanta import derive
    from tools.why_not import explain

    buf = io.StringIO()
    with redirect_stdout(buf):
        explain(derive("rAma", 1, 2), "6.1.102")
    out = buf.getvalue()
    assert "BLOCKED" in out
    assert "6.1.104" in out and "fired here" in out


def test_why_not_reports_an_unscheduled_sutra():
    import sutras  # noqa: F401
    from pipelines.subanta import derive
    from tools.why_not import explain

    buf = io.StringIO()
    with redirect_stdout(buf):
        explain(derive("rAma", 1, 1), "7.3.77")
    assert "NEVER SCHEDULED" in buf.getvalue()
