"""
pipelines/medyati_lat_mid.py — मेद्यति (YimidA~, laṭ, 3sg parasmaipada) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/मेद्यति .md`.

Target SLP1: **medyati** (मेद्यति).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_lat_vartamane_tip_and_sap,
    P00_tip_to_ti,
    P00_upadesha_it_1_3_1_2_5,
    P00_lashakvataddhite_it_lopa_chain,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("YimidA~"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "YimidA~"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_medyati() -> State:
    s = _build_state()

    # it/lopa per note: 1.3.2 + 1.3.5 + 1.3.9 (ñi includes its vowel via our 1.3.5 hook).
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    # After dhātu it-lopa, we treat the term as "raw dhātu" (not upadeśa) so later
    # it-sūtras for pratyayas don't mistakenly target dhātu-final consonants.
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    # laṭ spine: adhikāra + laT + tip→ti + Sap
    s = P00_lat_vartamane_tip_and_sap(s)

    # divādi apavāda: Syan (3.1.69).
    s.meta["3_1_69_syan_arm"] = True
    s = apply_rule("3.1.69", s)

    # it-lopa on Syan → y (as per note).
    s = P00_lashakvataddhite_it_lopa_chain(s)

    # Aṅga saṃjñā
    s = apply_rule("1.4.13", s)

    # mider guṇaḥ: i→e (apavāda)
    s = apply_rule("7.3.82", s)

    # Structural merge for final rendering.
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    return s


__all__ = ["derive_medyati"]

