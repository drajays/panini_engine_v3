"""
pipelines/vandanIya_vad_anIyar.py — वन्दनीय glass-box.

वदिँ (अभिवादनस्तुत्योः, भ्वादिः) + अनीयर् → वन्दनीय

Rule chain:
  1.3.1 → 1.3.2 (i~ is anunāsika it) → 1.3.9 (lopa of i~) → vad [idit]
  1.1.47 → 7.1.58 (idit → nuṃ after last vowel) → vand
  3.1.91 (dhātoḥ kṛt context) → 3.1.96 (anIyar arm) → anIyar attached
  1.3.3 (r = hal-antyam it) → 1.3.9 (lopa of r) → anIya remains
  merge → vandanīya

Target SLP1: **vandanIya** (वन्दनीय)
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

from core.canonical_pipelines import P00_upadesha_it_1_3_1_2_5, P00_tavyat_anIyar_it_lopa, P00_idit_num_3_1_91
from pipelines.subanta import _pada_merge


def derive_vandanIya() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("vadi~"),
        tags={"dhatu", "anga", "upadesha", "idit"},
        meta={"upadesha_slp1": "vadi~", "gana": 1},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # it-lopa: anunāsika i~ → vad (idit tag pre-set)
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    s.terms[0].tags.discard("upadesha")
    s.terms[0].meta["upadesha_slp1"] = "vad"

    # 7.1.58 idito nuṃ dhātoḥ: insert n after last vowel → vand; then dhātoḥ
    s = P00_idit_num_3_1_91(s)
    s.meta["krtya_recipe"] = "anIyar"
    s = P00_tavyat_anIyar_it_lopa(s)

    # Structural merge → vandanīya
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    return s


__all__ = ["derive_vandanIya"]
