"""
*It-saṃjñā* extends to ādeśa per **1.1.56** (always, unlike *al*-blockers).
"""
from __future__ import annotations

from engine.sthanivat import APIT_SAMJNA, KIT_SAMJNA, NIT_SAMJNA, term_has_it_samjna, term_is_apit
from pipelines.sthanivat_it_samjna_lesson import (
    derive_bhU_Nvul_ak_vrddhi,
    derive_brU_vac_atmanepada,
    derive_lot_sip_hi_apit,
    derive_pra_bhU_lyap_kngiti,
)
from sutras.adhyaya_1.pada_1.sutra_1_1_5 import ik_guna_vriddhi_blocked_by_1_1_5


def _applied(s, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and e.get("status") == "APPLIED"
        for e in s.trace
    )


def test_1_ktva_kit_lyap_blocks_guna() -> None:
    s = derive_pra_bhU_lyap_kngiti()
    lyap = next(t for t in s.terms if t.meta.get("upadesha_slp1") == "lyap")
    assert "kngiti" in lyap.tags
    assert term_has_it_samjna(lyap, KIT_SAMJNA)
    assert _applied(s, "7.1.37")
    assert ik_guna_vriddhi_blocked_by_1_1_5(s)
    assert not _applied(s, "7.3.84")


def test_2_brU_nit_vac_adesha_atmanepada() -> None:
    s = derive_brU_vac_atmanepada()
    vac = next(t for t in s.terms if t.meta.get("upadesha_slp1") == "vac")
    assert term_has_it_samjna(vac, NIT_SAMJNA)
    assert s.meta.get("pada") == "Atmanepada"
    assert _applied(s, "1.3.72")


def test_3_nvul_nit_ak_vrddhi() -> None:
    s = derive_bhU_Nvul_ak_vrddhi()
    ak = s.terms[-1]
    assert ak.meta.get("upadesha_slp1") == "ak"
    assert term_has_it_samjna(ak, NIT_SAMJNA)
    assert _applied(s, "7.2.115")


def test_4_sip_apit_hi_not_pit() -> None:
    s = derive_lot_sip_hi_apit()
    hi = next(t for t in s.terms if t.meta.get("upadesha_slp1") == "hi")
    assert term_is_apit(hi)
    assert term_has_it_samjna(hi, APIT_SAMJNA)
    assert hi.meta.get("pit") is not True
    assert _applied(s, "3.4.87")
