"""
Four *al-āśrita* exceptions to **1.1.56** *sthānivadādeśa* (pedagogy).
"""
from __future__ import annotations

import pytest

from engine.sthanivat import (
    BLOCK_AL_AFTER_STHANIN,
    BLOCK_AL_BEFORE_STHANIN,
    BLOCK_AL_SAME_SITE,
    BLOCK_NIMITTA_ELSEWHERE,
    sthanivat_blocked,
)
from pipelines.sthanivat_al_ashrita_exceptions_lesson import (
    derive_div_byAm_dyubhyAm,
    derive_pathin_su_panTAH,
    derive_rAma_izwaH,
    derive_vyUDhoraska,
)


def _applied(s, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and e.get("status") == "APPLIED"
        for e in s.trace
    )


def test_1_div_ut_u_not_vantatva_then_yan() -> None:
    s = derive_div_byAm_dyubhyAm()
    u_term = next(
        (t for t in s.terms if t.meta.get("6_1_131_residue_from_div")),
        None,
    )
    assert u_term is not None
    assert sthanivat_blocked(u_term, BLOCK_AL_SAME_SITE)
    assert _applied(s, "6.1.131")
    assert not _applied(s, "6.1.70")
    assert _applied(s, "6.1.77")
    flat = s.flat_slp1()
    assert flat.startswith("dyu") or "dyu" in flat


def test_2_pathin_a_adesha_blocks_6_1_68() -> None:
    s = derive_pathin_su_panTAH()
    anga = s.terms[0]
    assert sthanivat_blocked(anga, BLOCK_AL_AFTER_STHANIN)
    assert anga.meta.get("7_1_85_a_adesha") is True
    assert _applied(s, "7.1.85")
    assert not _applied(s, "6.1.68")
    sup = next((t for t in s.terms if "sup" in t.tags), None)
    assert sup is not None and sup.varnas and sup.varnas[0].slp1 == "s"


def test_3_rAma_izwaH_no_yanaditva_u_on_izwa() -> None:
    s = derive_rAma_izwaH()
    izwa = s.terms[-1]
    assert sthanivat_blocked(izwa, BLOCK_AL_BEFORE_STHANIN)
    assert not _applied(s, "6.1.114")
    flat = s.flat_slp1()
    assert "izwa" in flat or "izwaH" in flat
    assert "u" not in flat.split("izwa")[-1][:2]


def test_4_vyUDhoraska_no_natva_after_visarga_s() -> None:
    s = derive_vyUDhoraska()
    assert s.terms[0].varnas[-1].slp1 == "s"
    assert sthanivat_blocked(s.terms[0], BLOCK_NIMITTA_ELSEWHERE)
    assert not _applied(s, "8.4.2")
    assert "R" not in s.flat_slp1()
