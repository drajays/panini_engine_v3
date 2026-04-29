"""
pipelines/cicIzati_ci_san_desiderative_demo.py — चिचीषति (*cicIzati*) demo.

Source: ``separated_prakriyas/prakriya_11_2026-04-29_14_08_21.json`` (headline
*ci* + *san* desiderative).

Target SLP1: **cicIzati**

Narrow spine:
  *ci* + *san* (3.1.7 → ``is``) → 1.2.8 (*kitvat* on *san*) → 3.1.32
  6.1.1 + 6.1.4 + **6.4.16** (*ī* before *san* on the non-abhyāsa *ci*; *is* → ``s``)
  laṭ 3sg kartari (``P00_lat_vartamane_tip_and_sap``) + *śap* *it*-lopa
  *pada* merge → tripāḍī **8.3.59** (*s* → *ṣ* / ``z`` after *ī*).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_lat_vartamane_tip_and_sap
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_cicIzati() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ci"),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "ci"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    s.meta["3_1_7_san_arm"] = True
    s = apply_rule("3.1.7", s)
    s = apply_rule("1.2.8", s)
    s = apply_rule("1.1.5", s)
    s = apply_rule("3.1.32", s)

    s.meta["6_1_1_dvitva_arm"] = True
    s = apply_rule("6.1.1", s)
    s = apply_rule("6.1.4", s)
    s.meta["6_4_16_sani_dirgha_arm"] = True
    s = apply_rule("6.4.16", s)

    s = P00_lat_vartamane_tip_and_sap(s)
    for sid in ("1.3.3", "1.3.8", "1.3.9"):
        s = apply_rule(sid, s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.59", s)
    return s


__all__ = ["derive_cicIzati"]
