"""
pipelines/jakzatuH_lit_ad_gas_P034_demo.py — **जक्षतुः** (*jakṣatuḥ*, *liṭ* pra. dvi).

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P034.json``

Spine (glass-box ``apply_rule`` + narrow meta arms, per JSON):

  • *dhātu* **ad** → **Gas** (**2.4.40**) in *liṭ* (**3.2.115**)
  • *tas* → *atus* (**3.4.82**) + **1.2.5** (*kit*)
  • **6.4.100** (*upadhā* **a**-*lopa* before *atus*)
  • **6.1.8** / **6.1.4** / **7.4.60** / **7.4.62** / **7.4.59** on *abhyāsa*
  • *pada* merge → **8.2.1** → **8.4.55** ``jaGsatus``→``jakzatus`` → **8.2.66** / **8.3.15** (SLP1 **z** = ष)
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


def derive_jakzatuH_lit_ad_gas_P034() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("ad")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "ad"},
    )
    dhatu.meta["1_4_22_affix_class"] = "dvi"

    s = State(terms=[dhatu], meta={}, trace=[])

    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    s.meta["3_2_115_paroksha_lit_arm"] = True
    s = apply_rule("3.2.115", s)

    s.meta["P034_2_4_40_ad_to_gas_arm"] = True
    s = apply_rule("2.4.40", s)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s.meta["3_4_82_lit_atus_arm"] = True
    s = P00_tin_tas_adesh_full(s)

    s = apply_rule("3.4.82", s)
    s = apply_rule("1.2.5", s)

    s.meta["P034_6_4_100_gas_upadha_atus_arm"] = True
    s = apply_rule("6.4.100", s)

    s.meta["6_1_8_lit_dvitva_arm"] = True
    s = apply_rule("6.1.8", s)
    s = apply_rule("6.1.4", s)

    if s.terms and "abhyasa" in s.terms[0].tags:
        s.terms[0].meta["7_4_60_first_hal_only"] = True
    s = apply_rule("7.4.60", s)

    s.meta["7_4_62_kuhoscu_abhyasa_arm"] = True
    s = apply_rule("7.4.62", s)

    s.meta["P034_7_4_59_abhyasa_pad_a_arm"] = True
    s = apply_rule("7.4.59", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s.meta["P034_8_4_55_jakz_cluster_arm"] = True
    s = apply_rule("8.4.55", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s


__all__ = ["derive_jakzatuH_lit_ad_gas_P034"]
