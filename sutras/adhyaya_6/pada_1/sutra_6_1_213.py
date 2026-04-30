"""
6.1.213  यतोऽनावः  —  ANUVADA (narrow)

**Pāṭha:** *yato'nāvaḥ* — *udātta* on the first vowel of the base when the
affix is **yat** (accent *śāstra*; v3 has no *svara* on ``Varna`` rows).

Narrow v3 (``prakriya_18``):
  • ``cond`` — ``state.meta['prakriya_18_6_1_213_arm']``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return bool(state.meta.get("prakriya_18_6_1_213_arm"))


def act(state: State) -> State:
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.213",
    sutra_type     = SutraType.ANUVADA,
    text_slp1      = "yato nAvaH",
    text_dev       = "यतोऽनावः",
    padaccheda_dev = "यतः अनावः",
    why_dev        = "यत्-प्रत्यये आद्य्-उदात्त-न्यायः (श्रुति-स्तरः)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
