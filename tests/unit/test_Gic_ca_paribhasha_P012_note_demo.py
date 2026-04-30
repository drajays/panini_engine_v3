"""Unit tests for ``pipelines/Gic_ca_paribhasha_P012_note_demo.py`` (**P012**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.Gic_ca_paribhasha_P012_note_demo import derive_Gic_ca_paribhasha_P012_note


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P012_applies_1_1_52_then_1_1_53_and_installs_gates():
    s = derive_Gic_ca_paribhasha_P012_note()
    assert _trace_ids(s) == ["1.1.52", "1.1.53"]

    assert "1.1.52_alo_antyasya" in s.paribhasha_gates
    assert "1.1.53_Gic_ca" in s.paribhasha_gates

