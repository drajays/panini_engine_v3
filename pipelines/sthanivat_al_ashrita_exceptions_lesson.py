"""
pipelines/sthanivat_al_ashrita_exceptions_lesson.py — four worked *pariśiṣṭa*
examples from this region of the text. The first three are *al-āśrita*
*guṇa-dharma* cases where **1.1.56** *sthānivadādeśa* does **not** apply;
the fourth (व्यूढोरस्केन) is a same-mechanism sibling of महोरस्केन the text
cross-references rather than an independent अल्-आश्रित exception — kept here
as it shares this file's setup/tests, see its own docstring below.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_guna_prayoga_readiness,
    P00_kap_bahuvrihi_head,
    P00_sup_it_lopa_aprkta,
)
from engine import apply_rule
from engine.state import State, Term
from engine.sthanivat import mark_sthanivat_block
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.subanta import derive_from_state


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
        varnas=list(parse_slp1_upadesha_sequence("paTin")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "paTin"},
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


# 4) व्यूढ + उरस् (बहुव्रीहि) + कप् (5.4.151) + तृतीया एकवचन → व्यूढोरस्केन
#
# PDF p.655 (Mīmāṃsaka Aṣṭādhyāyī-Bhāṣya, pariśiṣṭa) gives महोरस्केन's full
# derivation on p.654, then for व्यूढोरस्केन says only "इसी प्रकार...की
# सिद्धि भी जानें" — "understand its derivation the same way." It is not an
# independently-worked example, and (re-checked against the source) it is
# not actually one of this file's four अल्-आश्रित 1.1.56 exceptions either —
# it is cited there purely as a same-mechanism sibling of महोरस्केन
# (`pipelines/mahoraskena_bahuvrihi.py`), minus महोरस्केन's महत्→महा-specific
# 6.3.46 step (व्यूढ needs no पूर्वपद-आदेश — it already ends in अ, so 6.1.87
# आद्गुणः applies directly: व्यूढ-अ + उरस्-उ → व्यूढो-रस्, "o"). Kept here
# (rather than moved) since it is already the established home for this
# word's demo/tests; the earlier version's विसर्ग/8.3.38/8.4.2 premise had
# no textual basis — व्यूढ ends in a vowel, not visarga, as a समास पूर्वपद.
def derive_vyUDhoraska() -> State:
    vyUDha = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("vyUDha")),
        tags={"anga", "samasa_member", "bahuvrIhi"},
        meta={"upadesha_slp1": "vyUDha"},
    )
    uras = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("uras")),
        tags={"anga", "samasa_member", "bahuvrIhi"},
        meta={"upadesha_slp1": "uras"},
    )
    s = State(terms=[vyUDha, uras], meta={}, trace=[], samjna_registry={})
    s.meta["sthanivat_lesson_vyUDhoraska"] = True

    s = P00_kap_bahuvrihi_head(s)
    s = apply_rule("1.2.46", s)
    s = P00_guna_prayoga_readiness(s)
    s = apply_rule("6.1.87", s)   # A+u -> o: vyUDha+uras -> vyUDhoras(ka)

    s = derive_from_state(s, 3, 1)  # tṛtīyā ekavacana: ...ka + TA -> ...kena

    s = apply_rule("1.1.56", s)
    s.meta.pop("1_1_68_svadrupa_audit_done", None)
    s = apply_rule("1.1.68", s)
    return s


__all__ = [
    "derive_div_byAm_dyubhyAm",
    "derive_pathin_su_panTAH",
    "derive_rAma_izwaH",
    "derive_vyUDhoraska",
]
