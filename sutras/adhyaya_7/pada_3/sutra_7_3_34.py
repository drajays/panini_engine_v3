"""
7.3.34  नोदात्तोपदेशस्य मान्तस्यानाचमेः  —  VIDHI

Padaccheda: न उपदिष्ट&उदात्तस्य /seq=1 <BV>&()म&()अन्तस्य अन्-आचमेः

नोदात्तोपदेशस्य मान्तस्यानाचमेः (7.3.34)
Pāṭha: ashtadhyayi.com data.txt row i=73034 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_34_nodAttopad_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.34", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.34",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "nodAttopadeSasya mAntasyAnAcameH",
    text_dev              = "नोदात्तोपदेशस्य मान्तस्यानाचमेः",
    samagra_slp1          = "aNgasya na udAttopadeSasya mAntasya anAcameH vfdDiH YRiti ciRkftoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य न उदात्तोपदेशस्य मान्तस्य अनाचमेः वृद्धिः ञ्णिति चिण्कृतोः",
    padaccheda_dev        = "न उपदिष्ट&उदात्तस्य /seq=1 <BV>&()म&()अन्तस्य अन्-आचमेः",
    why_dev               = "(सूत्रम् 7.3.34) नोदात्तोपदेशस्य मान्तस्यानाचमेः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
