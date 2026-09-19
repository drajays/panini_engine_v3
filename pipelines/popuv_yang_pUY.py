"""
pipelines/popuv_yang_pUY.py — पोपुवः (pUY, yaG, aC, prathamā-ekavacana) glass-box.

Same shape as ``pipelines/loluv_yang_lUY.py`` (लोलुवः, लू) — पू is an ऊ-अंत
क्र्यादि root of the identical phonological class, so the यङ्लुक् recipe
(अभ्यास, 2.4.74 यङ्-लुक्, 6.4.77 वुक्) carries over unchanged via the
shared ``P00_yang_luk_simple_dvitva_to_guna`` tail; only the धातु उपदेश
differs.

Target SLP1: **popuvaH** (पोपुवः), "one who purifies repeatedly."

Prakriyotsava sweep — यङ्लुक् mechanism family, item #4 of 9
(pp.601–602, पोपुव्).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_bhuvadi_dhatu_it_anunasik_hal,
    P00_subanta_prathama_su_tripadi_visarga,
    P00_yang_adhikara_yaG_append_sanadi,
    P00_yang_dvitva_abhyasa_gate,
    P00_yang_luk_simple_dvitva_to_guna,
)


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("pUY"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "pUY"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_popuvaH() -> State:
    s = _build_state()

    s = P00_bhuvadi_dhatu_it_anunasik_hal(s)
    s = P00_yang_adhikara_yaG_append_sanadi(s)
    s = P00_yang_dvitva_abhyasa_gate(s)
    s = P00_yang_luk_simple_dvitva_to_guna(s)
    s = P00_subanta_prathama_su_tripadi_visarga(s)
    return s


__all__ = ["derive_popuvaH"]
