"""
pipelines/pracChanIya_pracCha_anIyar_demo.py — प्रच्छनीय glass-box.

प्रछँ (ज्ञीप्सायाम्, तुदादिः, ०६.०१४९) + अनीयर् → प्रच्छनीय

Rule chain:
  1.3.2 (a~ is anunāsika it) → 1.3.9 (lopa of a~) → pracC
  3.1.91 → 3.1.96 (anIyar arm) → pracC + anIyar
  1.3.3 (r = hal-antyam it) → 1.3.9 (lopa of r) → pracC + anIya
  6.1.73 (छे च: hrasva 'a' before C within dhātu → insert tuk 't') → pratC + anIya
  merge → pratCanIya
  8.2.1 → 8.4.40 (stoḥ ścunā ścuḥ: t+C → c) → pracCanIya = प्रच्छनीय

Target SLP1: **pracCanIya** (प्रच्छनीय)
"""
# ── Claude Code review 2026-05-28 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected
# Structural merges recorded in State.trace · no gold shortcuts
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from pipelines.subanta import _pada_merge


def derive_pracChanIya() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("pracCa~"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "pracCa~", "gana": 6},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # it-lopa: anunāsika a~ → pracC
    s = apply_rule("1.3.1", s)
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.9", s)
    s.terms[0].tags.discard("upadesha")
    s.terms[0].meta["upadesha_slp1"] = "pracC"

    # kṛtya context + anīyar (krtya_recipe coordination key)
    s = apply_rule("3.1.91", s)
    s.meta["krtya_recipe"] = "anIyar"
    s = apply_rule("3.1.96", s)

    # it-lopa on anīyar 'r'
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    # 6.1.73: hrasva 'a' before C within dhātu → insert tuk 't' (→ pratC + anIya)
    s = apply_rule("6.1.73", s)

    # Merge then enter tripāḍī for ścutva
    _pada_merge(s)
    s = apply_rule("8.2.1", s)

    # 8.4.40 stoḥ ścunā ścuḥ: t+C → c (→ pracCanIya = प्रच्छनीय)
    s.meta["8_4_40_sto_tCh_arm"] = True
    s = apply_rule("8.4.40", s)
    return s


__all__ = ["derive_pracChanIya"]
