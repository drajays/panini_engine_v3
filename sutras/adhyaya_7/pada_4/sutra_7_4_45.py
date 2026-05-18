"""
7.4.45  सुधितवसुधितनेमधितधिष्वधिषीय च  —  VIDHI

Padaccheda: सुधित (लुप्तप्रथमान्तनिर्देशः) वसुधित (लुप्तप्रथमान्तनिर्देशः) नेमधित (लुप्तप्रथमान्तनिर्देशः) धिष्व (क्रियापदम्) धिषीय (क्रियापदम्) च

सुधितवसुधितनेमधितधिष्वधिषीय च (7.4.45)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_45_suDitavasu_45"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_45_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "suDitavasuDitanemaDitaDizvaDizIya ca",
    text_dev              = "सुधितवसुधितनेमधितधिष्वधिषीय च",
    padaccheda_dev        = "सुधित (लुप्तप्रथमान्तनिर्देशः) वसुधित (लुप्तप्रथमान्तनिर्देशः) नेमधित (लुप्तप्रथमान्तनिर्देशः) धिष्व (क्रियापदम्) धिषीय (क्रियापदम्) च",
    why_dev               = "(सूत्रम् 7.4.45) सुधितवसुधितनेमधितधिष्वधिषीय च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
