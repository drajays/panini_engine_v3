"""
pipelines/ninAya_lit_nI_P036_demo.py — **निनाय** (*nināya*, *liṭ* pra. eka, *nī*).

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P036.json``

Spine (``apply_rule`` + recipe meta; **7.2.115** *vṛddhi* pakṣa omitted — JSON **PAKṢA-2**
**7.3.84** *guṇa* path):

  • *nī* (**nI**) + *liṭ* → **tip** row → **3.4.82** ``tip``→``Nal`` (``P00_lit_tip_to_Nal``)
  • **1.3.3**/**1.3.9** on ``Nal`` → ``Na`` → **7.3.84** → **6.1.78** (*e*+*a* of ``ṇal``)
  • **8.4.41** (**P036**) ``Na``→augment ``a`` → **6.1.8** (*sthānivat* **ne**) → **7.4.59** → **7.4.60**
  • *pada* merge → **6.1.101** (**P036**) ``ninaya``→``ninAya``
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_lit_tip_to_Nal,
    P00_upadesha_it_1_3_1_2_5,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_ninAya_lit_nI_P036() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("nI")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "nI"},
    )
    dhatu.meta["1_4_22_affix_class"] = "eka"

    s = State(terms=[dhatu], meta={}, trace=[])

    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    s.meta["3_2_115_paroksha_lit_arm"] = True
    s = apply_rule("3.2.115", s)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = P00_lit_tip_to_Nal(s)

    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    s = apply_rule("7.3.84", s)
    s = apply_rule("6.1.78", s)

    s.meta["P036_8_4_41_Na_to_augment_a_arm"] = True
    s = apply_rule("8.4.41", s)

    s.meta["P036_6_1_8_lit_sthanivat_ne_arm"] = True
    s = apply_rule("6.1.8", s)

    s.meta["P036_7_4_59_abhyasa_ne_to_ni_arm"] = True
    s = apply_rule("7.4.59", s)
    s = apply_rule("7.4.60", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s.meta["P036_6_1_101_ninaya_dirgha_arm"] = True
    s = apply_rule("6.1.101", s)
    return s


__all__ = ["derive_ninAya_lit_nI_P036"]
