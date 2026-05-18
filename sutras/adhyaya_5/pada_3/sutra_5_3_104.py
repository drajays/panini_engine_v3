"""
5.3.104  द्रव्यं च भव्ये  —  VIDHI

Padaccheda: द्रव्यम् च भव्ये

द्रव्यं च भव्ये (5.3.104)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_104_dravyaM_104"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_104_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dravyaM ca Bavye",
    text_dev              = "द्रव्यं च भव्ये",
    padaccheda_dev        = "द्रव्यम् च भव्ये",
    why_dev               = "(सूत्रम् 5.3.104) द्रव्यं च भव्ये।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
