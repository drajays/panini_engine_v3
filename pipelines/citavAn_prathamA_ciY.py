"""
pipelines/citavAn_prathamA_ciY.py — चितवान् (*ciñ* + *ktavatu~*, prathamā-ekavacana).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/चितवान्.md``

Target SLP1: **citavAn** (चितवान्).  Scheduling is ``apply_rule`` only (CONSTITUTION
Art. 7 / 11).  *Tripāḍī* opens only after *sup* / *num* / *6.4.14* / *6.1.68* so
non–8.x rules are not *asiddha*-blocked (**8.2.1** gate).

The *sub* tail (``4.1.2`` … ``8.2.23``) lives in
``core.canonical_pipelines.P00_ciY_ktavatu_nistha_prathama_tail`` to satisfy the
duplicate scheduling auditor.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_ciY_dhatu_hal_it_then_bhuvadi,
    P00_ciY_ktavatu_nistha_prathama_tail,
    P00_ktavatu_kartari_nistha_opening,
)


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ciY"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "ciY"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_citavAn() -> State:
    s = _build_state()
    s = P00_ktavatu_kartari_nistha_opening(
        s,
        target_upadesha_slp1="ciY",
        dhatu_bootstrap=P00_ciY_dhatu_hal_it_then_bhuvadi,
    )
    s = P00_ciY_ktavatu_nistha_prathama_tail(s)
    return s


__all__ = ["derive_citavAn"]
