"""
pipelines/loluv_yang_lUY.py — लोलुवः (lUY, yaG, aC, prathamā-ekavacana) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/loluv.md`

Target SLP1: **loluvH** (लोलुवः).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_bhuvadi_dhatu_it_anunasik_hal,
    P00_subanta_prathama_su_tripadi_visarga,
    P00_yang_ac_three_term_frame,
    P00_yang_adhikara_yaG_append_sanadi,
    P00_yang_dvitva_abhyasa_gate,
    P00_yang_luk_2_4_74_and_1_1_4,
)


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("lUY"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "lUY"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_loluvH() -> State:
    s = _build_state()

    s = P00_bhuvadi_dhatu_it_anunasik_hal(s)
    s = P00_yang_adhikara_yaG_append_sanadi(s)
    s = P00_yang_dvitva_abhyasa_gate(s)
    s = apply_rule("7.4.60", s)
    s = apply_rule("7.4.82", s)
    s = P00_yang_ac_three_term_frame(s)
    s = P00_yang_luk_2_4_74_and_1_1_4(s)
    s = apply_rule("7.3.84", s)
    s = apply_rule("6.4.77", s)
    s = P00_subanta_prathama_su_tripadi_visarga(s)
    return s


__all__ = ["derive_loluvH"]
