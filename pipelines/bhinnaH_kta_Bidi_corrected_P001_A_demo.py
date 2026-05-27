"""
pipelines/bhinnaH_kta_Bidi_corrected_P001_A_demo.py — **P001-A** भिन्नः (*bhid* + *kta*).

Source row **P001-A** in the audited ``corrected_prakriyas_v2`` JSON bundle
(upstream file ``prakriya_01_*.json``).

Uses shared *kartari* *niṣṭhā* helpers through ``Bid`` + ``ta``, then narrow **8.2.42**
(*Bid*+*t* → *bhinna* stem) and **1.2.46** (bundle stem registration), then the usual
prathamā *su* tail (``P00_pratipadika_prathama_sup_after_stem_merge`` +
``P00_tripadi_rutva_visarga``).

CONSTITUTION Art. 7 / 11: ``apply_rule`` + permitted structural merges only.
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
    P00_anunasikadi_bhuvadi_dhatu_it_chain,
    P00_ciY_kartari_krt_nistha_adhikara_prefix,
    P00_krt_ardhadhatuka_ekac_it_and_guna_audit,
    P00_lashakvataddhite_it_lopa_chain,
    P00_pratipadika_prathama_sup_after_stem_merge,
    P00_tripadi_rutva_visarga,
)


def derive_bhinnaH_kta_Bidi_corrected_P001_A() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("Bidi~")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "Bidi~"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    s.meta["ekac_dhatu"] = True

    s = P00_anunasikadi_bhuvadi_dhatu_it_chain(s)
    s = P00_ciY_kartari_krt_nistha_adhikara_prefix(s)
    s.meta["3_2_102_target_upadesha_slp1"] = "Bidi~"
    s.meta["3_2_102_kta_arm"] = True
    s = apply_rule("3.2.102", s)
    s = P00_lashakvataddhite_it_lopa_chain(s)
    s = P00_krt_ardhadhatuka_ekac_it_and_guna_audit(s)

    s = apply_rule("8.2.42", s)

    s = apply_rule("1.2.46", s)

    s.meta["linga"] = "pulliṅga"
    s = P00_pratipadika_prathama_sup_after_stem_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


__all__ = ["derive_bhinnaH_kta_Bidi_corrected_P001_A"]
