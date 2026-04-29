"""
pipelines/ruNaddhi_rudhadi_snam_demo.py — रुणद्धि (ruNaddhi) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/रुणद्धि .md`
Target SLP1: **ruRadDi**
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


def derive_ruRadDi() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ruDi~r"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "ruDi~r"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # upadeśa it-lopa (i~ + r) ⇒ ruD
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
        s.terms[0].meta["upadesha_slp1"] = "ruD"

    # laṭ + tip→ti (no Sap for rudhādi)
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

    # śnam infix (3.1.78) + 1.1.47 placement
    s = apply_rule("1.1.47", s)
    s.meta["3_1_78_snam_arm"] = True
    s = apply_rule("3.1.78", s)
    s.meta.pop("3_1_78_snam_arm", None)

    # Structural merge then Tripāḍī cascade per note:
    # 8.4.2 (n→R) → 8.2.40 (t→D) → 8.4.53 (D→d before D)
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.4.2", s)
    s = apply_rule("8.2.40", s)
    s = apply_rule("8.4.53", s)
    return s


__all__ = ["derive_ruRadDi"]

