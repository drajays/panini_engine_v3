"""
2.4.23  सभा राजाऽमनुष्यपूर्वा  —  VIDHI

Padaccheda: सभा राजा-अमनुष्यपूर्वा

Sabha when preceded by raja or non-human.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_23_raja_sapha"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_23_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saBA rAjA'manuzyapUrvA",
    text_dev              = "सभा राजाऽमनुष्यपूर्वा",
    padaccheda_dev        = "सभा राजा-अमनुष्यपूर्वा",
    why_dev               = "राजा-अमनुष्यपूर्वा सभा (२.४.२३)।",
    anuvritti_from        = ('2.4.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
