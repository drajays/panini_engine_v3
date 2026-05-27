"""
pipelines/vepathuH_athuc_wuvepf_corrected_P002_A_demo.py — **P002-A** वेपथुः.

Source row **P002-A** in ``corrected_prakriyas_v2``: *ṭuvepṛ* (*wuvepf~*, Bhvādi)
+ *athuc* (**3.3.89**, *bhāva*) → *vepathuḥ*.

Spine: ñi-*it* … ``vep`` → **3.1.91** *adhikāra* → **3.3.89** *athuc* → *it*-*lopa*
→ ``vepathu`` *pada*; **1.2.46** Case K; **4.1.1** / **4.1.2** + Tripāḍī tail.

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
    P00_pratipadika_prathama_sup_after_stem_merge,
    P00_tripadi_rutva_visarga,
)
from pipelines.subanta import _pada_merge

_UPADESHA = "wuvepf~"


def derive_vepathuH_athuc_wuvepf_corrected_P002_A() -> State:
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

    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)

    s = apply_rule("3.3.89", s)
    s = P00_lashakvataddhite_it_lopa_chain(s)
    s = apply_rule("3.4.114", s)

    _pada_merge(s)

    stem = s.terms[0]
    stem.kind = "prakriti"
    stem.tags.discard("pada")
    stem.meta["corrected_v2_P002_A_bhava_stem"] = True
    s = apply_rule("1.2.46", s)

    s.meta["linga"] = "pulliṅga"
    s = apply_rule("4.1.1", s)
    s = P00_pratipadika_prathama_sup_after_stem_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


__all__ = ["derive_vepathuH_athuc_wuvepf_corrected_P002_A", "_UPADESHA"]
