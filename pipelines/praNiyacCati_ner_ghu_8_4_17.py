"""
*pra*+*ni*+**dā** → **7.3.78** *yacch* *ādeśa* *laṭ* slice — **8.4.17** (प्रणियच्छति).

The note
``…/my panini notes/प्रणियच्छति .md`` shows **पाघ्रा… (७.३.७८)** + **1.1.55** + **1.1.56**
(*sthānivadbhāva* for *ghu* with *yacch*), then **8.4.17** *neḥ* → *ṇ* on *ni*.

v3 does **not** model **7.3.78** *vidhi* here; the *laṭ* 3sg *ādeśa* row is pre-filled as
**yacCati** (SLP1 **C** = छ) with **upadesha_slp1** still **``da~da``** (the *sthānin*), so
**1.1.20** *ghu* and **8.4.17** *ner*+**घु** use the same ``cond`` path as
``pipelines/praNidadAti_ner_ghu_8_4_17`` — *śāstrīya* *upadeśa* identity, not the surface
string, drives *ghu* (see **1.1.56** *paribhāṣā* in the *prakriyā* note).

*Śruti target (SLP1):* **praRiyacCati** (ण् = ``R``).
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


def _make_pra_ni_yacCati_terms() -> tuple[Term, Term, Term]:
    """*Śabda* after **7.3.78**+**śap**+**tip** (surface), *upadeśa* = *da~da* (``1.1.55`` *corpus*)."""
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
    yacCati = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("yacCati"),
        tags={"dhatu", "anga", "upadesha"},
        meta={
            "upadesha_slp1": "da~da",
            "7_3_78_yacC_adesa": True,
        },
    )
    return (pra, ni, yacCati)


def build_pra_ni_yacCati_ghu_state() -> State:
    pra, ni, y = _make_pra_ni_yacCati_terms()
    s = State(terms=[pra, ni, y], meta={}, trace=[])
    s = apply_rule("1.1.20", s)
    if not ghu_samjna_is_registered(s):
        raise RuntimeError("1.1.20 ghu set not registered (unexpected)")
    u = s.terms[2].meta.get("upadesha_slp1", "")
    if not dhatu_upadesha_slp1_is_ghu(s, u):
        raise RuntimeError("demo dhātu upadeśa must be ghu (da~da)")
    s = apply_rule("1.1.56", s)
    if s.paribhasha_gates.get("sthanivadbhava") is not True:
        raise RuntimeError("1.1.56 sthānivadbhāva gate (unexpected)")
    return s


def praNiyacCati_ner_ghu() -> State:
    s = build_pra_ni_yacCati_ghu_state()
    s.tripadi_zone = True
    s = apply_rule("8.4.17", s)
    if not s.terms[1].meta.get("8_4_17_ner_done"):
        raise RuntimeError("8.4.17 did not apply to ni-upasarga")
    return s


__all__ = [
    "build_pra_ni_yacCati_ghu_state",
    "praNiyacCati_ner_ghu",
]
