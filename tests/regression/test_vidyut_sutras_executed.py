"""Vidyut ⊆ engine: sūtras Vidyut cites that the engine used to leave SKIPPED/absent (docs/SUTRA_SUPERSET_GAPS.md)."""
import pytest

import sutras  # noqa: F401
from pipelines.tinanta import derive

EXECUTED = {"APPLIED", "APPLIED_VACUOUS", "DEFINED", "VACUOUS", "AUDIT"}


def _fired(root, lakara):
    st = derive(root, lakara, "kartari", 3, 1)
    return {s["sutra_id"] for s in st.trace if s["status"] in EXECUTED}


@pytest.mark.parametrize("root", ["eDa~", "sparDa~"])
def test_1_3_12_fires_for_atmanepadi_roots(root):
    assert "1.3.12" in _fired(root, "laT")


def test_1_3_12_not_for_parasmaipadi_root():
    assert "1.3.12" not in _fired("BU", "laT")


@pytest.mark.parametrize("root", ["BU", "eDa~", "paWa"])
def test_luG_executes_3_4_113_and_3_4_114(root):
    assert {"3.4.113", "3.4.114"} <= _fired(root, "luG")
