"""
*सर्वकः* / *विश्वकः* — **5.3.71** *akac* *prāk ṭeḥ* (user ``सर्वकः.md``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from phonology.joiner import slp1_to_devanagari
from pipelines.sarvaka_subanta import derive_sarvakaha


def _had_applied(s, sutra_id: str) -> bool:
    for e in s.trace:
        if e.get("sutra_id") == sutra_id and e.get("status") == "APPLIED":
            return True
    return False


def test_sarvakaha_prathama_eka_slp1_dev():
    s = derive_sarvakaha("sarva")
    assert s.flat_slp1() == "sarvakaH"
    assert slp1_to_devanagari(s.terms[0].varnas) == "सर्वकः"


def test_sarvakaha_trace_5_3_71_1_2_46_8_2_8_3():
    s = derive_sarvakaha("sarva")
    for sid in ("5.3.71", "1.2.46", "8.2.66", "8.3.15"):
        assert _had_applied(s, sid), f"expected {sid} APPLIED in trace"


def test_viSvakaha_parallel_viSva_stem():
    s = derive_sarvakaha("viSva")
    assert s.flat_slp1() == "viSvakaH"
    assert slp1_to_devanagari(s.terms[0].varnas) == "विश्वकः"
