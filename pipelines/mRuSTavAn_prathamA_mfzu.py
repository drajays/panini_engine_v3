"""
pipelines/mRuSTavAn_prathamA_mfzu.py — मृष्टवान् (*mṛṣ* + *ktavatu~*, prathamā-ekavacana).

*Viśeṣa:* **8.4.40** (*z*+*t* → *z*+*w*, i.e. *ṣ*+*ṭ*) runs on the merged stem
before *Tripāḍī* via ``ktavatu_mfz_stuta_arm`` (see ``sutra_8_4_40``).
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
        varnas=parse_slp1_upadesha_sequence("mfzu~"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "mfzu~"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_mRuSTavAn() -> State:
    s = _build_state()
    s = P00_ktavatu_kartari_nistha_opening(
        s,
        target_upadesha_slp1="mfzu~",
        dhatu_bootstrap=P00_anunasikadi_bhuvadi_dhatu_it_chain,
    )
    s.meta["ktavatu_mfz_stuta_arm"] = True
    s = P00_ciY_ktavatu_nistha_prathama_tail(s)
    return s


__all__ = ["derive_mRuSTavAn"]
