"""
pipelines/madhvari_madhu_ari_dvitva_lesson.py — द्वित्व (१.१.५८): *yaṇ* ādeśa vs **8.4.47** gemination.

Prakriyā (*मधु* + *अरि* → **मद्ध्वरि** / SLP1 **maddhvari**):
  **6.1.77** ``u``→``v`` (*para-nimitta* ādeśa, not *sthānivat* for **8.4.47**) →
  **1.1.57** + **1.1.58** → **8.4.47** ``a``+``d`` gemination (not ``v``) → *maddhvari*.

Note: tripāḍī **8.4.47** (*anaci ca*), not **6.** adhyāya *abhyāsa* *dvirvacana* (**1.1.59**).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_samhita_iko_yanaci_spine,
    P00_tripadi_yar_anaci_dvitva_spine,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _madhu_ari_pair() -> State:
    return State(
        terms=[
            Term(
                kind="prakriti",
                varnas=list(parse_slp1_upadesha_sequence("madhu")),
                tags={"prātipadika", "anga"},
                meta={"upadesha_slp1": "madhu"},
            ),
            Term(
                kind="prakriti",
                varnas=list(parse_slp1_upadesha_sequence("ari")),
                tags={"prātipadika", "anga"},
                meta={"upadesha_slp1": "ari"},
            ),
        ],
        meta={},
        trace=[],
    )


def derive_madhvari_madhu_ari_dvitva_lesson() -> State:
    s = P00_samhita_iko_yanaci_spine(_madhu_ari_pair())
    s = apply_rule("1.1.57", s)
    s = apply_rule("1.1.58", s)
    return P00_tripadi_yar_anaci_dvitva_spine(s)


def derive_madhvari_madhu_ari_yan_only_lesson() -> State:
    """After **6.1.77** only — ``madhvari`` (no **8.4.47**)."""
    s = P00_samhita_iko_yanaci_spine(_madhu_ari_pair())
    s = apply_rule("1.1.57", s)
    s = apply_rule("1.1.58", s)
    return s


__all__ = [
    "derive_madhvari_madhu_ari_dvitva_lesson",
    "derive_madhvari_madhu_ari_yan_only_lesson",
]
