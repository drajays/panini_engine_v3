"""
pipelines/Bavitum_split_prakriyas_P001_demo.py — **P001** (**भवितुम्**).

Source: ``…/my_scripts/final/split_prakriyas_11/P001.json``.

Spine (rule-based ``apply_rule`` only):
  **3.3.158** (narrow samjna stamp) → **1.3.3** → **1.3.9** → **7.2.35** → **7.3.84** → **6.1.78** →
  **1.1.40** (extended here with **tumun**) → **4.1.2** (prathamā-eka ``su``) → **2.4.82**.

**Upadesha tape:** internal Varṇa shape **tumn** (final **n** = *it*); ``meta['upadesha_slp1_original']``
preserves **tumun** for **1.1.40** / śāstra alignment (full ``tumun`` parse would leave **tumu** after
**1.3.9**, blocking **भवितुम्**).

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _witness_BU_split_P001() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("BU")),
        tags={"dhatu", "anga", "prātipadika", "prakriya_P001_Bavitum_demo"},
        meta={"upadesha_slp1": "BU"},
    )


def _tumun_pratyaya_P001() -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("tumn")),
        tags={"pratyaya", "krt", "ardhadhatuka", "upadesha"},
        meta={"upadesha_slp1": "tumn", "upadesha_slp1_original": "tumun"},
    )


def derive_Bavitum_split_prakriyas_P001() -> State:
    s = State(terms=[_witness_BU_split_P001(), _tumun_pratyaya_P001()], meta={}, trace=[])

    s.meta["prakriya_P001_samAnakartRk_tumun_note"] = True
    s.meta["prakriya_P001_3_3_158_arm"] = True
    s = apply_rule("3.3.158", s)

    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("7.2.35", s)
    s = apply_rule("7.3.84", s)
    s = apply_rule("6.1.78", s)

    s = apply_rule("1.1.40", s)

    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("2.4.82", s)
    return s


__all__ = [
    "derive_Bavitum_split_prakriyas_P001",
    "_witness_BU_split_P001",
    "_tumun_pratyaya_P001",
]
