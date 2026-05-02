"""Unit tests for ``pipelines/tasmAd_iti_uttarasya_paribhasha_P044_note_demo.py`` (**P044**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.tasmAd_iti_uttarasya_paribhasha_P044_note_demo import (
    derive_tasmAd_iti_uttarasya_paribhasha_P044_note,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P044_trace_paribhasha_sequence_and_gates():
    s = derive_tasmAd_iti_uttarasya_paribhasha_P044_note()
    assert _trace_ids(s) == [
        "1.1.68",
        "1.1.67",
        "8.1.28",
        "1.1.67",
        "8.1.28",
        "1.1.66",
        "1.1.67",
    ]
    assert s.meta.get("1_1_68_svadrupa_audit_done") is True
    assert "1.1.67_tasmAd_iti_uttarasya" in s.paribhasha_gates
    assert "1.1.67_atiNa_panchami_targets_uttara" in s.paribhasha_gates
    assert "1.1.66_tasminniti_nirdiste_purvasya" in s.paribhasha_gates
    assert "1.1.67_panchami_saptami_positional_semantics" in s.paribhasha_gates
    assert s.meta.get("P044_8_1_28_tin_atina_note_done") is True
    assert s.meta.get("P044_8_1_28_nighata_note_done") is True
    assert s.meta.get("P044_nighata_on_following_tin_demo") is True
    assert s.meta.get("P044_8_1_28_tin_context_arm") is None
    assert s.meta.get("P044_8_1_28_nighata_illustration_arm") is None
    assert s.meta.get("P044_1_1_67_atina_arm") is None
    assert s.meta.get("P044_1_1_67_siddhi_arm") is None
