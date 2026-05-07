"""
pipelines/upasarajaH_upapada_corrected_P005_B_demo.py — **P005-B** उपसरजः.

``upasara`` + सप्तमी *Ni* + *√jan~* + **ḍa** (**3.2.97**) → internal *sup* *luk*
(**2.4.71**), *cuṭū* + *it*-*lopa* on **qa**, **6.4.143** (*jan* → ``j`` before *ḍit*
``a``), structural merge **upasaraja**, then standard *subanta* prathamā *eka*
with tripāḍī **8.2.66** / **8.3.15** → ``upasarajaH``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` + documented structural merges only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P01_subanta_bootstrap,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    run_subanta_sup_attach_and_finish,
)
from engine import apply_rule
from engine.lopa_ghost import term_is_sup_luk_ghost
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _merge_upasaraja(state: State) -> None:
    """Concatenate *upasara* + *j* + *a* (skip **2.4.71** ghosts)."""
    acc: list = []
    for t in state.terms:
        if term_is_sup_luk_ghost(t):
            continue
        acc.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=acc,
        tags={"anga", "prātipadika", "samasa_member", "krt", "pulliṅga"},
        meta={"upadesha_slp1": "upasaraja", "corrected_v2_P005_B_upasaraja_stem": True},
    )
    before = state.flat_slp1()
    state.terms = [merged]
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "P005-B-उपपद-उपसरज",
            "form_before": before,
            "form_after": state.flat_slp1(),
            "why_dev": "उपसर + ज् + अ → उपसरज (संरचनात्मकम्)।",
            "status": "APPLIED",
        }
    )


def derive_upasarajaH_upapada_corrected_P005_B() -> State:
    upasara = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("upasara")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "upasara"},
    )
    ni = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Ni")),
        tags={"sup", "pratyaya", "upadesha"},
        meta={"upadesha_slp1": "Ni"},
    )
    jan = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("jan~")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "jan~"},
    )
    s = State(terms=[upasara, ni, jan], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P005_B_demo"] = True
    s.meta["corrected_v2_P005_B_upapada_frame"] = True

    s = apply_rule("1.3.1", s)

    s.meta["corrected_v2_P005_B_3_1_92_arm"] = True
    s = apply_rule("3.1.92", s)

    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s = apply_rule("1.3.2", s)
    s.meta["corrected_v2_P005_B_3_2_97_arm"] = True
    s = apply_rule("3.2.97", s)
    # *jan~* **1.3.3** (*hal* on ``n``) + **1.3.9** (*anunāsika* vowel *it* slice).
    for sid in ("1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    s.meta["2_2_19_upapada_atiNg_arm"] = True
    s = apply_rule("2.2.19", s)

    s = apply_rule("1.2.46", s)

    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    for sid in ("1.3.7", "1.3.9"):
        s = apply_rule(sid, s)

    s.meta["corrected_v2_P005_B_6_4_143_arm"] = True
    s = apply_rule("6.4.143", s)

    _merge_upasaraja(s)

    s.meta["corrected_v2_P005_B_upasaraja_merged_1_2_46_arm"] = True
    s = apply_rule("1.2.46", s)

    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s = P01_subanta_bootstrap(s)
    s = run_subanta_sup_attach_and_finish(s)

    return s


__all__ = ["derive_upasarajaH_upapada_corrected_P005_B"]
