"""
pipelines/akurvAtAm_laG_tanadi_kf.py — **P020** (**अकुर्वाताम्**).

Source: ``…/my_scripts/final/split_prakriyas_11/P020.json``.

The JSON notes the OCR target ``akurutAm`` is wrong; the recorded derivation yields
**akurvAtAm** (laṅ, prathamā-dvivacana ātmanepada of *kf* in this narrow tanādi-u demo).

Spine (apply_rule only):
  **3.2.111** (laṅ placeholder, armed) → **3.4.77** → **3.4.78** (AtAm) →
  **3.1.79** (tanādi u) → **7.3.84** → **1.1.51** →
  **6.1.77** (armed general boundary: u + A → v + A) →
  **1.2.4** → **1.1.5** → **6.4.110** →
  **6.1.77** (armed again: u + A → v + A) →
  **6.4.71** (aṭ augment for laṅ).

CONSTITUTION Art. 7 / 11: apply_rule only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3, P00_tin_adesha_base, P00_tanadi_u_guna
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_akurvAtAm_laG_tanadi_kf_P020() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kf")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "kf"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["prakriya_P020_akurvAtAm_split_prakriyas_11"] = True
    s.meta["lakara"] = "laG"

    s = apply_rule("3.2.111", s)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s = P00_tin_adesha_base(s, "AtAm")
    s.meta["3_1_79_tanadi_u_arm"] = True
    s = P00_tanadi_u_guna(s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
    s = apply_rule("1.2.4", s)
    s = apply_rule("1.1.5", s)
    s = apply_rule("6.4.110", s)

    # kuru + AtAm → kurvAtAm (general arm across terms)
    s = apply_rule("6.1.77", s)

    # aṭ augment for laṅ
    s = apply_rule("6.4.71", s)
    return s


__all__ = ["derive_akurvAtAm_laG_tanadi_kf_P020"]

