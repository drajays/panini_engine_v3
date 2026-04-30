"""Unit tests for ``pipelines/pramANakRtAntarye_paribhasha_P007_demo.py`` (**P007**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.pramANakRtAntarye_paribhasha_P007_demo import (
    derive_pramANakRtAntarye_P007_demo,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P007_paribhasha_notes_1_1_50_then_1_1_48():
    s = derive_pramANakRtAntarye_P007_demo()
    ids = _trace_ids(s)
    assert ids.index("1.1.50") < ids.index("1.1.48")

    # 1.1.50 installs selection gates; 1.1.48 sets its own paribhāṣā gate.
    assert "sthanantara_vrddhi" in s.paribhasha_gates
    assert "sthanantara_guna" in s.paribhasha_gates
    assert s.paribhasha_gates.get("1.1.48_ec_ig_hrasva") is True

    # E (ec) → i (ik hrasva) by 1.1.48 demo kernel.
    assert s.flat_slp1() == "i"

