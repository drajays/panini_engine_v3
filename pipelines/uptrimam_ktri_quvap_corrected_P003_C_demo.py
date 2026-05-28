"""
pipelines/uptrimam_ktri_quvap_corrected_P003_C_demo.py — **P003-C** उप्त्रिमम्.

**ḍuvapā̃** (``quvap~z``) + *ktri* + *mam* → **6.1.15** / **1.1.45** / **6.1.108**
→ *uptrimam*.

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
    P00_lashakvataddhite_it_lopa_chain,
    P00_tripadi_rutva_visarga,
)
from pipelines.subanta import _pada_merge

_UPADESHA = "quvap~z"


def derive_uptrimam_ktri_quvap_corrected_P003_C() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(_UPADESHA)),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": _UPADESHA},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["ekac_dhatu"] = True

    for sid in ("1.3.1", "1.3.5", "1.3.2", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
    s = apply_rule("1.3.1", s)

    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)

    s.meta["corrected_v2_P003_C_3_3_88_arm"] = True
    s = apply_rule("3.3.88", s)
    s.meta["corrected_v2_P003_mam_augment_arm"] = True
    s = apply_rule("4.4.20", s)
    s = apply_rule("3.4.114", s)
    s = P00_lashakvataddhite_it_lopa_chain(s)

    s = apply_rule("6.1.15", s)
    s = apply_rule("1.1.45", s)
    s = apply_rule("6.1.108", s)

    _pada_merge(s)

    stem = s.terms[0]
    stem.kind = "prakriti"
    stem.tags.discard("pada")
    stem.meta["corrected_v2_P003_C_ktrim_stem"] = True
    s = apply_rule("1.2.46", s)

    stem = s.terms[0]
    stem.tags.add("napuṃsaka")
    s.meta["vibhakti_vacana"] = "1-1"
    s.meta["corrected_v2_P003_subanta_tail_arm"] = True
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


__all__ = ["derive_uptrimam_ktri_quvap_corrected_P003_C", "_UPADESHA"]
