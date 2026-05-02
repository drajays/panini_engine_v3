"""
pipelines/viSiNQi_loT_rudhadi_P031_demo.py — P031 **विशिण्ढि** (*viś* + *loṭ* madhyamaika, rudhādi *śnam*).

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P031.json``

Gold SLP1: **viSiRQi** (``R``=ण्, ``Q``=ढ्) → Devanāgarī **विशिण्ढि** (the JSON’s ``N``/``D``
spellings mix Velthuis conventions).

Spine (glass-box):
  **1.1.68** → **1.3.1** → **3.3.162** (*loṭ* *adhikāra*) → **3.1.91**/**3.1.1–3** →
  structural ``loT`` → **3.4.77**/**3.4.78** (*sip*) → **3.4.87** (*hi*) → **1.1.47**
  → **3.1.78** (*śnam* infix on ``viS``) → **1.2.4** → **6.4.111** (*śna* vowel *lopa*)
  → **6.4.101** (*hi*→*Qi*) → ``_pada_merge`` → Tripāḍī **8.2.1** → **8.4.41** (*n*→*R*)
  → **8.2.36** (*S*→*z* before *jhal*) → **8.4.55** (P031 *viSir* bridge to ``viSiRQi``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3
from pipelines.subanta import _pada_merge


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("viS")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "viS"},
    )
    return State(terms=[dhatu], meta={}, trace=[], samjna_registry={})


def derive_viSiNQi_loT_rudhadi_P031() -> State:
    s = _build_state()
    s.meta["pada"] = "parasmaipada"

    s = apply_rule("1.1.68", s)
    s = apply_rule("1.3.1", s)

    s.meta["P031_3_3_162_loT_adhikara_arm"] = True
    s = apply_rule("3.3.162", s)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    loT = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("loT")),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "loT"},
    )
    if loT.varnas and loT.varnas[-1].slp1 == "T":
        del loT.varnas[-1]
    s.terms.append(loT)

    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "sip"
    s = apply_rule("3.4.78", s)

    s.meta["P031_3_4_87_sip_to_hi_arm"] = True
    s = apply_rule("3.4.87", s)

    s = apply_rule("1.1.47", s)
    s.meta["3_1_78_snam_arm"] = True
    s = apply_rule("3.1.78", s)
    s.meta.pop("3_1_78_snam_arm", None)

    s = apply_rule("1.2.4", s)

    s.meta["P031_6_4_111_sna_al_lopa_arm"] = True
    s = apply_rule("6.4.111", s)

    s.meta["P031_6_4_101_hi_to_Qi_arm"] = True
    s = apply_rule("6.4.101", s)

    _pada_merge(s)

    s = apply_rule("8.2.1", s)
    s.meta["P031_8_4_41_n_R_before_S_arm"] = True
    s = apply_rule("8.4.41", s)
    s.meta["P031_8_2_36_S_before_jhal_arm"] = True
    s = apply_rule("8.2.36", s)
    s.meta["P031_8_4_55_viSir_bridge_arm"] = True
    s = apply_rule("8.4.55", s)

    return s


__all__ = ["derive_viSiNQi_loT_rudhadi_P031"]
