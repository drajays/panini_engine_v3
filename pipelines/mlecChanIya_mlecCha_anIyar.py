"""
pipelines/mlecChanIya_mlecCha_anIyar.py — म्लेच्छनीय glass-box.

म्लेछँ (अव्यक्ते शब्दे, भ्वादिः, ०१.०२३३) + अनीयर् → म्लेच्छनीय

Rule chain:
  1.3.2 (a~ is anunāsika it) → 1.3.9 (lopa of a~) → mleC
  3.1.91 → 3.1.96 (anIyar arm) → mleC + anIyar
  1.3.3 (r = hal-antyam it) → 1.3.9 (lopa of r) → mleC + anIya
  6.1.75 (दीर्घात्: dīrgha 'e' before C → insert tuk 't') → mletC + anIya
  merge → mletCanIya
  8.2.1 → 8.4.40 (t+C → c) → mlecCanIya = म्लेच्छनीय

Target SLP1: **mlecCanIya** (म्लेच्छनीय)
"""
# ── Claude Code review 2026-05-28 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected
# Structural merges recorded in State.trace · no gold shortcuts
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_tavyat_anIyar_it_lopa
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from pipelines.subanta import _pada_merge


def derive_mlecChanIya() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("mleCa~"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "mleCa~", "gana": 1},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # it-lopa: anunāsika a~ → mleC
    s = apply_rule("1.3.1", s)
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.9", s)
    s.terms[0].tags.discard("upadesha")
    s.terms[0].meta["upadesha_slp1"] = "mleC"

    # kṛtya context + anīyar (krtya_recipe coordination key)
    s = apply_rule("3.1.91", s)
    s.meta["krtya_recipe"] = "anIyar"
    s = P00_tavyat_anIyar_it_lopa(s)

    # 6.1.75: dīrgha 'e' before C within dhātu → insert tuk 't' (→ mletC + anIya)
    s = apply_rule("6.1.75", s)

    # Merge then enter tripāḍī for ścutva
    _pada_merge(s)
    s = apply_rule("8.2.1", s)

    # 8.4.40 stoḥ ścunā ścuḥ: t+C → c (→ mlecCanIya = म्लेच्छनीय)
    s.meta["8_4_40_sto_tCh_arm"] = True
    s = apply_rule("8.4.40", s)
    return s


__all__ = ["derive_mlecChanIya"]
