"""
pipelines/muYcati_tudadi_sa_num_demo.py — मुञ्चति (muYcati) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/मुञ्चति.md`
Target SLP1: **muYcati**
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_tip_to_ti,
    P00_upadesha_it_1_3_1_2_5,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)


def derive_muYcati() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("muci~"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "muci~"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # it-lopa on dhātu (i~ it) → muc
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
        s.terms[0].meta["upadesha_slp1"] = "muc"

    # laṭ + tip→ti (no Sap; tudādi uses Sa-vikaraṇa)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.123", s)
    laT = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("laT"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    if laT.varnas and laT.varnas[-1].slp1 == "T":
        del laT.varnas[-1]
    s.terms.append(laT)
    s = P00_tip_to_ti(s)

    # tudādi vikaraṇa Sa, then num on muc before Sa.
    s.meta["3_1_77_sa_arm"] = True
    s = apply_rule("3.1.77", s)
    s.meta.pop("3_1_77_sa_arm", None)
    # it-lopa on Sa: laśakvataddhite (S it) → tasya lopaḥ.
    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.9", s)

    s = apply_rule("6.4.1", s)
    s = apply_rule("1.1.47", s)
    s.meta["7_1_59_num_arm"] = True
    s = apply_rule("7.1.59", s)
    s.meta.pop("7_1_59_num_arm", None)

    # Merge to one pada then anusvāra + parasavarṇa.
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.24", s)
    s = apply_rule("8.4.58", s)
    return s


__all__ = ["derive_muYcati"]

