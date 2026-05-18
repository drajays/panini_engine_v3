"""
5.2.26  तेन वित्तश्चुञ्चुप्चणपौ  —  VIDHI

Padaccheda: तेन वित्तः चुञ्चुप्-चणपौ

तेन वित्तश्चुञ्चुप्चणपौ (5.2.26)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_26_tena_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_26_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tena vittaScuYcupcaRapO",
    text_dev              = "तेन वित्तश्चुञ्चुप्चणपौ",
    padaccheda_dev        = "तेन वित्तः चुञ्चुप्-चणपौ",
    why_dev               = "(सूत्रम् 5.2.26) तेन वित्तश्चुञ्चुप्चणपौ।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
