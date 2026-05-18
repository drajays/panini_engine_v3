"""
6.3.139  सम्प्रसारणस्य  —  VIDHI

Padaccheda: सम्प्रसारणस्य

सम्प्रसारणस्य (6.3.139)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_139_samprasAra_139"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_139_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.139"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.139",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samprasAraRasya",
    text_dev              = "सम्प्रसारणस्य",
    padaccheda_dev        = "सम्प्रसारणस्य",
    why_dev               = "(सूत्रम् 6.3.139) सम्प्रसारणस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
