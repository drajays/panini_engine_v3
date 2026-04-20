"""
tests/forward/test_forward_subanta_smoke.py
─────────────────────────────────────────────

Smoke tests for pipelines.subanta.derive — verifies that the pipeline
runs without crashing on every (vibhakti, vacana) cell of राम.  Per
CONSTITUTION Article 8 (prakriyā is a test, not a target) we do NOT
yet assert surface equality; we assert:

  • the trace is non-empty
  • each step has required keys
  • no R1Violation was raised
  • the final form renders to a non-empty SLP1 string

Surface-equality tests come online in tests/regression/ once the
18-representative-sūtra cascade is extended to the full ~200 sūtras
needed for a complete a-stem paradigm.
"""
from __future__ import annotations

import pytest

from pipelines.subanta import derive


@pytest.mark.parametrize("v,vv", [(v, vv) for v in range(1, 9) for vv in range(1, 4)])
def test_subanta_pipeline_runs(v, vv):
    state = derive("rAma", v, vv)
    assert state.trace, f"empty trace for ({v},{vv})"
    for step in state.trace:
        assert "sutra_id" in step
        assert "form_before" in step
        assert "form_after" in step
        assert "why_dev" in step
    assert state.render() != ""
