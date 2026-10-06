"""
4.4.33  रक्षति  —  VIDHI

Padaccheda: रक्षति (क्रियापदम्)

रक्षति (4.4.33)
Pāṭha: ashtadhyayi.com data.txt row i=44033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_33_rakzati_33"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.33", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rakzati",
    text_dev              = "रक्षति",
    samagra_slp1          = "tat rakzati iti samarTAnAm praTamAt paraH Wak pratyayaH",
    samagra_dev           = "'तत् रक्षति' (इति) समर्थानाम् प्रथमात् परः ठक् प्रत्ययः",
    padaccheda_dev        = "रक्षति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 4.4.33) रक्षति।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
