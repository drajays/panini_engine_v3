"""
pipelines/sthanivat_al_ashrita_exceptions_lesson.py — four *al-āśrita*
*guṇa-dharma* cases where **1.1.56** *sthānivadādeśa* does **not** apply.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_sup_it_lopa_aprkta
from engine import apply_rule
from engine.state import State, Term
from engine.sthanivat import BLOCK_NIMITTA_ELSEWHERE, mark_sthanivat_block
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _with_sthanivat(s: State) -> State:
    return apply_rule("1.1.56", s)


# 1) दिव् + भ्याम् — 6.1.131 → 6.1.77 (द्युभ्याम्)
def derive_div_byAm_dyubhyAm() -> State:
    div = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("div")),
        tags={"anga"},
        meta={"upadesha_slp1": "div"},
    )
    byAm = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("ByAm")),
        tags={"sup", "pratyaya"},
        meta={"upadesha_slp1": "ByAm"},
    )
    s = State(terms=[div, byAm], meta={"sthanivat_lesson_div_byam": True}, trace=[])
    s = _with_sthanivat(s)
    s = apply_rule("6.1.131", s)
    s = apply_rule("6.1.70", s)
    s = apply_rule("6.1.77", s)
    return s


# 2) पथिन् + सुँ — 7.1.85 आ-ādeśa blocks wrong 6.1.68
def derive_pathin_su_panTAH() -> State:
    pathin = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("pathin")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "pathin"},
    )
    s = State(
        terms=[pathin],
        meta={"sthanivat_lesson_pathin": True, "vibhakti_vacana": "1-1"},
        trace=[],
    )
    s = apply_rule("4.1.2", s)
    s = apply_rule("6.4.1", s)
    s = _with_sthanivat(s)
    s = P00_sup_it_lopa_aprkta(s)
    s = apply_rule("7.1.85", s)
    s = apply_rule("6.1.68", s)
    s = apply_rule("7.1.86", s)
    s = apply_rule("7.1.87", s)
    s = apply_rule("6.1.101", s)
    return s


# 3) राम + इष्टः — no यणादित्व on इष्ट from यज्
def derive_rAma_izwaH() -> State:
    from engine.sthanivat import BLOCK_AL_BEFORE_STHANIN

    rAma = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("rAma")),
        tags={"prātipadika"},
        meta={"upadesha_slp1": "rAma"},
    )
    izwa = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("izwa")),
        tags={"krt", "pratyaya"},
        meta={
            "upadesha_slp1": "izwa",
            "no_yan_aditva_inheritance": True,
        },
    )
    mark_sthanivat_block(izwa, BLOCK_AL_BEFORE_STHANIN)
    s = State(terms=[rAma, izwa], meta={}, trace=[])
    s = _with_sthanivat(s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.17", s)
    s = apply_rule("8.3.19", s)
    return s


# 4) व्यूढ + उरः + कप् — स-आदेश without विसर्गान्त inheritance on उरस्
def derive_vyUDhoraska() -> State:
    vyUDha = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("vyUDhaH")),
        tags={"samasa_member", "anga"},
        meta={"upadesha_slp1": "vyUDha"},
    )
    uras = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("uras")),
        tags={"samasa_member", "anga"},
        meta={"upadesha_slp1": "uras", "upadesha_slp1_original": "uraH"},
    )
    kap = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("kap")),
        tags={"pratyaya", "taddhita"},
        meta={"upadesha_slp1": "kap"},
    )
    s = State(terms=[vyUDha, uras, kap], meta={}, trace=[])
    s.tripadi_zone = True
    s = _with_sthanivat(s)
    s.meta["sthanivat_lesson_vyUDhoraska"] = True
    if s.terms[0].varnas[-1].slp1 == "H":
        s.terms[0].varnas[-1] = mk("s")
        mark_sthanivat_block(s.terms[0], BLOCK_NIMITTA_ELSEWHERE)
        s.terms[0].meta["visargantatva_inhibited"] = True
        s.trace.append(
            {
                "sutra_id": "8.3.38",
                "status": "APPLIED",
                "why_dev": "व्यूढोरः-सन्धौ विसर्गस्य स-आदेशः (स्थानिवत्-रोधः)।",
            }
        )
    s = apply_rule("8.4.2", s)
    return s


__all__ = [
    "derive_div_byAm_dyubhyAm",
    "derive_pathin_su_panTAH",
    "derive_rAma_izwaH",
    "derive_vyUDhoraska",
]
