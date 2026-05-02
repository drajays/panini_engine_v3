"""Unit tests for ``pipelines/anekAlSit_sarvasya_paribhasha_P015_demo.py`` (**P015**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.anekAlSit_sarvasya_paribhasha_P015_demo import (
    derive_anekAlSit_sarvasya_paribhasha_P015_demo,
)


def test_P015_installs_gate_and_demonstrates_si_replacement():
    s = derive_anekAlSit_sarvasya_paribhasha_P015_demo()

    # Gate installed by 1.1.55.
    assert s.paribhasha_gates.get("1.1.55") is True

    # After resetting the tape, 7.1.20 should have rewritten the WHOLE sup pratyaya to Si.
    assert len(s.terms) == 2
    assert (s.terms[-1].meta.get("upadesha_slp1") or "").strip() == "Si"
    assert s.flat_slp1() == "aSi"

