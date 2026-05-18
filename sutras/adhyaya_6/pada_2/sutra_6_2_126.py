"""
6.2.126  चेलखेटकटुककाण्डं गर्हायाम्  —  VIDHI

Padaccheda: चेल-खेट-कटुक-काण्डम् गर्हायाम्

चेलखेटकटुककाण्डं गर्हायाम् (6.2.126)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_126_celaKewaka_126"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_126_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.126"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.126",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "celaKewakawukakARqaM garhAyAm",
    text_dev              = "चेलखेटकटुककाण्डं गर्हायाम्",
    padaccheda_dev        = "चेल-खेट-कटुक-काण्डम् गर्हायाम्",
    why_dev               = "(सूत्रम् 6.2.126) चेलखेटकटुककाण्डं गर्हायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
