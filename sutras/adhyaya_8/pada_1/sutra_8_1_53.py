"""
8.1.53  विभाषितं सोपसर्गमनुत्तमम्  —  VIDHI

Padaccheda: विभाषितम् स-उपसर्गम् अन्-उत्तमम्

विभाषितं सोपसर्गमनुत्तमम् (8.1.53)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_53_viBAzitaM_53"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzitaM sopasargamanuttamam",
    text_dev              = "विभाषितं सोपसर्गमनुत्तमम्",
    padaccheda_dev        = "विभाषितम् स-उपसर्गम् अन्-उत्तमम्",
    why_dev               = "(सूत्रम् 8.1.53) विभाषितं सोपसर्गमनुत्तमम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
