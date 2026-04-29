"""
pipelines/Binatti_Cinatti_rudhadi_snam_demo.py

Implements the prakriyā from `भिनत्ति .md` (and parallel छिनत्ति note):
  - Binatti (Bid + Snam + laṭ 3sg) → Binatti
  - Cinatti (Cid + Snam + laṭ 3sg) → Cinatti
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


def _build_state(dhatu_upadesha_slp1: str) -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(dhatu_upadesha_slp1),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": dhatu_upadesha_slp1},
    )
    return State(terms=[dhatu], meta={}, trace=[])


def _lat_tip_no_sap(s: State) -> State:
    """
    laṭ 3sg kartari skeleton WITHOUT Sap (since rudhādi uses śnam vikaraṇa).
    """
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
    return s


def _derive(dhatu_upadesha_slp1: str) -> State:
    s = _build_state(dhatu_upadesha_slp1)

    # Upadeśa it-lopa (ñi/ṭu/ḍu etc.) if any; then tasya lopaḥ.
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    # laṭ spine: laT + tip→ti (NO Sap for rudhādi śnam).
    s = _lat_tip_no_sap(s)

    # Infix insertion of 'n' for śnam (rūdhādi) — modelled via 3.1.78 after 1.1.47.
    s = apply_rule("1.1.47", s)
    s.meta["3_1_78_snam_arm"] = True
    s = apply_rule("3.1.78", s)
    s.meta.pop("3_1_78_snam_arm", None)

    # Merge to single pada and apply Tripāḍī khari-ca (d→t before t).
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.4.55", s)
    return s


def derive_Binatti() -> State:
    return _derive("Bid")


def derive_Cinatti() -> State:
    return _derive("Cid")


__all__ = ["derive_Binatti", "derive_Cinatti"]

