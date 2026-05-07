"""
pipelines/apajAnIte_lat_apa_jYA_corrected_P012_demo.py — **P012** अपजानीते.

``apa`` + **ज्ञा** (**``jYA``**) + laṭ ātmanepada 3 sg.: **3.1.81** *śnā*, **7.3.79**
*jnā*→*jā*, *ś*-lopa (**1.3.8**/**1.3.9**), **6.4.113**, **1.1.64**/**3.4.79** —
aligned with ``corrected_prakriyas_v2`` row **P012**.

**1.3.44** (*apahnava*) is commentary-only for this slice (recipe commits ātmanepada
via **3.4.79**).

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


def derive_apajAnIte_lat_apa_jYA_corrected_P012() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("jYA")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "jYA"},
    )
    s = State(terms=[dhatu], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P012_demo"] = True
    s.meta["lakara"] = "laT"

    s = apply_rule("1.3.1", s)

    apa = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("apa")),
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "apa"},
    )
    s.terms.insert(0, apa)

    s = apply_rule("1.4.59", s)

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

    s.meta["corrected_v2_P012_3_1_81_arm"] = True
    s = apply_rule("3.1.81", s)

    s.meta["corrected_v2_P012_7_3_79_arm"] = True
    s = apply_rule("7.3.79", s)

    for sid in ("1.3.8", "1.3.9"):
        s = apply_rule(sid, s)

    s.meta["corrected_v2_P012_6_4_113_arm"] = True
    s = apply_rule("6.4.113", s)

    s = apply_rule("1.1.64", s)
    s = apply_rule("3.4.79", s)

    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    return s


__all__ = ["derive_apajAnIte_lat_apa_jYA_corrected_P012"]
