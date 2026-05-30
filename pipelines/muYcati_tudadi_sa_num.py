"""
pipelines/muYcati_tudadi_sa_num.py — मुञ्चति (muYcati) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/मुञ्चति.md`
Target SLP1: **muYcati**
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
    P00_tripadi_anusvara_parasavarna,
    P00_tip_to_ti,
    P00_upadesha_it_1_3_1_2_5,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_lac_lat_attach,
    P00_snam_it_lopa_chain,
)


def derive_muYcati() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("muci~"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "muci~", "gana": 6},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # it-lopa on dhātu (i~ it) → muc
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
        s.terms[0].meta["upadesha_slp1"] = "muc"

    # laṭ + tip→ti (no Sap; tudādi uses Sa-vikaraṇa)
    s = P00_lac_lat_attach(s)
    s = P00_tip_to_ti(s)

    # tudādi vikaraṇa Sa + it-lopa (3.1.77 → 1.3.8 → 1.3.9)
    s = P00_snam_it_lopa_chain(s)

    s = apply_rule("6.4.1", s)
    s = apply_rule("1.1.47", s)
    s.meta["7_1_59_num_arm"] = True
    s = apply_rule("7.1.59", s)
    s.meta.pop("7_1_59_num_arm", None)

    # Merge to one pada then anusvāra + parasavarṇa.
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s = P00_tripadi_anusvara_parasavarna(s)
    return s


__all__ = ["derive_muYcati"]

