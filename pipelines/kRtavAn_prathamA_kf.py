"""
pipelines/kRtavAn_prathamA_kf.py — कृतवान् (*kf* + *ktavatu~*, prathamā-ekavacana).

Uses short-ṛ *upadeśa* ``kf`` (cf. ``raw_dhatu_after_it_lopa_slp1`` in
``data/inputs/dhatupatha_upadesha.json`` for *ḍukṛñ*) so *kit* blocks **7.3.84**
*guṇa* and the surface keeps *ṛ* (**kRtavAn**), matching common *Devanāgarī*
**कृतवान्**.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_ciY_ktavatu_nistha_prathama_tail,
    P00_kF_dhatu_bhuvadi,
    P00_ktavatu_kartari_nistha_opening,
)


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("kf"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "kf"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_kRtavAn() -> State:
    s = _build_state()
    s = P00_ktavatu_kartari_nistha_opening(
        s,
        target_upadesha_slp1="kf",
        dhatu_bootstrap=P00_kF_dhatu_bhuvadi,
    )
    s = P00_ciY_ktavatu_nistha_prathama_tail(s)
    return s


__all__ = ["derive_kRtavAn"]
