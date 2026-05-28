"""
7.1.39  सुपां सुलुक्पूर्वसवर्णाऽऽच्छेयाडाड्यायाजालः  —  VIDHI

Padaccheda: सुपाम् सु-लुक्-पूर्वसवर्ण-आ-आत्-शे-या-डा-ड्या-याच्-आलः

सुपां सुलुक्पूर्वसवर्णाऽऽच्छेयाडाड्यायाजालः (7.1.39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_39_supAM_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.39", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "supAM sulukpUrvasavarRA''cCeyAqAqyAyAjAlaH",
    text_dev              = "सुपां सुलुक्पूर्वसवर्णाऽऽच्छेयाडाड्यायाजालः",
    padaccheda_dev        = "सुपाम् सु-लुक्-पूर्वसवर्ण-आ-आत्-शे-या-डा-ड्या-याच्-आलः",
    why_dev               = "(सूत्रम् 7.1.39) सुपां सुलुक्पूर्वसवर्णाऽऽच्छेयाडाड्यायाजालः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
