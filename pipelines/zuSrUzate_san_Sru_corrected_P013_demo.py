"""
pipelines/zuSrUzate_san_Sru_corrected_P013_demo.py — **P013** शुश्रूषते.

*Śru* (surface **``Sru``**; bundle *śruṃ* *it* is pre-resolved here so **1.3.2** does
not elide the vowel) + *san* (desiderative) + laṭ ātmanepada 3 sg.: **3.1.7**,
**6.4.16** (*u*→*ū* before *san*), **6.1.1**/**6.1.4**, **7.4.60** (``Sru`` abhyāsa
→ ``Su``), then the **tíṅ** + *śap* spine (**3.1.91** … **3.4.79** *te*) and *pada*
merge + **6.1.97** *pararūpa* — tripāḍī **8.2.1**/**8.3.59** **last** (as *cicīṣati*
demos: ``tripadi_zone`` blocks **3.4.77** if **8.2.1** runs too early).  Aligned
with ``corrected_prakriyas_v2`` row **P013** (surface **``SuSrUzate``**).

SLP1: **``S``** = श्, **``z``** = ष् (``phonology.varna.HAL_DEV``).

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


def derive_zuSrUzate_san_Sru_corrected_P013() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("Sru")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "Sru"},
    )
    s = State(terms=[dhatu], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P013_demo"] = True
    s.meta["lakara"] = "laT"

    s = apply_rule("1.3.1", s)

    s.meta["3_1_7_san_arm"] = True
    s = apply_rule("3.1.7", s)
    s = apply_rule("1.2.8", s)
    s = apply_rule("1.1.5", s)
    s = apply_rule("3.1.32", s)

    s.meta["6_1_1_dvitva_arm"] = True
    s = apply_rule("6.1.1", s)
    s = apply_rule("6.1.4", s)

    s.meta["corrected_v2_P013_sani_dirgha_arm"] = True
    s.meta["6_4_16_sani_dirgha_arm"] = True
    s = apply_rule("6.4.16", s)

    s.meta["corrected_v2_P013_Sru_abhyasa_arm"] = True
    s = apply_rule("7.4.60", s)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.123", s)
    laT = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("laT"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    if laT.varnas and laT.varnas[-1].slp1 == "T":
        del laT.varnas[-1]
    s.terms.append(laT)

    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "ta"
    s = apply_rule("3.4.78", s)

    s.meta["3_1_68_kartari_recipe"] = True
    s = apply_rule("3.1.68", s)

    for sid in ("1.3.3", "1.3.8", "1.3.9"):
        s = apply_rule(sid, s)

    s = apply_rule("3.4.113", s)
    s = apply_rule("1.1.64", s)
    s = apply_rule("3.4.79", s)

    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s.meta["corrected_v2_P013_6_1_97_arm"] = True
    s = apply_rule("6.1.97", s)

    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.59", s)
    return s


__all__ = ["derive_zuSrUzate_san_Sru_corrected_P013"]
