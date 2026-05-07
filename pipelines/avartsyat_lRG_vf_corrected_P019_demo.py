"""
pipelines/avartsyat_lRG_vf_corrected_P019_demo.py — **P019** *avartsyat*.

**``vft``** (वृत्) + *lṛṅ* parasmaipada 3 sg.: **3.3.139**, **3.4.78** *tip*→*ti*,
**3.1.33** *sy*, **3.4.100**, **7.3.86** *ṛ*→*ar*, **6.4.71** *aṭ*, *pada* merge —
aligned with ``corrected_prakriyas_v2`` row **P019** (surface **``avartsyat``**).

CONSTITUTION Art. 7 / 11: ``apply_rule`` + ``_pada_merge`` only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_avartsyat_lRG_vf_corrected_P019() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("vft")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "vft"},
    )
    s = State(terms=[dhatu], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P019_demo"] = True
    s.meta["lakara"] = "lRG"

    s = apply_rule("1.3.1", s)

    s.meta["corrected_v2_P019_3_3_139_lRG_arm"] = True
    s = apply_rule("3.3.139", s)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "tip"
    s = apply_rule("3.4.78", s)

    for sid in ("1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    s.meta["corrected_v2_P019_3_1_33_sy_arm"] = True
    s = apply_rule("3.1.33", s)

    s = apply_rule("3.4.100", s)

    s.meta["corrected_v2_P019_vRt_guNa_arm"] = True
    s = apply_rule("7.3.86", s)
    s = apply_rule("1.1.51", s)

    s = apply_rule("6.4.71", s)

    for sid in ("1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    return s


__all__ = ["derive_avartsyat_lRG_vf_corrected_P019"]
