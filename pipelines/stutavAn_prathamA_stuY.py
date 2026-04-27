"""
pipelines/stutavAn_prathamA_stuY.py — स्तुतवान् (*stuñ* + *ktavatu~*, prathamā-ekavacana).

Target SLP1: **stutavAn**.  Same *ugit* / *vant* / *Tripāḍī* spine as *citavān*
(``P00_ciY_ktavatu_nistha_prathama_tail``); *dhātu* bootstrap is *Y*-final
``stuY`` (``P00_Yanta_hal_dhatu_it_then_bhuvadi``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_ciY_ktavatu_nistha_prathama_tail,
    P00_ktavatu_kartari_nistha_opening,
    P00_Yanta_hal_dhatu_it_then_bhuvadi,
)


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("stuY"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "stuY"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_stutavAn() -> State:
    s = _build_state()
    s = P00_ktavatu_kartari_nistha_opening(
        s,
        target_upadesha_slp1="stuY",
        dhatu_bootstrap=P00_Yanta_hal_dhatu_it_then_bhuvadi,
    )
    s = P00_ciY_ktavatu_nistha_prathama_tail(s)
    return s


__all__ = ["derive_stutavAn"]
