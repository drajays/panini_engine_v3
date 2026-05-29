"""
pipelines/yasAMsi_jas_shi_num.py — यशांसि (yasAMsi) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/यशांसि.md`
Target SLP1: **yasAMsi**
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected
# Structural merges recorded in State.trace · no gold shortcuts
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_jas_si_num_napumsaka
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_yasAMsi() -> State:
    stem = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("yasas"),
        tags={"anga", "prātipadika", "napuṃsaka"},
        meta={"upadesha_slp1": "yasas"},
    )
    s = State(terms=[stem], meta={"linga": "napuṃsaka", "vibhakti_vacana": "1-3"}, trace=[])

    s = P00_jas_si_num_napumsaka(s)
    s = apply_rule("6.4.10", s)  # a -> A before n+s

    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.24", s)  # n -> M before s
    return s


__all__ = ["derive_yasAMsi"]
