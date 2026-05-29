"""
pipelines/paTayati_paTu_Nic.py — P025 (*paṭayति*)

Source: ``…/my_scripts/final/split_prakriyas_11/P025.json``.

Target SLP1: ``paTayati`` — *paṭu* + *ṇic* (*vārttika* frame under **2.1.26**),
*ṭi*-lopa (**6.4.155**), *paribhāṣā* **1.1.57**, then *laṭ* *kartari* spine with
*śap* (**3.1.68**) and *tip* (**3.4.78**), **7.3.84** + **6.1.78**.

Structural merge (``__MERGE__``) joins *paṭ* + *ṇic* residue ``i`` into one *dhātu*
``paTi`` so **7.3.84** can see an *ik*-final *aṅga* before *śap*’s ``a``.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3, P00_krt_it_lopa, P00_tin_adesha_base, P00_lac_lat_attach
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _merge_paT_nic_i_to_paTi(state: State) -> None:
    """Structural: ``paT`` + ``i`` → ``paTi`` (one *dhātu* ``Term``)."""
    if len(state.terms) < 2:
        return
    a, b = state.terms[0], state.terms[1]
    merged = Term(
        kind="prakriti",
        varnas=list(a.varnas) + list(b.varnas),
        tags={"dhatu", "anga", "prātipadika"},
        meta={"upadesha_slp1": "paTi"},
    )
    state.terms = [merged] + state.terms[2:]
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "धातु-मेलनम्",
            "form_before": state.flat_slp1(),
            "form_after": state.flat_slp1(),
            "why_dev": "पट् + णिच्-अवशेष-इकारः → पटि (एक-धातु-टर्म्, P025)।",
            "status": "APPLIED",
        }
    )


def derive_paTayati_paTu_Nic_P025() -> State:
    paTu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("paTu")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "paTu"},
    )
    s = State(terms=[paTu], meta={}, trace=[], samjna_registry={})

    s = apply_rule("1.1.68", s)
    s = apply_rule("1.2.45", s)

    s.meta["vibhakti_vacana"] = "2-1"
    s = apply_rule("4.1.2", s)

    s.meta["P025_2_1_26_Nic_arm"] = True
    s = apply_rule("2.1.26", s)

    s = P00_krt_it_lopa(s)

    s.meta["P025_3_1_32_arm"] = True
    s = apply_rule("3.1.32", s)

    s.meta["P025_6_4_155_Ti_lopa_arm"] = True
    s = apply_rule("6.4.155", s)

    s = apply_rule("1.1.57", s)
    s = apply_rule("7.2.116", s)

    _merge_paT_nic_i_to_paTi(s)

    s = P00_lac_lat_attach(s)

    s.meta["3_1_68_kartari_recipe"] = True
    s = P00_tin_adesha_base(s, "tip")

    s = apply_rule("3.1.68", s)
    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    s = apply_rule("7.3.84", s)
    s = apply_rule("6.1.78", s)

    s.meta.pop("1_1_68_svadrupa_audit_done", None)
    s = apply_rule("1.1.68", s)
    return s


__all__ = ["derive_paTayati_paTu_Nic_P025"]
