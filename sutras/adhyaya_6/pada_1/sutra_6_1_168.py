"""
6.1.168  सावेकाचस्तृतीयाऽऽदिविभक्तिः  —  VIDHI

Padaccheda: सौ एक-अचः तृतीया-आदिः विभक्तिः

सावेकाचस्तृतीयाऽऽदिविभक्तिः (6.1.168)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_168_sAvekAcast_168"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.168"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.168",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sAvekAcastftIyA''diviBaktiH",
    text_dev              = "सावेकाचस्तृतीयाऽऽदिविभक्तिः",
    padaccheda_dev        = "सौ एक-अचः तृतीया-आदिः विभक्तिः",
    why_dev               = "(सूत्रम् 6.1.168) सावेकाचस्तृतीयाऽऽदिविभक्तिः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
