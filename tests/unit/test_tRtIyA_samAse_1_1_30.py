"""
**1.1.30** *tṛtīyā-samāse* vs **1.1.29** *na bahuvrīhau* (user ``तृतीयासमासे निषेध .md``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from phonology.joiner import slp1_to_devanagari
from pipelines.mAsa_pUrva_tRtIyA_subanta import (
    STEM_MASA_PURVA,
    derive_dvyahapUrvAya_caturthI_eka,
    derive_mAsapUrvAya_caturthI_eka,
    derive_tryahapUrvAya_caturthI_eka,
)
from pipelines.subanta import derive


def _ap(s, sid: str) -> bool:
    for e in s.trace:
        if e.get("sutra_id") == sid and e.get("status") == "APPLIED":
            return True
    return False


def _sk(s, sid: str) -> bool:
    for e in s.trace:
        if e.get("sutra_id") == sid and e.get("status") == "SKIPPED":
            return True
    return False


def test_mAsapUrvAya_tRtIyA_path_1_1_30_not_7_1_14():
    s = derive_mAsapUrvAya_caturthI_eka()
    assert s.flat_slp1() == "mAsapUrvAya"
    assert slp1_to_devanagari(s.terms[0].varnas) == "मासपूर्वाय"
    assert _ap(s, "1.1.27")
    assert _ap(s, "1.1.30")
    assert _sk(s, "1.1.29")
    assert _ap(s, "7.1.13")
    assert _sk(s, "7.1.14")
    assert _ap(s, "7.3.102")


def test_pUrva_eka_still_smai_path_7_1_14():
    s = derive("pUrva", 4, 1, "pulliṅga")
    assert s.flat_slp1() == "pUrvasmE"
    assert _ap(s, "7.1.14")


def test_mAsa_pUrva_list_id_without_tRtIyA_triggers_smai():
    s = derive(STEM_MASA_PURVA, 4, 1, "pulliṅga")
    assert s.flat_slp1() == "mAsapUrvasmE"
    assert _ap(s, "7.1.14")


def test_dvyahapUrvAya_tryahapUrvAya_forms():
    s2 = derive_dvyahapUrvAya_caturthI_eka()
    assert s2.flat_slp1() == "dvyahapUrvAya"
    assert slp1_to_devanagari(s2.terms[0].varnas) == "द्व्यहपूर्वाय"
    s3 = derive_tryahapUrvAya_caturthI_eka()
    assert s3.flat_slp1() == "tryahapUrvAya"
    assert slp1_to_devanagari(s3.terms[0].varnas) == "त्र्यहपूर्वाय"
