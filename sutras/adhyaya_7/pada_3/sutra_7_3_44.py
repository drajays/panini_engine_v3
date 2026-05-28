"""
7.3.44  प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः  —  VIDHI

Padaccheda: प्रत्ययस्थात् कात् पूर्वस्य अतः इत् आपि अ-सुपः

प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः (7.3.44)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_44_pratyayasT_44"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.44", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_3_44_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratyayasTAt kAt pUrvasyAta idApyasupaH",
    text_dev              = "प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः",
    padaccheda_dev        = "प्रत्ययस्थात् कात् पूर्वस्य अतः इत् आपि अ-सुपः",
    why_dev               = "(सूत्रम् 7.3.44) प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
