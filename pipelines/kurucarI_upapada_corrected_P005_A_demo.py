"""
pipelines/kurucarI_upapada_corrected_P005_A_demo.py — **P005-A** कुरुचरी.

``kuru`` + सप्तमी *Ni* + *√car* + **ट** (**3.2.16**) → internal *sup* *luk* (**2.4.71**),
*ṅīp* (**4.1.15**), **6.4.148**, **6.1.68** *su*-lopa — aligned with
``corrected_prakriyas_v2`` row **P005-A**.

CONSTITUTION Art. 7 / 11: ``apply_rule`` + documented structural merges only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.lopa_ghost import term_is_sup_luk_ghost
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _merge_kurucara(state: State) -> None:
    """Skip **2.4.71** ghosts; concatenate *kuru* + *car* + *wa* residue."""
    acc: list = []
    for t in state.terms:
        if term_is_sup_luk_ghost(t):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "kuru":
            acc.extend(v.clone() for v in t.varnas)
        elif up == "car":
            acc.extend(v.clone() for v in t.varnas)
        elif "krt" in t.tags and up == "wa":
            acc.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=acc,
        tags={"anga", "prātipadika", "samasa_member", "krt"},
        meta={"upadesha_slp1": "kurucara", "corrected_v2_P005_A_kurucara_stem": True},
    )
    before = state.flat_slp1()
    state.terms = [merged]
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "P005-A-उपपद-कुरुचर",
            "form_before": before,
            "form_after": state.flat_slp1(),
            "why_dev": "कुरु + चर् + ट्-शेष → कुरुचर (संरचनात्मकम्)।",
            "status": "APPLIED",
        }
    )


def _merge_kurucarI_surface(state: State) -> None:
    """*kurucar* + *ī* → single prātipadika *kurucarī*."""
    if len(state.terms) < 2:
        return
    acc: list = []
    for t in state.terms:
        acc.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=acc,
        tags={
            "anga",
            "prātipadika",
            "strīliṅga",
            "corrected_v2_P005_A_kurucarI_demo",
        },
        meta={"upadesha_slp1": "kurucarI"},
    )
    before = state.flat_slp1()
    state.terms = [merged]
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "P005-A-कुरुचरी",
            "form_before": before,
            "form_after": state.flat_slp1(),
            "why_dev": "कुरुचर् + ई → कुरुचरी (संरचनात्मकम्)।",
            "status": "APPLIED",
        }
    )


def derive_kurucarI_upapada_corrected_P005_A() -> State:
    kuru = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kuru")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "kuru"},
    )
    ni = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Ni")),
        tags={"sup", "pratyaya", "upadesha"},
        meta={"upadesha_slp1": "Ni"},
    )
    car = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("car")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "car"},
    )
    s = State(terms=[kuru, ni, car], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P005_A_demo"] = True
    s.meta["corrected_v2_P005_A_upapada_frame"] = True

    s = apply_rule("1.3.1", s)

    s.meta["corrected_v2_P005_A_3_1_92_arm"] = True
    s = apply_rule("3.1.92", s)

    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s.meta["corrected_v2_P005_A_3_2_16_arm"] = True
    s = apply_rule("3.2.16", s)

    s.meta["2_2_19_upapada_atiNg_arm"] = True
    s = apply_rule("2.2.19", s)

    s = apply_rule("1.2.46", s)

    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    for sid in ("1.3.7", "1.3.9"):
        s = apply_rule(sid, s)

    _merge_kurucara(s)

    s.meta["corrected_v2_P005_A_kurucara_merged_1_2_46_arm"] = True
    s = apply_rule("1.2.46", s)

    s.meta["corrected_v2_P005_A_4_1_15_arm"] = True
    s = apply_rule("4.1.15", s)

    for sid in ("1.3.8", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    s = apply_rule("6.4.1", s)
    s = apply_rule("6.4.129", s)

    s.meta["corrected_v2_P005_A_6_4_148_arm"] = True
    s = apply_rule("6.4.148", s)

    _merge_kurucarI_surface(s)

    s = apply_rule("4.1.1", s)
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.2.41", s)

    s.meta["corrected_v2_P005_A_6_1_68_arm"] = True
    s = apply_rule("6.1.68", s)

    return s


__all__ = ["derive_kurucarI_upapada_corrected_P005_A"]
