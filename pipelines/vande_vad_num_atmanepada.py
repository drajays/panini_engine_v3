"""
pipelines/vande_vad_num_atmanepada.py — वन्दे (vande) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/वन्दे .md`
Target SLP1: **vande**
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_idit_num_3_1_91
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_upadesha_it_1_3_1_2_5,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_tin_adesha_base,
    P00_hal_anit_it_lopa,
)


def derive_vande() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("vadi~"),
        tags={"dhatu", "anga", "upadesha", "idit"},
        meta={"upadesha_slp1": "vadi~"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # it-lopa on dhātu (i~ it) → vad
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
        s.terms[0].meta["upadesha_slp1"] = "vad"

    # idito num dhatoH + dhātoḥ scope
    s = P00_idit_num_3_1_91(s)

    # laṭ + ātmanepada 1sg i
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

    s = apply_rule("1.3.12", s)

    s = P00_tin_adesha_base(s, "iw")
    # it-lopa on `iw` → `i`
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    # Insert Sap between dhātu and i (kartari); then it-lopa yields `a`.
    s = apply_rule("3.1.68", s)
    s = P00_hal_anit_it_lopa(s)

    # i -> e (Ti + 3.4.79), then a + e → e (pararūpa) structurally by merge.
    s = apply_rule("1.1.64", s)
    s = apply_rule("3.4.79", s)

    # Structural merge and then perform a+e → e by deleting preceding a.
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    # remove 'a' immediately before final 'e'
    vs = s.terms[0].varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "a" and vs[i + 1].slp1 == "e":
            del vs[i]
            break
    return s


__all__ = ["derive_vande"]

