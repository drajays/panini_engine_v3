"""
pipelines/bhinnavAn_prathamA_Bidi.py — भिन्नवान् (*bhid* + *ktavatu~*, prathamā-ekavacana).

*Viśeṣa:* **3.2.102** arms ``3_2_102_bhinn_before_tavat_arm`` (*Bid*→*Binn*),
then **6.1.111** drops the *t* onset of *tavat* so *Binn* + *avat* merges before
the usual *ugit* / *num* / *6.4.14* tail.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_anunasikadi_bhuvadi_dhatu_it_chain,
    P00_ciY_ktavatu_nistha_prathama_tail,
    P00_ktavatu_kartari_nistha_opening,
)


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("Bidi~"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "Bidi~"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_bhinnavAn() -> State:
    s = _build_state()
    s.meta["3_2_102_bhinn_before_tavat_arm"] = True
    s = P00_ktavatu_kartari_nistha_opening(
        s,
        target_upadesha_slp1="Bidi~",
        dhatu_bootstrap=P00_anunasikadi_bhuvadi_dhatu_it_chain,
    )
    s.meta["6_1_111_nn_t_lopa_arm"] = True
    s = P00_ciY_ktavatu_nistha_prathama_tail(s)
    return s


__all__ = ["derive_bhinnavAn"]
