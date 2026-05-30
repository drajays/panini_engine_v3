"""
pipelines/kaNDUti_ktic_vareya_yalopa_lesson.py — वरेय (१.१.५८): कण्डूति।

Prakriyā:
  कण्डूय + **3.3.174** क्तिच् → **6.4.48** अतो लोपः → **1.1.57** → **1.1.58** →
  *it* lopa → **6.1.66** लोपो व्योर्वलि → कण्डूति।
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_hal_it_lopa, P06a_pratyaya_adhikara_3_1_1_to_3, P00_a_lopa_sthanivat_1_1_58
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kaNDUya")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "kaNDUya"},
    )
    return State(terms=[dhatu], meta={}, trace=[])


def _ktic_surface_ti(krt: Term) -> list:
    """*ktic* after *it*-lopa → surface *ti* (skip *kit* ``k``)."""
    vs = list(krt.varnas)
    for j, v in enumerate(vs):
        if v.slp1 == "t":
            return [x.clone() for x in vs[j:]]
    return [v.clone() for v in vs]


def _merge_kaNDU_ti(s: State) -> State:
    if len(s.terms) < 2:
        return s
    stem, krt = s.terms[0], s.terms[1]
    before = s.flat_slp1()
    merged = Term(
        kind="prakriti",
        varnas=list(stem.varnas) + _ktic_surface_ti(krt),
        tags={"prātipadika", "krt", "strīliṅga"},
        meta={"upadesha_slp1": "kaNDUti"},
    )
    s.terms = [merged]
    after = s.flat_slp1()
    s.trace.append(
        {
            "sutra_id": "__KRT_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "क्तिच्-मेलनम्",
            "form_before": before,
            "form_after": after,
            "why_dev": "कण्डू + ति → कण्डूति (रूपसिद्धि)।",
            "status": "APPLIED",
        }
    )
    return s


def derive_kaNDUti_ktic_vareya_yalopa_lesson() -> State:
    s = _build_state()

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s.meta["ktic_3_3_174_recipe"] = True
    s = apply_rule("3.3.174", s)

    s = P00_a_lopa_sthanivat_1_1_58(s)

    s = apply_rule("6.1.66", s)
    s = P00_hal_it_lopa(s)

    s = _merge_kaNDU_ti(s)
    s.meta["linga"] = "strīliṅga"
    return s


__all__ = ["derive_kaNDUti_ktic_vareya_yalopa_lesson"]
