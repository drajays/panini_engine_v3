"""
pipelines/yAyAvar_yang_varac_purvavidhau_lesson.py — वरेय (१.१.५८): यायावर।

Prakriyā (per user spine; no *su* / visarga — flat *kṛdanta* ``yAyAvar``):

  या + यङ् → **6.1.9** द्वित्व → **3.1.32** → **3.2.176** वरच् →
  *aṅga* merge + *yaṅ* residue ``a`` → **6.4.48** अतो लोपः → **1.1.57** → **1.1.58** →
  **6.4.64** निषेधः → *it* lopa → **6.1.66** लोपो व्योर्वलि → *pada* merge → यायावर।
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_bhuvadi_dhatu_it_anunasik_hal,
    P00_hal_it_lopa,
    P00_yang_adhikara_yaG_append_sanadi,
    P00_yang_dvitva_abhyasa_gate,
    P00_yang_abhyasa_hrasva_chain,
    P00_a_lopa_sthanivat_1_1_58,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("yA")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "yA"},
    )
    return State(terms=[dhatu], meta={}, trace=[], samjna_registry={})


def _merge_angas_with_yaG_a_before_varac(s: State) -> State:
    """Merge *abhyāsa*+*dhātu*; retain *yaṅ* ``a`` for **6.4.48** (*yāyāy+a*)."""
    varac = next(
        t for t in s.terms if (t.meta.get("upadesha_slp1") or "").strip() == "varac"
    )
    ang_terms = [t for t in s.terms if t is not varac]
    varnas = []
    for t in ang_terms:
        varnas.extend(v.clone() for v in t.varnas)
    varnas.extend(parse_slp1_upadesha_sequence("a"))
    before = s.flat_slp1()
    stem = Term(
        kind="prakriti",
        varnas=varnas,
        tags={"dhatu", "anga", "prātipadika"},
        meta={"upadesha_slp1": "yAyAya"},
    )
    s.terms = [stem, varac]
    after = s.flat_slp1()
    s.trace.append(
        {
            "sutra_id": "__YANG_ANGA_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "यङन्ताङ्ग-मेलनम्",
            "form_before": before,
            "form_after": after,
            "why_dev": "यायाय + यङ्-अकारः → यायायअ (६.४.४८-पूर्वम्)।",
            "status": "APPLIED",
        }
    )
    return s


def _varac_surface_var(varac: Term) -> list:
    """*varac* after *it*-lopa → surface *var* (वर), not *vara*."""
    vs = list(varac.varnas)
    if len(vs) >= 4 and vs[0].slp1 == "v" and vs[-1].slp1 == "a":
        return [v.clone() for v in vs[:3]]
    return [v.clone() for v in vs]


def _merge_stem_varac(s: State) -> State:
    if len(s.terms) < 2:
        return s
    stem, varac = s.terms[0], s.terms[1]
    before = s.flat_slp1()
    merged = Term(
        kind="prakriti",
        varnas=list(stem.varnas) + _varac_surface_var(varac),
        tags={"prātipadika", "krt", "pulliṅga"},
        meta={"upadesha_slp1": "yAyAvar"},
    )
    s.terms = [merged]
    after = s.flat_slp1()
    s.trace.append(
        {
            "sutra_id": "__KRT_PADA_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "वरच्-मेलनम्",
            "form_before": before,
            "form_after": after,
            "why_dev": "याया + वर → यायावर (रूपसिद्धि)।",
            "status": "APPLIED",
        }
    )
    return s


def derive_yAyAvar_yang_varac_purvavidhau_lesson() -> State:
    s = _build_state()

    s = apply_rule("1.1.68", s)
    s = P00_bhuvadi_dhatu_it_anunasik_hal(s)
    s = P00_yang_adhikara_yaG_append_sanadi(s)
    s = P00_yang_dvitva_abhyasa_gate(s)

    s.meta["7_4_59_abhyasa_hrasva_arm"] = True
    s.meta["P029_7_4_83_abhyasa_dirgha_arm"] = True
    s = P00_yang_abhyasa_hrasva_chain(s)

    s.meta["varac_recipe"] = True
    s = apply_rule("3.2.176", s)

    s = _merge_angas_with_yaG_a_before_varac(s)

    s = P00_a_lopa_sthanivat_1_1_58(s)
    s = apply_rule("6.4.64", s)

    s = apply_rule("6.1.66", s)
    s = P00_hal_it_lopa(s)

    s = _merge_stem_varac(s)
    s.meta["linga"] = "pulliṅga"
    return s


__all__ = ["derive_yAyAvar_yang_varac_purvavidhau_lesson"]
