"""
6.1.163  चितः  —  ANUVADA (narrow)

**Pāṭha:** *citaḥ* — a *cit* (*c*-marked *it*) *kṛt* *pratyaya* conditions
*antodātta* on the *pada* (accent *śāstra*; v3 has no *svara* tape).

Narrow v3 (``prakriya_20`` *devam*):
  • ``state.meta['prakriya_20_6_1_163_arm']`` — trace-only *anuvāda*.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return bool(state.meta.get("prakriya_20_6_1_163_arm"))


def act(state: State) -> State:
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.163",
    sutra_type     = SutraType.ANUVADA,
    text_slp1      = "citaH",
    text_dev       = "चितः",
    padaccheda_dev = "चितः",
    why_dev        = "चिति-प्रत्यये अन्तोदात्त-न्यायः (श्रुति-स्तरः; प्रक्रिया-२०)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
