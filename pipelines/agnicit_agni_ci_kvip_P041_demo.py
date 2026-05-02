"""
pipelines/agnicit_agni_ci_kvip_P041_demo.py — P041 (अग्निचित्)

Source: ``split_prakriyas_11/P041.json``.

Target SLP1: ``agnicit`` — *agni* + *√ci* + *kvip* (*upapada* *kṛt*), *it*-*lopa* on
*kvip*, **6.1.67** (*kvip* ``vi`` residue), structural empty *kvip* removal, **1.1.60**/**1.1.61**,
**1.1.62**, **1.1.5** (*kṅiti* note after *kit*), **7.3.86**
(skip), **1.1.46**, **6.1.71** (*tuk*), structural *upapada* merge, *subanta*
*su* + **6.1.68**, **8.2.30** (no change here), **1.1.68**.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_lashakvataddhite_it_lopa_chain, P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _p041_remove_empty_kvip(state: State) -> None:
    """Remove emptied ``kvip`` ``Term`` after **1.3** *it*-*lopa* (not a sūtra)."""
    removed = False
    new_terms = []
    for t in state.terms:
        if (t.meta.get("upadesha_slp1") or "").strip() == "kvip" and not t.varnas:
            removed = True
            continue
        new_terms.append(t)
    if not removed:
        return
    b = state.flat_slp1()
    state.terms = new_terms
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "क्विप्-शेष-लोपः",
            "form_before": b,
            "form_after": state.flat_slp1(),
            "why_dev": "क्विप्-प्रत्ययस्य सर्व-वर्ण-लोपानन्तरम् अपसारणम् (P041)।",
            "status": "APPLIED",
        }
    )


def _p041_merge_agni_cit(state: State) -> None:
    """``agni`` + ``ci`` + ``t`` → ``agnicit`` (one *prātipadika* ``Term``)."""
    if len(state.terms) < 2:
        return
    acc: list = []
    for t in state.terms:
        acc.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=acc,
        tags={"anga", "prātipadika", "pulliṅga", "P041_agnicit_demo"},
        meta={"upadesha_slp1": "agnicit"},
    )
    b = state.flat_slp1()
    state.terms = [merged]
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "उपपद-क्विप्-मेलनम्",
            "form_before": b,
            "form_after": state.flat_slp1(),
            "why_dev": "अग्नि + चित् → अग्निचित् (संरचनात्मकं, P041)।",
            "status": "APPLIED",
        }
    )


def derive_agnicit_agni_ci_kvip_P041() -> State:
    agni = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("agni")),
        tags={"anga", "upasarjana"},
        meta={"upadesha_slp1": "agni"},
    )
    ci = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("ci")),
        tags={"dhatu", "anga", "P041_ci_dhatu"},
        meta={"upadesha_slp1": "ci"},
    )
    s = State(terms=[agni, ci], meta={}, trace=[], samjna_registry={})

    s = apply_rule("1.1.68", s)

    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s.meta["3_2_76_kvip_arm"] = True
    s = apply_rule("3.2.76", s)

    s.meta["P041_3_2_91_arm"] = True
    s = apply_rule("3.2.91", s)

    s = P00_lashakvataddhite_it_lopa_chain(s)
    # ``kvip`` may leave a ``vi`` / ``v`` residue (**6.1.67**, same motor as *prakriya_22*).
    s.meta["prakriya_22_kvip_residue_arm"] = True
    s = apply_rule("6.1.67", s)
    _p041_remove_empty_kvip(s)

    s = apply_rule("1.1.60", s)
    s = apply_rule("1.1.61", s)

    s = apply_rule("1.1.62", s)

    s.meta["P041_record_kngiti_arm"] = True
    s = apply_rule("1.1.5", s)

    s = apply_rule("7.3.86", s)

    s = apply_rule("1.1.46", s)

    s.meta["P041_6_1_71_tuk_arm"] = True
    s = apply_rule("6.1.71", s)

    _p041_merge_agni_cit(s)

    s = apply_rule("4.1.1", s)
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.2.41", s)

    s.meta["P041_6_1_68_arm"] = True
    s = apply_rule("6.1.68", s)

    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.30", s)

    s.meta.pop("1_1_68_svadrupa_audit_done", None)
    s = apply_rule("1.1.68", s)
    return s


__all__ = ["derive_agnicit_agni_ci_kvip_P041"]
