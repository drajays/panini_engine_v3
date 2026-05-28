"""
6.4.174  दाण्डिनायनहास्तिनायनाथर्वणिकजैह्माशिनेयवाशिनायनिभ्रौणहत्यधैवत्यसारवैक्ष्वाकमैत्रेयहिरण्मयानि  —  VIDHI

Padaccheda: दाण्डिनायन-हास्तिनायन-आथर्वणिक-जैह्माशिनेय-वाशिनायनि-भ्रौणहत्य-धैवत्य-सारवैक्ष्वाक-मैत्रेय-हिरण्मयानि

दाण्डिनायनहास्तिनायनाथर्वणिकजैह्माशिनेयवाशिनायनिभ्रौणहत्यधैवत्यसारवैक्ष्वाकमैत्रेयहिरण्मयानि (6.4.174)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_174_dARqinAyan_174"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.174", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.174"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.174",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dARqinAyanahAstinAyanATarvaRikajEhmASineyavASinAyaniBrORahatyaDEvatyasAravEkzvAkamEtreyahiraRmayAni",
    text_dev              = "दाण्डिनायनहास्तिनायनाथर्वणिकजैह्माशिनेयवाशिनायनिभ्रौणहत्यधैवत्यसारवैक्ष्वाकमैत्रेयहिरण्मयानि",
    padaccheda_dev        = "दाण्डिनायन-हास्तिनायन-आथर्वणिक-जैह्माशिनेय-वाशिनायनि-भ्रौणहत्य-धैवत्य-सारवैक्ष्वाक-मैत्रेय-हिरण्मयानि",
    why_dev               = "(सूत्रम् 6.4.174) दाण्डिनायनहास्तिनायनाथर्वणिकजैह्माशिनेयवाशिनायनिभ्रौणहत्यधैवत्यसारवैक्ष्वाकमैत्रेयहिरण्मयानि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
