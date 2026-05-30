"""
pipelines/phalAni_santi_as_lat_padanta_lesson.py — पदान्त (१.१.५८): *padādi* लोपः vs *padānta* यण।

Vākya-anvākhyāna (फलानि सन्ति):
  फलानि (सिद्ध) + अस् + लट् + झि → **6.4.111** *as* आद्य-*a*-लोपः → **7.1.3** अन्ति →
  **1.1.57** + **1.1.58** → **6.1.77** निषेधः (न *phalānyanti*) → फलानि सन्ति।

Target SLP1 tape: **phalAnisanti** (two *pada* terms: *phalAni* + *santi*).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_lat_vartamane_jhi_and_sap,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_as_lat_adadi_2_4_72,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _phalAni_siddha() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("phalAni")),
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "phalAni"},
    )


def _as_dhatu() -> Term:
    t = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("as")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "as", "gana": 2, "karmakatva": "akarmaka"},
    )
    t.tags.discard("upadesha")
    return t


def _merge_verbal_pada(s: State) -> State:
    """Merge *s* + *anti* (post-**6.4.111** / **7.1.3**) into one verbal *pada*."""
    start = next(
        i
        for i, t in enumerate(s.terms)
        if "dhatu" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "as"
    )
    all_varnas = []
    for t in s.terms[start:]:
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"laT", "la", "Sap"}:
            continue
        if "lakAra_pratyaya_placeholder" in t.tags:
            continue
        all_varnas.extend(v.clone() for v in t.varnas)
    before = s.flat_slp1()
    merged = Term(
        kind="prakriti",
        varnas=all_varnas,
        tags={"tiṅānta", "pada"},
        meta={"upadesha_slp1": "santi"},
    )
    s.terms = [s.terms[0], merged]
    after = s.flat_slp1()
    s.trace.append({
        "sutra_id": "__VERBAL_PADA_MERGE__",
        "sutra_type": "STRUCTURAL",
        "type_label": "सन्ति-पद-मेलनम्",
        "form_before": before,
        "form_after": after,
        "why_dev": "धातु+तिङ्-शेषयोः एकं पदम् (वाक्यान्वाख्यान-पाठ)।",
        "status": "APPLIED",
    })
    return s


def derive_phalAni_santi_as_lat_padanta_lesson() -> State:
    s = State(terms=[_phalAni_siddha(), _as_dhatu()], meta={"lakara": "laT"}, trace=[])

    s.meta["3_1_68_kartari_recipe"] = True
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.123", s)
    laT = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("laT")),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    if laT.varnas and laT.varnas[-1].slp1 == "T":
        del laT.varnas[-1]
    s.terms.append(laT)

    # Finish laṭ+jhi+śap on the verbal terms only (indices 1+).
    verbal = State(terms=s.terms[1:], meta=dict(s.meta), trace=[])
    verbal = P00_lat_vartamane_jhi_and_sap(verbal)
    s.terms = [s.terms[0]] + verbal.terms
    s.meta.update(verbal.meta)
    s.trace.extend(verbal.trace)

    s.meta["2_4_72_sap_luk_arm"] = True
    s = P00_as_lat_adadi_2_4_72(s)
    s = apply_rule("7.1.3", s)

    s = apply_rule("1.1.57", s)
    s = apply_rule("1.1.58", s)
    s = apply_rule("6.1.77", s)

    s = _merge_verbal_pada(s)
    return s


__all__ = ["derive_phalAni_santi_as_lat_padanta_lesson"]
