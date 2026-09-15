"""
Eight *anal-āśrita* *guṇa-dharma* lessons (**1.1.56** + *ādeśa* *vidhi*).
"""
from __future__ import annotations

import pytest

from engine.sthanivat import (
    ANGATVA,
    AVYAYATVA,
    DHATUTVA,
    KRT_PRATYAYATVA,
    PADATVA,
    SUP_PRATYAYATVA,
    TADDHITA_PRATYAYATVA,
    TING_PRATYAYATVA,
    term_has_gunadharma,
)
from pipelines.sthanivat_anal_ashrita_lesson import (
    derive_Tak_to_ika,
    derive_apakr_lyap_tuk,
    derive_aster_bhU_anIyar,
    derive_dviz_am_laG,
    derive_kim_ka_kAByAm,
    derive_pra_paW_lyap_avyaya,
    derive_rAmAya,
    derive_yuSmAkam_vas,
)


def _applied(s, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and e.get("status") == "APPLIED"
        for e in s.trace
    )


def test_1_dhatutva_as_to_bhu_anIyar() -> None:
    s = derive_aster_bhU_anIyar()
    dh = next(t for t in s.terms if "dhatu" in t.tags)
    assert dh.meta.get("upadesha_slp1") == "BU~"
    assert term_has_gunadharma(dh, DHATUTVA)
    assert any(t.meta.get("upadesha_slp1") == "anIyar" for t in s.terms)
    assert _applied(s, "2.4.52")


def test_2_angatva_kim_to_ka_dirgha() -> None:
    s = derive_kim_ka_kAByAm()
    assert s.flat_slp1().startswith("kABy")
    stem = s.terms[0]
    assert term_has_gunadharma(stem, ANGATVA)
    assert _applied(s, "7.2.103")
    assert _applied(s, "7.3.102")


def test_3_krt_pratyayatva_lyap_tuk() -> None:
    s = derive_apakr_lyap_tuk()
    pr = next(t for t in s.terms if t.kind == "pratyaya")
    assert term_has_gunadharma(pr, KRT_PRATYAYATVA)
    assert "t" in s.flat_slp1()
    assert _applied(s, "7.1.37")
    assert _applied(s, "6.1.71")


def test_4_taddhita_Tak_to_ika() -> None:
    s = derive_Tak_to_ika()
    pr = s.terms[-1]
    assert pr.meta.get("upadesha_slp1") == "ika"
    assert term_has_gunadharma(pr, TADDHITA_PRATYAYATVA)


def test_5_avyayatva_prapaWya_sup_luk() -> None:
    s = derive_pra_paW_lyap_avyaya()
    assert any("avyaya" in t.tags for t in s.terms)
    assert _applied(s, "2.4.82") or s.meta.get("2_4_82_luk")


def test_6_sup_pratyayatva_rAmAya() -> None:
    s = derive_rAmAya()
    assert s.flat_slp1() == "rAmAya"
    pr = s.terms[-1]
    assert term_has_gunadharma(pr, SUP_PRATYAYATVA)
    assert _applied(s, "7.1.13")


def test_7_ting_pratyayatva_laG_am() -> None:
    s = derive_dviz_am_laG()
    tin = next(t for t in s.terms if "tin_adesha_3_4_78" in t.tags)
    assert "".join(v.slp1 for v in tin.varnas) == "am"
    assert term_has_gunadharma(tin, TING_PRATYAYATVA)
    assert _applied(s, "3.4.101")


def test_8_padatva_yuSmAkam_vas() -> None:
    s = derive_yuSmAkam_vas()
    t = s.terms[0]
    assert t.meta.get("upadesha_slp1") == "vas"
    assert term_has_gunadharma(t, PADATVA)
    assert _applied(s, "8.1.21")
