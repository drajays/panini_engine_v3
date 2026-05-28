"""
6.2.51  तवै चान्तश्च युगपत्  —  VIDHI

Padaccheda: तवै (लुप्तप्रथमान्तनिर्देशः) च अन्तः च युगपत्

तवै चान्तश्च युगपत् (6.2.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_51_tavE_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tavE cAntaSca yugapat",
    text_dev              = "तवै चान्तश्च युगपत्",
    padaccheda_dev        = "तवै (लुप्तप्रथमान्तनिर्देशः) च अन्तः च युगपत्",
    why_dev               = "(सूत्रम् 6.2.51) तवै चान्तश्च युगपत्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
