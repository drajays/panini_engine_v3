"""
6.2.189  अनोरप्रधानकनीयसी  —  VIDHI

Padaccheda: अनोः अप्रधान-कनीयसी

अनोरप्रधानकनीयसी (6.2.189)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_189_anorapraDA_189"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_189_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.189"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.189",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anorapraDAnakanIyasI",
    text_dev              = "अनोरप्रधानकनीयसी",
    padaccheda_dev        = "अनोः अप्रधान-कनीयसी",
    why_dev               = "(सूत्रम् 6.2.189) अनोरप्रधानकनीयसी।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
