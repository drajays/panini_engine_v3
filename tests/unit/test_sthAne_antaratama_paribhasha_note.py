"""Unit tests for ``pipelines/sthAne_antaratama_paribhasha_P008_note_demo.py`` (**P008**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.sthAne_antaratama_paribhasha_P008_note_demo import (
    derive_sthAne_antaratama_paribhasha_P008_note,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P008_note_only_applies_1_1_50_and_installs_gates():
    s = derive_sthAne_antaratama_paribhasha_P008_note()
    ids = _trace_ids(s)
    assert ids == ["1.1.50"]
    assert "sthanantara_vrddhi" in s.paribhasha_gates
    assert "sthanantara_guna" in s.paribhasha_gates

