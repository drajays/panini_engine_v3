"""
pipelines/mArzwi_lat_mFj.py — मार्ष्टि (mFjU~z, laṭ, 3sg parasmaipada) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/मार्ष्टि .md`.

Target SLP1: **mArzwi** (मार्ष्टि).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_lat_vartamane_tip_and_sap,
    P00_upadesha_it_anunasik_hal_lopa,
)


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("mFjU~z"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "mFjU~z"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_mArzwi() -> State:
    s = _build_state()

    # it/lopa on dhātu: nasal vowel + final z
    s = apply_rule("1.3.1", s)
    s = P00_upadesha_it_anunasik_hal_lopa(s)
    # After dhātu it-lopa, don't treat dhātu as upadeśa for later it-sūtras.
    s.terms[0].tags.discard("upadesha")

    # laṭ spine: adhikāra + laT + tip→ti + Sap
    s = P00_lat_vartamane_tip_and_sap(s)

    # adādi luk of Sap.
    s.meta["2_4_72_sap_luk_arm"] = True
    s = apply_rule("1.1.60", s)
    s = apply_rule("2.4.72", s)

    # Aṅga saṃjñā
    s = apply_rule("1.4.13", s)

    # mṛjeḥ vṛddhiḥ (ṛ → Ar) + uRaN-rapara.
    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.3", s)
    s = apply_rule("1.1.50", s)
    s = apply_rule("7.2.114", s)
    s = apply_rule("1.1.51", s)

    # Merge to one term, enter tripāḍī, then apply 8.2.36 and 8.4.40.
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.36", s)
    s = apply_rule("8.4.40", s)
    return s


__all__ = ["derive_mArzwi"]

