"""
5.1.55  कुलिजाल्लुक्खौ च  —  VIDHI

Padaccheda: कुलिजात् लुक्-खौ च

कुलिजाल्लुक्खौ च (5.1.55)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_55_kulijAlluk_55"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_55_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kulijAllukKO ca",
    text_dev              = "कुलिजाल्लुक्खौ च",
    padaccheda_dev        = "कुलिजात् लुक्-खौ च",
    why_dev               = "(सूत्रम् 5.1.55) कुलिजाल्लुक्खौ च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
