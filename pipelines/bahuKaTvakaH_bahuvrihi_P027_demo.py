"""
pipelines/bahuKaTvakaH_bahuvrihi_P027_demo.py — P027 (बहुखट्वकः) glass-box.

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P027.json``

Target SLP1: **bahuKaTvakaH** (बहुखट्वकः).

Compressed spine (matches JSON intent; OCR is low for step labelling):
  **1.1.68** → **2.2.24** (bahuvrīhi saṃjñā) → **5.4.154** (kap samāsānta, chosen) →
  **7.4.15** (āp-hṛasva, chosen: KaTvA → KaTva) → **1.2.46** (structural samāsa merge) →
  subanta prathamā-ekavacana via ``derive_from_state(..., 1, 1)`` →
  **1.1.56** (paribhāṣā note).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.subanta import derive_from_state


def derive_bahuKaTvakaH_bahuvrihi_P027() -> State:
    bahu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("bahu")),
        tags={"anga", "prātipadika", "samasa_member", "bahuvrIhi"},
        meta={"upadesha_slp1": "bahu"},
    )
    katva = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("KaTvA")),
        tags={"anga", "prātipadika", "samasa_member", "bahuvrIhi", "strIliṅga"},
        meta={"upadesha_slp1": "KaTvA"},
    )
    s = State(terms=[bahu, katva], meta={}, trace=[], samjna_registry={})

    s = apply_rule("1.1.68", s)

    s.meta["P027_2_2_24_arm"] = True
    s = apply_rule("2.2.24", s)

    s.meta["P027_5_4_154_kap_arm"] = True
    s = apply_rule("5.4.154", s)

    s.meta["P027_7_4_15_Ap_hrasva_arm"] = True
    s = apply_rule("7.4.15", s)

    s = apply_rule("1.2.46", s)

    s = derive_from_state(s, 1, 1, linga="pulliṅga")

    s = apply_rule("1.1.56", s)
    return s


__all__ = ["derive_bahuKaTvakaH_bahuvrihi_P027"]

