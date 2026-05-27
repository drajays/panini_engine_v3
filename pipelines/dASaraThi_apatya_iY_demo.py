"""
pipelines/dASaraThi_apatya_iY_demo.py — दाशरथि glass-box.

दशरथस्य अपत्यम् → दशरथ + इञ् → दाशरथि

Rule chain:
  4.1.82 (samartha adhikāra) → 4.1.92 (apatya adhikāra) → 4.1.95 (ata iñ)
  → P00_taddhita_it_lopa_chain (1.3.3/1.3.8/1.3.9/1.3.10 — lopos ñ, sets it_markers)
  → P00_vrddhi_prayoga_readiness → 1.4.13 → 6.4.1
  → 7.2.117 (taddhite ñit vṛddhi: a → ā)
  → 6.4.148 (yasyeti ca: final a lopa before i)
  → 1.1.60

Target SLP1: **dASaraTi** (दाशरथि).
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

from core.canonical_pipelines import (
    P00_taddhita_it_lopa_chain,
    P00_vrddhi_prayoga_readiness,
)


def _build_state() -> State:
    stem = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("daSaraTa"),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "daSaraTa"},
    )
    s = State(terms=[stem], meta={}, trace=[])
    return s


def derive_dASaraThi() -> State:
    s = _build_state()

    # Adhikāra setup: samarthā (4.1.82) → apatya (4.1.92)
    s = apply_rule("4.1.82", s)
    s = apply_rule("4.1.92", s)

    # Attach iñ by 4.1.95 (ata iñ — a-final in apatya context)
    s = apply_rule("4.1.95", s)

    # It-lopa: 1.3.3 recognises ñ (Y) as hal-antyam-it; 1.3.9 lopos it, records it_markers
    s = P00_taddhita_it_lopa_chain(s)

    # Aṅga-saṃjñā + aṅgasya adhikāra
    s = apply_rule("1.4.13", s)
    s = apply_rule("6.4.1", s)

    # Vṛddhi readiness paribhāṣā gates, then 7.2.117 taddhite ñit vṛddhi (a → ā)
    s = P00_vrddhi_prayoga_readiness(s)
    s = apply_rule("7.2.117", s)

    # 6.4.148 yasyeti ca: lopa of aṅgāntya 'a' before 'i' onset of iñ residue
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)

    s = apply_rule("1.1.60", s)
    return s


__all__ = ["derive_dASaraThi"]
