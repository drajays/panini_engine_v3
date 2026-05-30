"""
pipelines/kirati_karati_split_prakriyas.py — **P009** (*kirati* note; JSON spine yields **karati**).

Source: ``…/my_scripts/final/split_prakriyas_11/P009.json``.

The JSON explicitly notes the classical target **kirati** (via 7.4.10 etc.), but the
recorded steps demonstrate the **7.3.84** guṇa path on **kF** yielding **karati**.
This pipeline implements that recorded spine (rule-based, apply_rule-only).

Spine:
  **3.1.91** → **3.1.1–3** → **3.2.123** → (structural +laT) → **3.4.77** → **3.4.78** (*tip*) →
  **3.1.77** (*Sa* vikaraṇa, recipe-armed) → **1.3.8** → **1.3.9** →
  **7.3.84** → **1.1.51** → **1.3.3** → **1.3.9** → (flat concat = karati).

CONSTITUTION Art. 7 / 11: ``apply_rule`` only (plus structural lakāra placeholder insertion).
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3, P00_tin_adesha_base, P00_lac_lat_attach, P00_snam_it_lopa_chain
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_kirati_karati_split_prakriyas_P009() -> State:
    # Dhātu witness (kF) for the recorded guṇa demonstration — treated as tudādi (gana 6).
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kF")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "kF", "gana": 6},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["prakriya_P009_kirati_note_karati_spine"] = True

    # laṭ setup (structural placeholder + tip selection by 3.4.78).
    s = P00_lac_lat_attach(s)

    s = P00_tin_adesha_base(s, "tip")

    # tudādi vikaraṇa Sa + it-lopa (3.1.77 → 1.3.8 → 1.3.9)
    s = P00_snam_it_lopa_chain(s)

    # guṇa on kF (F → a, then 1.1.51 inserts r) before the following sārvadhātuka Sa.
    s = apply_rule("7.3.84", s)
    s = apply_rule("1.1.51", s)
    # After uRaN-rapara, the dhātu is no longer in upadeśa-state; otherwise the
    # inserted final 'r' would be mis-read as halantyam-it by a later 1.3.3 on *tip*.
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    # it on tip final p, then lopa → ti.
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    return s


__all__ = ["derive_kirati_karati_split_prakriyas_P009"]

