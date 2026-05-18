"""
4.1.165  वाऽन्यस्मिन् सपिण्डे स्थविरतरे जीवति  —  VIDHI

Padaccheda: वा अन्यस्मिन् सपिण्डे स्थविरतरे जीवति

वाऽन्यस्मिन् सपिण्डे स्थविरतरे जीवति (4.1.165)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_165_vAnyasmin_165"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_165_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.165"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.165",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA'nyasmin sapiRqe sTaviratare jIvati",
    text_dev              = "वाऽन्यस्मिन् सपिण्डे स्थविरतरे जीवति",
    padaccheda_dev        = "वा अन्यस्मिन् सपिण्डे स्थविरतरे जीवति",
    why_dev               = "(सूत्रम् 4.1.165) वाऽन्यस्मिन् सपिण्डे स्थविरतरे जीवति।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
