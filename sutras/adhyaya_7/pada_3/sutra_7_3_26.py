"""
7.3.26  अर्धात् परिमाणस्य पूर्वस्य तु वा  —  VIDHI

Padaccheda: अर्धात् परिमाणस्य पूर्वस्य तु वा

अर्धात् परिमाणस्य पूर्वस्य तु वा (7.3.26)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_26_arDAt_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.26", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_3_26_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arDAt parimARasya pUrvasya tu vA",
    text_dev              = "अर्धात् परिमाणस्य पूर्वस्य तु वा",
    padaccheda_dev        = "अर्धात् परिमाणस्य पूर्वस्य तु वा",
    why_dev               = "(सूत्रम् 7.3.26) अर्धात् परिमाणस्य पूर्वस्य तु वा।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
