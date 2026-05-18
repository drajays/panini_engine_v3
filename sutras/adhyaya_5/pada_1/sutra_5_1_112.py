"""
5.1.112  समापनात् सपूर्वपदात्  —  VIDHI

Padaccheda: समापनात् स-पूर्वपदात्

समापनात् सपूर्वपदात् (5.1.112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_112_samApanAt_112"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_112_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.112"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samApanAt sapUrvapadAt",
    text_dev              = "समापनात् सपूर्वपदात्",
    padaccheda_dev        = "समापनात् स-पूर्वपदात्",
    why_dev               = "(सूत्रम् 5.1.112) समापनात् सपूर्वपदात्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
