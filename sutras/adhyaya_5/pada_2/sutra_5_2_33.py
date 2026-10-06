"""
5.2.33  इनच्पिटच्चिकचि च  —  VIDHI

Padaccheda: इनच्-पिटच् चिकचि (लुप्तप्रथमान्तनिर्देशः) च

इनच्पिटच्चिकचि च (5.2.33)
Pāṭha: ashtadhyayi.com data.txt row i=52033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_33_inacpiwacc_33"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.33", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "inacpiwaccikaci ca",
    text_dev              = "इनच्पिटच्चिकचि च",
    samagra_slp1          = "nAsikAyAH nate neH inac-piwac neH cika-ciH ",
    samagra_dev           = "नासिकायाः नते नेः इनच्-पिटच्, (नेः) चिक-चिः ।",
    padaccheda_dev        = "इनच्-पिटच् चिकचि (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 5.2.33) इनच्पिटच्चिकचि च।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
