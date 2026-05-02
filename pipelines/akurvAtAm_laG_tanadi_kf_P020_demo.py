"""
pipelines/akurvAtAm_laG_tanadi_kf_P020_demo.py — **P020** (**अकुर्वाताम्**).

Source: ``…/my_scripts/final/split_prakriyas_11/P020.json``.

The JSON notes the OCR target ``akurutAm`` is wrong; the recorded derivation yields
**akurvAtAm** (laṅ, prathamā-dvivacana ātmanepada of *kf* in this narrow tanādi-u demo).

Spine (apply_rule only):
  **3.2.111** (laṅ placeholder, armed) → **3.4.77** → **3.4.78** (AtAm) →
  **3.1.79** (tanādi u) → **7.3.84** → **1.1.51** →
  **6.1.77** (armed general boundary: u + A → v + A) →
  **1.2.4** → **1.1.5** → **6.4.110** →
  **6.1.77** (armed again: u + A → v + A) →
  **6.4.71** (aṭ augment for laṅ).

CONSTITUTION Art. 7 / 11: apply_rule only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_akurvAtAm_laG_tanadi_kf_P020() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kf")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "kf"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["prakriya_P020_akurvAtAm_split_prakriyas_11"] = True
    s.meta["lakara"] = "laG"
    s.meta["3_2_111_laG_arm"] = True

    s = apply_rule("3.2.111", s)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    # tiṅ ādeśa: AtAm (3rd dual ātmanepada)
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "AtAm"
    s = apply_rule("3.4.78", s)

    # tanādi u-vikaraṇa
    s.meta["3_1_79_tanadi_u_arm"] = True
    s = apply_rule("3.1.79", s)

    # guṇa on kf before sārvadhātuka u; then uRaN-rapara completes ar
    s = apply_rule("7.3.84", s)
    s = apply_rule("1.1.51", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    # a → u before kṅit sārvadhātuka (engine context setup)
    s = apply_rule("1.2.4", s)
    s = apply_rule("1.1.5", s)
    s = apply_rule("6.4.110", s)

    # kuru + AtAm → kurvAtAm (general arm across terms)
    s.meta["6_1_77_ik_yan_aci_general_arm"] = True
    s = apply_rule("6.1.77", s)

    # aṭ augment for laṅ
    s = apply_rule("6.4.71", s)
    return s


__all__ = ["derive_akurvAtAm_laG_tanadi_kf_P020"]

