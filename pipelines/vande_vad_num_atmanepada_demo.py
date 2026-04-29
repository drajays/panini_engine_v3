"""
pipelines/vande_vad_num_atmanepada_demo.py — वन्दे (vande) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/वन्दे .md`
Target SLP1: **vande**
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_upadesha_it_1_3_1_2_5,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)


def derive_vande() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("vadi~"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "vadi~"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # it-lopa on dhātu (i~ it) → vad
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
        s.terms[0].meta["upadesha_slp1"] = "vad"

    # idito num dhatoH
    s = apply_rule("1.1.47", s)
    s.meta["7_1_58_num_arm"] = True
    s = apply_rule("7.1.58", s)
    s.meta.pop("7_1_58_num_arm", None)

    # laṭ + ātmanepada 1sg i
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

    s.meta["1_3_12_arm"] = True
    s = apply_rule("1.3.12", s)
    s.meta.pop("1_3_12_arm", None)

    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = s.meta.pop("tin_adesha_for_vande")
    s = apply_rule("3.4.78", s)
    # it-lopa on `iw` → `i`
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    # Insert Sap between dhātu and i (cartari); then it-lopa yields `a`.
    s.meta["3_1_68_kartari_recipe"] = True
    s = apply_rule("3.1.68", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.9", s)

    # i -> e (Ti + 3.4.79), then a + e → e (pararūpa) structurally by merge.
    s = apply_rule("1.1.64", s)
    s = apply_rule("3.4.79", s)

    # Structural merge and then perform a+e → e by deleting preceding a.
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    # remove 'a' immediately before final 'e'
    vs = s.terms[0].varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "a" and vs[i + 1].slp1 == "e":
            del vs[i]
            break
    return s


__all__ = ["derive_vande"]

