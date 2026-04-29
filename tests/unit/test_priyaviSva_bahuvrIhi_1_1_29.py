"""
*प्रियविश्वाय* / **1.1.29** *na bahuvrīhau* (user ``प्रियविश्वाय.md`` *Form 1*).
"""
from __future__ import annotations

import sutras  # noqa: F401

from phonology.joiner import slp1_to_devanagari
from pipelines.priyaviSva_bahuvrIhi_subanta import derive_priyaviSvAya_caturthI_eka
from pipelines.subanta import derive


def _had(s, sid: str, st: str) -> bool:
    for e in s.trace:
        if e.get("sutra_id") == sid and e.get("status") == st:
            return True
    return False


def test_priyaviSvAya_caturthI_eka_bahuvrIhi_path():
    s = derive_priyaviSvAya_caturthI_eka()
    assert s.flat_slp1() == "priyaviSvAya"
    assert slp1_to_devanagari(s.terms[0].varnas) == "प्रियविश्वाय"
    assert _had(s, "1.1.27", "APPLIED")
    assert _had(s, "1.1.29", "APPLIED")
    assert _had(s, "7.1.14", "SKIPPED")
    assert _had(s, "7.1.13", "APPLIED")
    assert _had(s, "7.3.102", "APPLIED")


def test_priya_viSva_without_bahuvrIhi_sarvanAma_smai():
    s = derive("priya-viSva", 4, 1, "pulliṅga")
    assert s.flat_slp1() == "priyaviSvasmE"
    assert _had(s, "1.1.14", "APPLIED")
    assert not _had(s, "1.1.29", "APPLIED")
