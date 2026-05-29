"""Unit tests for ``pipelines/sthAnivadAdezO_nalvidhau_paribhasha_P016_note_demo.py`` (**P016**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.sthAnivadAdezO_nalvidhau_paribhasha_P016_note_demo import (
    derive_sthAnivadAdezO_nalvidhau_paribhasha_P016_note,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P016_applies_1_1_56_then_1_1_62_and_installs_gates():
    s = derive_sthAnivadAdezO_nalvidhau_paribhasha_P016_note()
    assert _trace_ids(s) == ["1.1.56", "1.1.62"]
    assert s.paribhasha_gates.get("sthanivadbhava") is True
    assert s.paribhasha_gates.get("1.1.62_pratyayalope_pratyayalakshanam") is True

