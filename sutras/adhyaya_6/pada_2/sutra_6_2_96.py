"""
6.2.96  उदकेऽकेवले  —  VIDHI

Padaccheda: उदके अकेवले

उदकेऽकेवले (6.2.96)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_96_udakekeva_96"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_96_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udake'kevale",
    text_dev              = "उदकेऽकेवले",
    padaccheda_dev        = "उदके अकेवले",
    why_dev               = "(सूत्रम् 6.2.96) उदकेऽकेवले।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
