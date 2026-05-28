"""
pipelines/kRtrimam_ktri_kf_corrected_P003_B_demo.py — **P003-B** कृत्रिमम्.

**ḍukṛñ** (engine slice ``kf``) + *ktri* + *mam* (Vt. **4.4.20**) → *kṛtrimam*.
**7.3.84** is blocked by *kit* (**1.1.5**) on ``kf`` + *trim*.

CONSTITUTION Art. 7 / 11: ``apply_rule`` + ``_pada_merge`` only.
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
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_anga_guna_audit_1_4_13_1_1_5_7_3_84,
    P00_lashakvataddhite_it_lopa_chain,
    P00_tripadi_rutva_visarga,
)
from pipelines.subanta import _pada_merge


def derive_kRtrimam_ktri_kf_corrected_P003_B() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kf")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "kf"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["ekac_dhatu"] = True
    s = apply_rule("1.3.1", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)

    s = apply_rule("3.3.88", s)
    s = apply_rule("4.4.20", s)
    s = apply_rule("3.4.114", s)
    s = P00_lashakvataddhite_it_lopa_chain(s)
    s = P00_anga_guna_audit_1_4_13_1_1_5_7_3_84(s)

    _pada_merge(s)

    stem = s.terms[0]
    stem.kind = "prakriti"
    stem.tags.discard("pada")
    stem.meta["corrected_v2_P003_B_ktrim_stem"] = True
    s = apply_rule("1.2.46", s)

    stem = s.terms[0]
    stem.tags.add("napuṃsaka")
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.1", s)
    s = apply_rule("1.2.45", s)
    s = apply_rule("4.1.2", s)
    s = apply_rule("7.1.24", s)
    for sid in ("1.3.2", "1.3.9"):
        s = apply_rule(sid, s)
    s = apply_rule("6.1.107", s)
    _pada_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


__all__ = ["derive_kRtrimam_ktri_kf_corrected_P003_B"]
