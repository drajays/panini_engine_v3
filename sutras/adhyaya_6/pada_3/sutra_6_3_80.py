"""
6.3.80  द्वितीये चानुपाख्ये  —  VIDHI

Padaccheda: द्वितीये च अनुपाख्ये

द्वितीये चानुपाख्ये (6.3.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_80_dvitIye_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvitIye cAnupAKye",
    text_dev              = "द्वितीये चानुपाख्ये",
    padaccheda_dev        = "द्वितीये च अनुपाख्ये",
    why_dev               = "(सूत्रम् 6.3.80) द्वितीये चानुपाख्ये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
