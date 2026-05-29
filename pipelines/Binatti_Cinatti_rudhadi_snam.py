"""
pipelines/Binatti_Cinatti_rudhadi_snam.py

Implements the prakriyā from `भिनत्ति .md` (and parallel छिनत्ति note):
  - Binatti (Bid + Snam + laṭ 3sg) → Binatti
  - Cinatti (Cid + Snam + laṭ 3sg) → Cinatti
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


def _build_state(dhatu_upadesha_slp1: str) -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(dhatu_upadesha_slp1),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": dhatu_upadesha_slp1},
    )
    return State(terms=[dhatu], meta={}, trace=[])


def _lat_tip_no_sap(s: State) -> State:
    """
    laṭ 3sg kartari skeleton WITHOUT Sap (since rudhādi uses śnam vikaraṇa).
    """
    s = P00_lac_lat_attach(s)
    s = P00_tip_to_ti(s)
    return s


def _derive(dhatu_upadesha_slp1: str) -> State:
    s = _build_state(dhatu_upadesha_slp1)

    # Upadeśa it-lopa (ñi/ṭu/ḍu etc.) if any; then tasya lopaḥ.
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    # laṭ spine: laT + tip→ti (NO Sap for rudhādi śnam).
    s = _lat_tip_no_sap(s)

    s = P00_snam_infix_8_2_1(s)
    s = apply_rule("8.4.55", s)
    return s


def derive_Binatti() -> State:
    return _derive("Bid")


def derive_Cinatti() -> State:
    return _derive("Cid")


__all__ = ["derive_Binatti", "derive_Cinatti"]

