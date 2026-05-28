"""
2.3.52  अधीगर्थदयेशां कर्मणि  —  VIDHI

Padaccheda: अधि-इक्-अर्थ-दय-ईशाम् कर्मणि

adhi-ik, day, isa verbs take karma as sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_52_adhiika_daya_isa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDIgarTadayeSAM karmaRi",
    text_dev              = "अधीगर्थदयेशां कर्मणि",
    padaccheda_dev        = "अधि-इक्-अर्थ-दय-ईशाम् कर्मणि",
    why_dev               = "अधि-इक्-अर्थ-दय-ईशाम् कर्मणि षष्ठी (२.३.५२)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
