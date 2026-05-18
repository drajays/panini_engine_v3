"""
4.3.123  पत्त्राध्वर्युपरिषदश्च  —  VIDHI

Padaccheda: पत्त्र-अध्वर्यु-परिषदः च

पत्त्राध्वर्युपरिषदश्च (4.3.123)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_123_pattrADvar_123"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_123_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.123"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.123",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pattrADvaryuparizadaSca",
    text_dev              = "पत्त्राध्वर्युपरिषदश्च",
    padaccheda_dev        = "पत्त्र-अध्वर्यु-परिषदः च",
    why_dev               = "(सूत्रम् 4.3.123) पत्त्राध्वर्युपरिषदश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
