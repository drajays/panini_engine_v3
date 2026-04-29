"""
pipelines/rurudizati_san_desiderative_demo.py — रुरुदिषति (rurudizati) demo.

Source: `/Users/dr.ajayshukla/my_scripts/separated_prakriyas/prakriya_09_2026-04-29_14_06_58.json`

Target SLP1: **rurudizati**

Narrow spine:
  rud + san (3.1.7) → kitvat on san (1.2.8) → 3.1.32 (sanādi dhātu)
  6.1.1 dvitva (armed) + 6.1.4 + 7.4.60 (abhyāsa trim) → rurudis
  laṭ 3sg kartari: 3.2.123 + tip→ti + śap (P00_lat_vartamane_tip_and_sap)
  merge + tripāḍī 8.3.59 ṣatva: s → z after i → rurudizati
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_lat_vartamane_tip_and_sap
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_rurudizati() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("rud"),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "rud"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # Add sanādi (desiderative) suffix.
    s.meta["3_1_7_san_arm"] = True
    s = apply_rule("3.1.7", s)
    s = apply_rule("1.2.8", s)  # kitvat marker on san
    s = apply_rule("1.1.5", s)
    s = apply_rule("3.1.32", s)

    # dvitva + abhyāsa trim
    s.meta["6_1_1_dvitva_arm"] = True
    s = apply_rule("6.1.1", s)
    s = apply_rule("6.1.4", s)
    s = apply_rule("7.4.60", s)

    # laṭ 3sg kartari + śap
    s = P00_lat_vartamane_tip_and_sap(s)
    # it-lopa on śap (and other upadeśa markers) so `Sap` collapses to `a`.
    for sid in ("1.3.3", "1.3.8", "1.3.9"):
        s = apply_rule(sid, s)

    # merge + tripāḍī ṣatva on s of san (`is`)
    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.59", s)
    return s


__all__ = ["derive_rurudizati"]

