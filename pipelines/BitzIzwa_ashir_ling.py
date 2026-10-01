"""
pipelines/BitzIzwa_ashir_ling.py — भित्सीष्ट (*BitzIzwa*) demo.

Source: ``separated_prakriyas/prakriya_12_2026-04-29_14_08_30.json``

Target SLP1: **BitzIzwa**

Narrow spine:
  भिदिँर् (dhātupāṭha 07.0002) → it-lopa → Bid + āśīr-liṅ (3.3.173) + ``ta``
  (3.4.77 → 3.4.78) + sīyuṭ (3.4.102) + 1.2.11 kitvat + suṭ (3.4.107)
  + 6.1.66 (य्-लोप) → merge → tripāḍī 8.2.1 → 8.3.59 (s→z after I, twice)
  → 8.4.55 (d→t before z) → 8.4.41 (zt → zw)
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_ashir_atmane_suw_yalopa_merge,
    P00_dhatu_upadesha_it_lopa,
    P00_tin_adesha_base,
)

from engine import apply_rule
from engine.state import State
from pipelines.dhatupatha import resolve_dhatu_identifier
from pipelines.tinanta import _build_dhatu_term


def derive_BitzIzwa() -> State:
    dhatu = _build_dhatu_term(resolve_dhatu_identifier("Bidi~r"), "kartari", "AsIrliG")
    s = State(terms=[dhatu], meta={}, trace=[])
    s = P00_dhatu_upadesha_it_lopa(s)           # भिदिँर् → भिद्

    s.meta["ashir_liG"] = True
    s = apply_rule("3.3.173", s)

    # tin ādeśa: choose ātmanepada 3sg `ta` without reading paradigm coords in cond().
    s = P00_tin_adesha_base(s, "ta")

    s.meta["sIyuw_recipe"] = True
    s = apply_rule("3.4.102", s)
    s = apply_rule("1.2.11", s)
    s = P00_ashir_atmane_suw_yalopa_merge(s)

    # Two s-kāras occur here (sī + suṭ); apply ṣatva twice.
    s = apply_rule("8.3.59", s)
    s = apply_rule("8.3.59", s)
    s = apply_rule("8.4.55", s)
    s = apply_rule("8.4.41", s)
    return s


__all__ = ["derive_BitzIzwa"]
