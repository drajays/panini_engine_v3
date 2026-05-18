"""
6.1.47  स्फुरतिस्फुलत्योर्घञि  —  VIDHI

Padaccheda: स्फुरति-स्फुलत्योः घञि

स्फुरतिस्फुलत्योर्घञि (6.1.47)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_47_sPuratisPu_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_47_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sPuratisPulatyorGaYi",
    text_dev              = "स्फुरतिस्फुलत्योर्घञि",
    padaccheda_dev        = "स्फुरति-स्फुलत्योः घञि",
    why_dev               = "(सूत्रम् 6.1.47) स्फुरतिस्फुलत्योर्घञि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
