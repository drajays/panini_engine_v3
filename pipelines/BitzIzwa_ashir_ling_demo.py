"""
pipelines/BitzIzwa_ashir_ling_demo.py — भित्सीष्ट (*BitzIzwa*) demo.

Source: ``separated_prakriyas/prakriya_12_2026-04-29_14_08_30.json``

Target SLP1: **BitzIzwa**

Narrow spine:
  Bid + āśīr-liṅ (3.3.173) + tin-ādeśa ``ta`` (3.4.77 → 3.4.78)
  liṅ-sīyut (3.4.102 armed) + 1.2.11 kitvat tag (demo) + suṭ (3.4.107 armed)
  merge → tripāḍī 8.2.1 → 8.3.59 (s→z after I, twice) → 8.4.55 (d→t before z)
  → 8.4.41 (zt → zw)
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_BitzIzwa() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("Bid"),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "Bid"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # āśīr-liṅ lakāra placeholder.
    s.meta["3_3_173_ashishi_ling_arm"] = True
    s = apply_rule("3.3.173", s)

    # tin ādeśa: choose ātmanepada 3sg `ta` without reading paradigm coords in cond().
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "ta"
    s = apply_rule("3.4.78", s)

    # sīyut + suṭ augments for this āśīr-liṅ demo.
    s.meta["3_4_102_sIyuw_arm"] = True
    s = apply_rule("3.4.102", s)
    s.meta["1_2_11_ling_sic_kitvat_arm"] = True
    s = apply_rule("1.2.11", s)
    s.meta["3_4_107_suw_arm"] = True
    s = apply_rule("3.4.107", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    # Two s-kāras occur here (sī + suṭ); apply ṣatva twice.
    s = apply_rule("8.3.59", s)
    s = apply_rule("8.3.59", s)
    s = apply_rule("8.4.55", s)
    s = apply_rule("8.4.41", s)
    return s


__all__ = ["derive_BitzIzwa"]

