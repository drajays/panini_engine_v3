"""
pipelines/kathi_kath_nic_lesson.py — कथ (चुरादिः, वाक्यप्रबन्ध) + णिच् (३.१.२५).

Prakriyā:
  कथ + णिच् → कथ + इ → कथ् + इ (**6.4.48** अतो लोपः; **1.1.57** स्थानिवत् on lupta *a*)
  → कथि (**3.1.32** धातुसंज्ञा) — **7.2.116** blocked (परनिमित्तक लोपः).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_krt_it_lopa
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _merge_kath_i_to_kathi(state: State) -> None:
    if len(state.terms) < 2:
        return
    ang, nic = state.terms[0], state.terms[1]
    meta = {"upadesha_slp1": "kathi", "curadi_kath": True}
    for key in ("6_4_48_a_lopa_done", "upadha_blocked_para_nimitta"):
        if key in ang.meta:
            meta[key] = ang.meta[key]
    merged = Term(
        kind="prakriti",
        varnas=list(ang.varnas) + list(nic.varnas),
        tags={"dhatu", "anga", "prātipadika"},
        meta=meta,
    )
    state.terms = [merged]
    state.emit_structural(
        "__MERGE__",
        form_before=state.flat_slp1(),
        form_after=state.flat_slp1(),
        why_dev="कथ् + णिच्-अवशेष-इ → कथि (चुरादि-णिच्-डेमो)।",
        type_label="धातु-मेलनम्",
    )


def derive_kathi_kath_nic_lesson() -> State:
    # कथँ — कथ + अ (अनुदात्त); engine tape k,a,t,h,a
    katha = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("katha")),
        tags={"prātipadika", "curadi", "dhatu", "anga"},
        meta={"upadesha_slp1": "katha", "curadi_kath": True, "gana": 10},
    )
    s = State(terms=[katha], meta={}, trace=[])

    s = apply_rule("1.1.68", s)
    s = apply_rule("1.2.45", s)

    s.meta["nic_recipe"] = "nic"
    s = apply_rule("3.1.25", s)
    s = apply_rule("3.1.26", s)
    s = P00_krt_it_lopa(s)

    s = apply_rule("6.4.48", s)
    s = apply_rule("1.1.57", s)
    s = apply_rule("7.2.116", s)

    s = apply_rule("3.1.32", s)

    _merge_kath_i_to_kathi(s)
    return s


__all__ = ["derive_kathi_kath_nic_lesson"]
