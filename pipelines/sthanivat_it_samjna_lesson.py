"""
pipelines/sthanivat_it_samjna_lesson.py — *it-saṃjñā* always extends to ādeśa.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_krt_it_lopa,
    P00_nvul_krt_prefix,
    P00_nvul_133_7_1_1,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P01_samjna_dhatu_class,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _with_sthanivat(s: State) -> State:
    return apply_rule("1.1.56", s)


def _dhatu(up: str, **meta) -> Term:
    m = {"upadesha_slp1": up}
    m.update(meta)
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(up.rstrip("~"))),
        tags={"dhatu", "anga"},
        meta=m,
    )


def _pratyaya(up: str, **meta) -> Term:
    m = {"upadesha_slp1": up}
    m.update(meta)
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags={"pratyaya"},
        meta=m,
    )


# 1) क्त्वा (कित्) → ल्यप् — प्र+भू+ल्यप् blocks guṇa (१.१.५)
def derive_pra_bhU_lyap_kngiti() -> State:
    s = State(
        terms=[
            Term(
                kind="upasarga",
                varnas=parse_slp1_upadesha_sequence("pra"),
                tags={"upasarga"},
                meta={},
            ),
            _dhatu("BU~"),
            _pratyaya("ktvA", tags={"pratyaya", "krt"}, it_markers={"k"}),
        ],
        meta={},
        trace=[],
    )
    s.meta["lyap_recipe"] = True
    s = _with_sthanivat(s)
    s = apply_rule("7.1.37", s)
    s = apply_rule("1.1.5", s)
    s = apply_rule("7.3.84", s)
    return s


# 2) ब्रूञ् (ञित्) → वच्-आदेश — १.३.७२ आत्मनेपदम्
def derive_brU_vac_atmanepada() -> State:
    from engine.sthanivat import adesha_substitute_varnas

    dhatu = _dhatu("brU~", it_markers={"Y"})
    dhatu.tags.update({"svaritaYit", "Yit_dhatu", "kartfBiprAya_usage"})
    sap = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Sap")),
        tags={"pratyaya", "vikarana", "upadesha"},
        meta={"upadesha_slp1": "Sap"},
    )
    s = State(terms=[dhatu, sap], meta={}, trace=[])
    s = _with_sthanivat(s)
    dhatu_t = next(t for t in s.terms if "dhatu" in t.tags)
    sap_t = next(t for t in s.terms if t.meta.get("upadesha_slp1") == "Sap")
    adesha_substitute_varnas(sap_t, "vac", s, sutra_id="3.1.68", sthanin_term=dhatu_t)
    s = apply_rule("1.3.72", s)
    return s


# 3) ण्वुल् (णित्) → अक् — भू+ण्वुल् → ७.२.११५ वृद्धि
def derive_bhU_Nvul_ak_vrddhi() -> State:
    s = State(terms=[_dhatu("BU~")], meta={}, trace=[])
    s = P01_samjna_dhatu_class(s)
    s.meta["krt_artha"] = "kartari"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s.meta["krt_upadesha_slp1"] = "Nvul"
    s = _with_sthanivat(s)
    s = P00_nvul_133_7_1_1(s)
    s = apply_rule("7.2.115", s)
    return s


# 4) सिप् (अपित्) → हि — ३.४.८७
def derive_lot_sip_hi_apit() -> State:
    loT = Term(
        kind="pratyaya",
        varnas=[],
        tags={"lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "loT"},
    )
    sip = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("sip")),
        tags={"pratyaya", "tin", "tin_adesha_3_4_78"},
        meta={
            "upadesha_slp1": "sip",
            "is_apit": True,
            "source_lakara_upadesha": "loT",
        },
    )
    s = State(terms=[loT, sip], meta={}, trace=[])
    s = _with_sthanivat(s)
    s = apply_rule("3.4.87", s)
    return s


__all__ = [
    "derive_pra_bhU_lyap_kngiti",
    "derive_brU_vac_atmanepada",
    "derive_bhU_Nvul_ak_vrddhi",
    "derive_lot_sip_hi_apit",
]
