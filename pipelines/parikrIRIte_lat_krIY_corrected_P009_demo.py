"""
pipelines/parikrIRIte_lat_krIY_corrected_P009_demo.py — **P009** परिक्रीणीते.

``pari`` + *ḍukrīñ* (**``qukrIY``**) + laṭ ātmanepada 3 sg.: **3.1.81** *śnā*, *it*-lopa,
**6.4.113**, **3.4.79** *te*, tripāḍī **8.4.2** *ṇ*-tvam — aligned with
``corrected_prakriyas_v2`` row **P009**.

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


def derive_parikrIRIte_lat_krIY_corrected_P009() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("qukrIY")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "qukrIY"},
    )
    s = State(terms=[dhatu], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P009_demo"] = True
    s.meta["lakara"] = "laT"

    for sid in ("1.3.1", "1.3.5", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    dh = s.terms[0]
    dh.meta["upadesha_slp1"] = "krI"

    pari = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("pari")),
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "pari"},
    )
    s.terms.insert(0, pari)

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

    s = apply_rule("3.1.81", s)

    for sid in ("1.3.8", "1.3.9"):
        s = apply_rule(sid, s)

    s = apply_rule("6.4.113", s)

    s = apply_rule("1.1.64", s)
    s = apply_rule("3.4.79", s)

    s = apply_rule("8.2.1", s)
    s = apply_rule("8.4.2", s)

    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    return s


__all__ = ["derive_parikrIRIte_lat_krIY_corrected_P009"]
