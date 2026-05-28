"""
6.2.194  उपाद् द्व्यजजिनमगौरादयः  —  VIDHI

Padaccheda: उपात् द्वि-अच्-अजिन अगौर-आदयः

उपाद् द्व्यजजिनमगौरादयः (6.2.194)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_194_upAd_194"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.194"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.194",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upAd dvyajajinamagOrAdayaH",
    text_dev              = "उपाद् द्व्यजजिनमगौरादयः",
    padaccheda_dev        = "उपात् द्वि-अच्-अजिन अगौर-आदयः",
    why_dev               = "(सूत्रम् 6.2.194) उपाद् द्व्यजजिनमगौरादयः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
