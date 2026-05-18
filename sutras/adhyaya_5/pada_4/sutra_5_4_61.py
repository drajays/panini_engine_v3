"""
5.4.61  सपत्त्रनिष्पत्रादतिव्यथने  —  VIDHI

Padaccheda: सपत्र-निष्पत्रात् अतिव्यथने

सपत्त्रनिष्पत्रादतिव्यथने (5.4.61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_61_sapattrani_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_61_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sapattranizpatrAdativyaTane",
    text_dev              = "सपत्त्रनिष्पत्रादतिव्यथने",
    padaccheda_dev        = "सपत्र-निष्पत्रात् अतिव्यथने",
    why_dev               = "(सूत्रम् 5.4.61) सपत्त्रनिष्पत्रादतिव्यथने।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
