"""
*pra*+*ni*+**dā** (*ghu*) *laṭ* surface slice — **8.4.17** *neḥ* → *ṇ* (प्रणि·ददाति).

State model: three ``Term``s (``pra`` | ``ni`` | **dadAti** *dhātu*), **1.1.20** *ghu*
*saṃjñā* registered, then *Tripāḍī* so **8.4.17** (first **n** of *ni* → **R**) applies.

*Śruti target (SLP1):* **praRidadAti** (ण् = ``R``, *not* ``N``/ङ्; not **pranidadAti**).

*Cross-check* user note: ``…/my panini notes/प्रणिददाति'.md`` — *n* in *ni* after *pra* before *ghu* *dā*.
"""
from __future__ import annotations

import sutras  # noqa: F401  — SUTRA_REGISTRY

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_20 import (
    dhatu_upadesha_slp1_is_ghu,
    ghu_samjna_is_registered,
)


def _make_pra_ni_dadAti_terms() -> tuple[Term, Term, Term]:
    """Fresh ``Term``s (``apply_rule`` mutates; do not cache across calls)."""
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
    # *da~da* *dā* *bhu* *laṭ* 3sg (surface row only; *vidhi* chain is out of scope)
    dadAti = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("dadAti"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "da~da"},
    )
    return (pra, ni, dadAti)


def build_pra_ni_ghu_state() -> State:
    pra, ni, dadAti = _make_pra_ni_dadAti_terms()
    s = State(terms=[pra, ni, dadAti], meta={}, trace=[])
    s = apply_rule("1.1.20", s)
    if not ghu_samjna_is_registered(s):
        raise RuntimeError("1.1.20 ghu set not registered (unexpected)")
    u = s.terms[2].meta.get("upadesha_slp1", "")
    if not dhatu_upadesha_slp1_is_ghu(s, u):
        raise RuntimeError("demo dhātu must be ghu (da~da)")
    return s


def praNidadAti_ner_ghu() -> State:
    s = build_pra_ni_ghu_state()
    s.tripadi_zone = True
    s = apply_rule("8.4.17", s)
    if not s.terms[1].meta.get("8_4_17_ner_done"):
        raise RuntimeError("8.4.17 did not apply to ni-upasarga")
    return s


__all__ = [
    "build_pra_ni_ghu_state",
    "praNidadAti_ner_ghu",
]
