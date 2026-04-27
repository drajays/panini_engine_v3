"""
*pra*+*ni*+**deN** (रक्षणे) *laf* 3*sg* ātmane **dayate** — **8.4.17** (प्रणिदयते).

The note
``…/my panini notes/प्रणिदयते'.md`` (file name may use U+2019) traces **1.3.12** ātmanepada,
**3.4.78**/**3.4.79** *te*, **3.1.68** *śap*, **6.1.78** *d e*+**a** (after *lopa* **de**)
→ **d ay a te**, **1.1.20** *ghu* for *de* under **6.1.45** *dā* class, **8.4.17** *ner*.

v3: no **1.3.12** / **3.4** / **6.1.78** *vidhi* in this file — the *āpta* row is **dayate** with
``upadesha_slp1`` = ``de~N`` (``1.1.20`` *ghu* set, extended for *E*-ādeśa *dā*/*dhā* *śākhā*).
**1.1.56** is recorded for the note’s *sthānivad* *corpus*; **8.4.17** still keys off *ghu*+upadeśa.

*Śruti target (SLP1):* **praRidayate** (ण् = ``R``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_20 import (
    dhatu_upadesha_slp1_is_ghu,
    ghu_samjna_is_registered,
)


def _make_pra_ni_dayate_terms() -> tuple[Term, Term, Term]:
    pra = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("pra"),
        tags={"upasarga", "anga"},
        meta={},
    )
    ni = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ni"),
        tags={"upasarga", "anga"},
        meta={},
    )
    dayate = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("dayate"),
        tags={"dhatu", "anga", "upadesha"},
        meta={
            "upadesha_slp1": "de~N",
        },
    )
    return (pra, ni, dayate)


def build_pra_ni_dayate_ghu_state() -> State:
    pra, ni, d = _make_pra_ni_dayate_terms()
    s = State(terms=[pra, ni, d], meta={}, trace=[])
    s = apply_rule("1.1.20", s)
    if not ghu_samjna_is_registered(s):
        raise RuntimeError("1.1.20 ghu set not registered (unexpected)")
    u = s.terms[2].meta.get("upadesha_slp1", "")
    if not dhatu_upadesha_slp1_is_ghu(s, u):
        raise RuntimeError("demo dhātu upadeśa must be ghu (de~N)")
    s = apply_rule("1.1.56", s)
    if s.paribhasha_gates.get("sthanivadbhava") is not True:
        raise RuntimeError("1.1.56 (unexpected)")
    return s


def praNidayate_ner_ghu() -> State:
    s = build_pra_ni_dayate_ghu_state()
    s.tripadi_zone = True
    s = apply_rule("8.4.17", s)
    if not s.terms[1].meta.get("8_4_17_ner_done"):
        raise RuntimeError("8.4.17 did not apply to ni-upasarga")
    return s


__all__ = [
    "build_pra_ni_dayate_ghu_state",
    "praNidayate_ner_ghu",
]
