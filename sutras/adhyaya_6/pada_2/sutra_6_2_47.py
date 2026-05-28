"""
6.2.47  अहीने द्वितीया  —  VIDHI

Padaccheda: अहीने द्वितीया

अहीने द्वितीया (6.2.47)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_47_ahIne_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ahIne dvitIyA",
    text_dev              = "अहीने द्वितीया",
    padaccheda_dev        = "अहीने द्वितीया",
    why_dev               = "(सूत्रम् 6.2.47) अहीने द्वितीया।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
