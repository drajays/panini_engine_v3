"""
pipelines/agda_lit_ghas_P033_demo.py — P033 **अग्द**-*stem* (**agda**, *ghas*+*liṭ* span).

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P033.json``

OCR/teaching trace is labelled *very-low*; engine models the JSON’s mechanical spine:

  • **Gas** (*ghas* machine shape) → **liṭ** (**3.2.115**) → ``ta`` (**3.4.77**/**3.4.78** slice)
  • **6.4.100** (*upadhā-*``a`` *lopa* before *hal*)
  • Tripāḍī **8.2.26** / **8.2.40** (**G**+*t*→**G**+*d*) / **8.4.53** (*jaṣṭva* **G**→**g**)
  • **8.4.55** span ``gda``→``agda`` completes the illustrative *siddhi* (substitute **2.4.40**
    *ad*→*ghas* + augment echo, per JSON notes).
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
from pipelines.subanta import _pada_merge


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("Gas")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "Gas"},
    )
    return State(terms=[dhatu], meta={}, trace=[], samjna_registry={})


def derive_agda_lit_ghas_P033() -> State:
    s = _build_state()
    s.meta["pada"] = "parasmaipada"

    s = apply_rule("1.1.68", s)
    s = apply_rule("1.3.1", s)
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    s.meta["3_2_115_paroksha_lit_arm"] = True
    s = apply_rule("3.2.115", s)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "ta"
    s = apply_rule("3.4.78", s)
    for sid in ("1.4.99", "1.4.100", "1.3.78", "1.4.101", "1.4.108", "1.4.102", "1.4.22"):
        s = apply_rule(sid, s)
    for sid in ("1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    s.meta["P033_6_4_100_gas_upadha_arm"] = True
    s = apply_rule("6.4.100", s)

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s.meta["P033_8_2_26_jhalo_jhali_arm"] = True
    s = apply_rule("8.2.26", s)
    s.meta["P033_8_2_40_G_to_d_arm"] = True
    s = apply_rule("8.2.40", s)
    s.meta["P033_8_4_53_jashtva_arm"] = True
    s = apply_rule("8.4.53", s)
    s.meta["P033_8_4_55_agda_bridge_arm"] = True
    s = apply_rule("8.4.55", s)
    return s


__all__ = ["derive_agda_lit_ghas_P033"]
