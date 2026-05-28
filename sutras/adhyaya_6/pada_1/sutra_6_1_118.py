"""
6.1.118  आपोजुषाणोवृष्णोवर्षिष्ठेऽम्बेऽम्बालेऽम्बिकेपूर्वे  —  VIDHI

Padaccheda: आपो जुषाणो वृष्णो वर्षिष्ठे अम्बे अम्बाले (लुप्तप्रथमान्तनिर्देशः) अम्बिके-पूर्वे

आपोजुषाणोवृष्णोवर्षिष्ठेऽम्बेऽम्बालेऽम्बिकेपूर्वे (6.1.118)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_118_ApojuzARov_118"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.118"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.118",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ApojuzARovfzRovarzizWe'mbe'mbAle'mbikepUrve",
    text_dev              = "आपोजुषाणोवृष्णोवर्षिष्ठेऽम्बेऽम्बालेऽम्बिकेपूर्वे",
    padaccheda_dev        = "आपो जुषाणो वृष्णो वर्षिष्ठे अम्बे अम्बाले (लुप्तप्रथमान्तनिर्देशः) अम्बिके-पूर्वे",
    why_dev               = "(सूत्रम् 6.1.118) आपोजुषाणोवृष्णोवर्षिष्ठेऽम्बेऽम्बालेऽम्बिकेपूर्वे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
