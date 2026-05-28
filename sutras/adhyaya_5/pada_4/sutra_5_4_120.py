"""
5.4.120  सुप्रातसुश्वसुदिवशारिकुक्षचतुरश्रैणीपदाजपदप्रोष्ठपदाः  —  VIDHI

Padaccheda: सुप्रात-सुश्व-सुदिव-शारिकुक्ष-चतुरश्र-एणीपद-अजपद-प्रोष्ठपदाः

सुप्रातसुश्वसुदिवशारिकुक्षचतुरश्रैणीपदाजपदप्रोष्ठपदाः (5.4.120)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_120_suprAtasuS_120"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.120", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.120"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.120",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "suprAtasuSvasudivaSArikukzacaturaSrERIpadAjapadaprozWapadAH",
    text_dev              = "सुप्रातसुश्वसुदिवशारिकुक्षचतुरश्रैणीपदाजपदप्रोष्ठपदाः",
    padaccheda_dev        = "सुप्रात-सुश्व-सुदिव-शारिकुक्ष-चतुरश्र-एणीपद-अजपद-प्रोष्ठपदाः",
    why_dev               = "(सूत्रम् 5.4.120) सुप्रातसुश्वसुदिवशारिकुक्षचतुरश्रैणीपदाजपदप्रोष्ठपदाः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
