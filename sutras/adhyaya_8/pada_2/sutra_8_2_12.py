"""
8.2.12  आसन्दीवदष्ठीवच्चक्रीवत्कक्षीवद्रुमण्वच्चर्मण्वती  —  VIDHI

Padaccheda: आसन्दीवत् (लुप्तप्रथमान्त) अष्ठीवत् (लुप्तप्रथमान्त) चक्रीवत् (लुप्तप्रथमान्त) कक्षीवत् (लुप्तप्रथमान्त) रुमण्वत् (लुप्तप्रथमान्त) चर्मण्वती (लुप्तप्रथमान्त)

आसन्दीवदष्ठीवच्चक्रीवत्कक्षीवद्रुमण्वच्चर्मण्वती (8.2.12)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_12_AsandIvada_12"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AsandIvadazWIvaccakrIvatkakzIvadrumaRvaccarmaRvatI",
    text_dev              = "आसन्दीवदष्ठीवच्चक्रीवत्कक्षीवद्रुमण्वच्चर्मण्वती",
    padaccheda_dev        = "आसन्दीवत् (लुप्तप्रथमान्त) अष्ठीवत् (लुप्तप्रथमान्त) चक्रीवत् (लुप्तप्रथमान्त) कक्षीवत् (लुप्तप्रथमान्त) रुमण्वत् (लुप्तप्रथमान्त) चर्मण्वती (लुप्तप्रथमान्त)",
    why_dev               = "(सूत्रम् 8.2.12) आसन्दीवदष्ठीवच्चक्रीवत्कक्षीवद्रुमण्वच्चर्मण्वती।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
