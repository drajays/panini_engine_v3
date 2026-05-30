"""
pipelines/sthanivat_anal_ashrita_lesson.py — eight *anal-āśrita* *guṇa-dharma*
demos (स्थानिवद्भाव per **1.1.56**).

Each spine applies **1.1.56** before the *ādeśa* *vidhi*, then downstream rules
that read inherited *tags* on the substitute.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3, P00_vikarana_it_lopa, P00_avyaya_sup_luk
from pipelines.subanta import (
    PADA_MERGE_STEP,
    SUBANTA_RULE_IDS_POST_4_1_2,
    _pada_merge,
    build_initial_state,
    run_subanta_preflight_through_1_4_7,
)


def _with_sthanivat(s: State) -> State:
    return apply_rule("1.1.56", s)


def _dhatu(up: str, *, pratipadika: bool = False) -> Term:
    tags = {"dhatu", "anga", "upadesha"}
    if pratipadika:
        tags.add("prātipadika")
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags=tags,
        meta={"upadesha_slp1": up},
    )


def _pratyaya(up: str, *, tags: frozenset[str] | None = None) -> Term:
    tgs = {"pratyaya", "upadesha"}
    if tags:
        tgs |= set(tags)
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags=tgs,
        meta={"upadesha_slp1": up},
    )


# 1) धातुत्वम् — अस् → भू (2.4.52) → अनीयर् (3.1.96 recipe)
def derive_aster_bhU_anIyar() -> State:
    s = State(terms=[_dhatu("as")], meta={}, trace=[])
    s = _with_sthanivat(s)
    s = apply_rule("2.4.35", s)
    s = apply_rule("2.4.52", s)
    s.meta["krtya_recipe"] = "anIyar"
    s = apply_rule("3.1.96", s)
    return s


# 2) अङ्गत्वम् — किम् → क (7.2.103) + काभ्याम् (7.3.102)
def derive_kim_ka_kAByAm() -> State:
    s = build_initial_state("kim", 3, 2, "pulliṅga")
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)
    s = apply_rule("1.4.13", s)
    s = apply_rule("6.4.1", s)
    s = _with_sthanivat(s)
    s.meta["sthanivat_lesson_7_2_103"] = True
    s = apply_rule("7.2.103", s)
    s = apply_rule("7.3.102", s)
    return s


# 3) कृत्-प्रत्ययत्वम् — क्त्वा → ल्यप् (7.1.37) + तुक् (6.1.71)
def derive_apakr_lyap_tuk() -> State:
    s = State(
        terms=[_dhatu("kf"), _pratyaya("ktvA", tags=frozenset({"krt"}))],
        meta={},
        trace=[],
    )
    s = _with_sthanivat(s)
    s.meta["lyap_recipe"] = True
    s = apply_rule("7.1.37", s)
    s = P00_vikarana_it_lopa(s)
    s = apply_rule("6.1.71", s)
    return s


# 4) तद्धित-प्रत्ययत्वम् — ठञ् → इक (7.3.50) — narrow P018-style
def derive_Tak_to_ika() -> State:
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("saMvatsara")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "saMvatsara"},
    )
    pr = _pratyaya("Tak", tags=frozenset({"taddhita"}))
    s = State(terms=[stem, pr], meta={}, trace=[])
    s = _with_sthanivat(s)
    s = apply_rule("7.3.50", s)
    return s


# 5) अव्ययत्वम् — क्त्वा → ल्यप् + 1.1.40 + 2.4.82 (प्रपठ्य)
def derive_pra_paW_lyap_avyaya() -> State:
    s = State(
        terms=[
            Term(kind="upasarga", varnas=parse_slp1_upadesha_sequence("pra"), tags={"upasarga"}, meta={}),
            _dhatu("paW", pratipadika=True),
            _pratyaya("ktvA", tags=frozenset({"krt"})),
        ],
        meta={},
        trace=[],
    )
    s.meta["ktvA_recipe"] = True
    s = apply_rule("3.4.21", s)
    s = _with_sthanivat(s)
    s.meta["lyap_recipe"] = True
    s = apply_rule("7.1.37", s)
    s = P00_vikarana_it_lopa(s)
    _pada_merge(s)
    if s.terms:
        s.terms[0].tags.add("avyaya")
    s.meta["vibhakti_vacana"] = "1-1"
    s = P00_avyaya_sup_luk(s)
    return s


# 6) सुप्-प्रत्ययत्वम् — ङे → य (7.1.13) + दीर्घ (7.3.102)
def derive_rAmAya() -> State:
    s = build_initial_state("rAma", 4, 1, "pulliṅga")
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)
    s = apply_rule("1.4.13", s)
    s = apply_rule("6.4.1", s)
    s = _with_sthanivat(s)
    s = apply_rule("7.1.13", s)
    s = apply_rule("7.3.102", s)
    return s


# 7) तिङ्-प्रत्ययत्वम् — मिप् → अम् (3.4.101) under laṅ
def derive_dviz_am_laG() -> State:
    s = State(terms=[_dhatu("dviz")], meta={"lakara": "laG"}, trace=[])
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.111", s)
    lac = _pratyaya("laG", tags=frozenset({"lakAra_pratyaya_placeholder"}))
    s.terms.append(lac)
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_form"] = "mip"
    s = _with_sthanivat(s)
    s = apply_rule("3.4.78", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("3.4.101", s)
    return s


# 8) पदत्वम् — युष्माकम् → वस् (8.1.21) + रुँ (8.2.66) in tripāḍī
def derive_yuSmAkam_vas() -> State:
    pada = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("yuSmAkam")),
        tags={"pada", "prātipadika", "sarvanama"},
        meta={"upadesha_slp1": "yuSmAkam", "subanta_pada": True},
    )
    s = State(terms=[pada], meta={"sthanivat_lesson_8_1_21": True}, trace=[])
    s = _with_sthanivat(s)
    s = apply_rule("8.1.21", s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    return s


__all__ = [
    "derive_aster_bhU_anIyar",
    "derive_kim_ka_kAByAm",
    "derive_apakr_lyap_tuk",
    "derive_Tak_to_ika",
    "derive_pra_paW_lyap_avyaya",
    "derive_rAmAya",
    "derive_dviz_am_laG",
    "derive_yuSmAkam_vas",
]
