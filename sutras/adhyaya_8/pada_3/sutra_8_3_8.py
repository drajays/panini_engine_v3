"""
8.3.8  उभयथर्क्षु  —  VIDHI

Padaccheda: उभयथा ऋक्षु

उभयथर्क्षु (8.3.8)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_8_uBayaTarkz_8"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_8_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uBayaTarkzu",
    text_dev              = "उभयथर्क्षु",
    padaccheda_dev        = "उभयथा ऋक्षु",
    why_dev               = "(सूत्रम् 8.3.8) उभयथर्क्षु।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
