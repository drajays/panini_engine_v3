"""
pipelines/vibhidatuH_lit_demo.py — विभिदतुः (vibibhidatuH) glass-box demo.

Source: `/Users/dr.ajayshukla/my_scripts/separated_prakriyas/prakriya_04_2026-04-29_14_06_11.json`

Target SLP1: **vibiBidatuH**

Narrow spine (as per note):
  bhid (भिद्) + liṭ (parokṣa) + tas → atus (3.4.82)
  1.2.5 marks liṭ-ending as kit → blocks 7.3.86 guṇa via kṅiti signal
  6.1.8 dvitva + 6.1.4 abhyāsa-gate + 7.4.60 trim + 8.4.54 carca (B→b)
  Tripāḍī ru/visarga on final -s.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_upadesha_it_1_3_1_2_5,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_tin_tas_adesh_full,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_vibhidatuH() -> State:
    # dhātu: bhid
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("Bid"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "Bid"},
    )
    dhatu.meta["1_4_22_affix_class"] = "dvi"  # needed for tas in P00_tin_tas_adesh_full
    s = State(terms=[dhatu], meta={}, trace=[])

    # it-slice (harmless here; keeps consistency with other dhātu pipelines)
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    # parokṣa liṭ
    s.meta["3_2_115_paroksha_lit_arm"] = True
    s = apply_rule("3.2.115", s)

    # pratyaya adhikāra and tiṅ ādeśa (tas)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s.meta["3_4_82_lit_atus_arm"] = True
    s = P00_tin_tas_adesh_full(s)

    # liṭ parasmaipada tas -> atus
    s = apply_rule("3.4.82", s)

    # (Attempted) guṇa on upadhā in presence of ārdhadhātuka — blocked by 1.2.5→kṅiti.
    s = apply_rule("1.2.5", s)
    s = apply_rule("1.1.5", s)
    s = apply_rule("7.3.86", s)

    # dvitva & abhyāsa operations
    s.meta["6_1_8_lit_dvitva_arm"] = True
    s = apply_rule("6.1.8", s)
    s = apply_rule("6.1.4", s)
    s = apply_rule("7.4.60", s)
    s = apply_rule("8.4.54", s)

    # upasarga vi-
    vi = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("vi"),
        tags={"upasarga", "anga"},
        meta={"upadesha_slp1": "vi"},
    )
    s.terms.insert(0, vi)

    # merge + ru/visarga
    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s


__all__ = ["derive_vibhidatuH"]

