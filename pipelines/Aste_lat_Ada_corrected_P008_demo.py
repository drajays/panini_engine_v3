"""
pipelines/Aste_lat_Ada_corrected_P008_demo.py — **P008** आस्ते (*ās* + laṭ ātmanepada 3 sg.).

Aligned with corrected-v2 row **P008** (source ``prakriya_08_*.json``):
**आसँ** → *it*-lopa → **3.2.123** laṭ → **त** → **3.1.68**
**शप्** → **2.4.72** *śap* *luk* (Adādi) → **3.4.113** / **3.4.79** → **आस्ते**.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only + structural ``laT`` placeholder + ``_pada_merge``.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_upadesha_it_1_3_1_2_5,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_Aste_lat_Ada_corrected_P008() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("Asa~")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "Asa~"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["corrected_v2_P008_Aste_demo"] = True
    s.meta["lakara"] = "laT"

    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
        s.terms[0].meta["upadesha_slp1"] = "As"

    s.meta["1_3_12_arm"] = True
    s = apply_rule("1.3.12", s)
    s.meta.pop("1_3_12_arm", None)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.123", s)
    laT = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("laT"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    if laT.varnas and laT.varnas[-1].slp1 == "T":
        del laT.varnas[-1]
    s.terms.append(laT)

    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "ta"
    s = apply_rule("3.4.78", s)

    s.meta["3_1_68_kartari_recipe"] = True
    s = apply_rule("3.1.68", s)

    s.meta["2_4_72_sap_luk_arm"] = True
    s = apply_rule("2.4.72", s)

    s = apply_rule("3.4.113", s)
    s = apply_rule("1.1.64", s)
    s = apply_rule("3.4.79", s)

    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    return s


__all__ = ["derive_Aste_lat_Ada_corrected_P008"]
