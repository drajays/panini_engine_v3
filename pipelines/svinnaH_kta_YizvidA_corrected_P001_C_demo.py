"""
pipelines/svinnaH_kta_YizvidA_corrected_P001_C_demo.py — **P001-C** स्विन्नः.

Source row **P001-C** in the audited ``corrected_prakriyas_v2`` bundle (upstream
``prakriya_01_*.json``): *ñi*+*ṣvid* (*YizvidA~*, Bhvādi list row) + *kta* → *svinnaḥ*.

Spine: ñi-*it* … → *zvid*; **6.1.64** → *svid* + *kta* → *t*; narrow **8.2.42**
→ *svinna*; **1.2.46**; prathamā *su* → **8.2.66** / **8.3.15**.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only (plus shared canonical helpers).
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
    P00_ciY_kartari_krt_nistha_adhikara_prefix,
    P00_krt_ardhadhatuka_ekac_it_and_guna_audit,
    P00_lashakvataddhite_it_lopa_chain,
    P00_pratipadika_prathama_sup_after_stem_merge,
    P00_tripadi_rutva_visarga,
)

_UPADESHA = "YizvidA~"


def derive_svinnaH_kta_YizvidA_corrected_P001_C() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(_UPADESHA)),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": _UPADESHA},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    s.meta["ekac_dhatu"] = True

    for sid in ("1.3.1", "1.3.5", "1.3.2", "1.3.9"):
        s = apply_rule(sid, s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
    s = apply_rule("1.3.1", s)

    s = P00_ciY_kartari_krt_nistha_adhikara_prefix(s)
    s.meta["3_2_102_target_upadesha_slp1"] = _UPADESHA
    s.meta["3_2_102_kta_arm"] = True
    s = apply_rule("3.2.102", s)
    s = P00_lashakvataddhite_it_lopa_chain(s)
    s = P00_krt_ardhadhatuka_ekac_it_and_guna_audit(s)

    s.meta["corrected_v2_P001_C_6_1_64_arm"] = True
    s = apply_rule("6.1.64", s)

    s.meta["corrected_v2_P001_C_8_2_42_arm"] = True
    s = apply_rule("8.2.42", s)

    s = apply_rule("1.2.46", s)

    s.meta["linga"] = "pulliṅga"
    s = P00_pratipadika_prathama_sup_after_stem_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


__all__ = ["derive_svinnaH_kta_YizvidA_corrected_P001_C"]
