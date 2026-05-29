"""
pipelines/ruNaddhi_rudhadi_snam.py — रुणद्धि (ruNaddhi) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/रुणद्धि .md`
Target SLP1: **ruRadDi**
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_tip_to_ti,
    P00_upadesha_it_1_3_1_2_5,
    P06a_pratyaya_adhikara_3_1_1_to_3,

    P00_lac_lat_attach,
    P00_snam_infix_8_2_1,
)


def derive_ruRadDi() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ruDi~r"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "ruDi~r"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # upadeśa it-lopa (i~ + r) ⇒ ruD
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
        s.terms[0].meta["upadesha_slp1"] = "ruD"

    # laṭ + tip→ti (no Sap for rudhādi)
    s = P00_lac_lat_attach(s)
    s = P00_tip_to_ti(s)

    s = P00_snam_infix_8_2_1(s)
    s = apply_rule("8.4.2", s)
    s = apply_rule("8.2.40", s)
    s = apply_rule("8.4.53", s)
    return s


__all__ = ["derive_ruRadDi"]

