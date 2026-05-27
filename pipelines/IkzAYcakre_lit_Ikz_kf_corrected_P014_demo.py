"""
pipelines/IkzAYcakre_lit_Ikz_kf_corrected_P014_demo.py — **P014** *īkṣāñcakre*.

``Ikz`` + periphrastic **ām** + **kṛñ** anuprayoga + *liṭ* *ātmanepada* 3 sg.,
aligned with ``corrected_prakriyas_v2`` row **P014** (target SLP1 **IkzAYcakre**).

CONSTITUTION Art. 7 / 11: ``apply_rule`` + ``_pada_merge`` only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_IkzAYcakre_lit_Ikz_kf_corrected_P014() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("Ikz")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "Ikz"},
    )
    s = State(terms=[dhatu], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P014_demo"] = True

    s = apply_rule("1.3.1", s)

    s.meta["3_2_115_paroksha_lit_arm"] = True
    s = apply_rule("3.2.115", s)

    s = apply_rule("3.1.36", s)

    s.meta["2_4_81_lit_luk_arm"] = True
    s = apply_rule("2.4.81", s)

    s = apply_rule("3.1.40", s)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.4.77", s)

    s = apply_rule("1.3.12", s)

    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "ta"
    s = apply_rule("3.4.78", s)

    s.meta["3_4_81_lit_esh_arm"] = True
    s = apply_rule("3.4.81", s)
    s = apply_rule("1.1.55", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    if s.terms and "pratyaya" in s.terms[-1].tags:
        s.terms[-1].meta["upadesha_slp1"] = "e"

    s = apply_rule("1.2.5", s)

    s.meta["6_1_8_lit_dvitva_arm"] = True
    s = apply_rule("6.1.8", s)
    s = apply_rule("6.1.4", s)

    for i, t in enumerate(s.terms):
        if "abhyasa" in t.tags:
            s.terms[i].meta["7_4_60_first_hal_only"] = True
            break

    s.meta["7_4_66_urat_abhyasa_arm"] = True
    s = apply_rule("7.4.66", s)
    s = apply_rule("1.1.51", s)
    s = apply_rule("7.4.60", s)

    s = apply_rule("7.4.62", s)

    s = apply_rule("6.1.77", s)

    for term in s.terms:
        if "dhatu" in term.tags:
            term.tags.add("aT_agama_context")
            break
    s = apply_rule("6.4.71", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.7", s)
    s = apply_rule("8.4.58", s)
    return s


__all__ = ["derive_IkzAYcakre_lit_Ikz_kf_corrected_P014"]
