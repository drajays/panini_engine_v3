"""
6.2.10  अध्वर्युकषाययोर्जातौ  —  VIDHI

Padaccheda: अध्वर्यु-कषाययोः जातौ

अध्वर्युकषाययोर्जातौ (6.2.10)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_10_aDvaryukaz_10"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDvaryukazAyayorjAtO",
    text_dev              = "अध्वर्युकषाययोर्जातौ",
    padaccheda_dev        = "अध्वर्यु-कषाययोः जातौ",
    why_dev               = "(सूत्रम् 6.2.10) अध्वर्युकषाययोर्जातौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
