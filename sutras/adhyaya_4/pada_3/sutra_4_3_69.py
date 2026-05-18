"""
4.3.69  अध्यायेष्वेवर्षेः  —  VIDHI

Padaccheda: अध्यायेषु एव ऋषेः

अध्यायेष्वेवर्षेः (4.3.69)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_69_aDyAyezvev_69"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_69_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDyAyezvevarzeH",
    text_dev              = "अध्यायेष्वेवर्षेः",
    padaccheda_dev        = "अध्यायेषु एव ऋषेः",
    why_dev               = "(सूत्रम् 4.3.69) अध्यायेष्वेवर्षेः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
