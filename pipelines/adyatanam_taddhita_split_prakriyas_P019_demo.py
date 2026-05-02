"""
pipelines/adyatanam_taddhita_split_prakriyas_P019_demo.py — **P019** (**अद्यतनम्**).

Source: ``…/my_scripts/final/split_prakriyas_11/P019.json``.

Spine (apply_rule only):
  **4.3.23** (attach tyup, recipe-armed) → **1.3.3** → **1.3.9** (tyup→tyu) →
  **7.1.1** (tyu→tana) → **1.2.46** → (merge) → **4.1.2** → **7.1.24** → **6.1.107**.

Note: JSON cites **6.1.101** for a+am; this engine uses **6.1.107** for that contraction.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_adyatanam_taddhita_split_prakriyas_P019() -> State:
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("adya")),
        tags={"anga", "prātipadika", "napuṃsaka", "prakriya_P019_adyatanam_demo"},
        meta={"upadesha_slp1": "adya"},
    )
    s = State(terms=[stem], meta={}, trace=[])
    s.meta["prakriya_P019_adyatanam_split_prakriyas_11"] = True

    s.meta["prakriya_P019_4_3_23_tyup_arm"] = True
    s = apply_rule("4.3.23", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("7.1.1", s)

    s = apply_rule("1.2.46", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("7.1.24", s)
    s = apply_rule("6.1.107", s)
    return s


__all__ = ["derive_adyatanam_taddhita_split_prakriyas_P019"]

