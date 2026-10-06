"""
5.1.88  वर्षाल्लुक् च  —  VIDHI

Padaccheda: वर्षात् लुक् च

वर्षाल्लुक् च (5.1.88)
Pāṭha: ashtadhyayi.com data.txt row i=51088 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_88_varzAlluk_88"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.88", state, "5.1.78"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.88"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "varzAlluk ca",
    text_dev              = "वर्षाल्लुक् च",
    samagra_slp1          = "tamaDIzwo Bfto BUto BAvI taTA tena nirvfttam iti varzAt dvigoH KaH WaY vA luk ca ",
    samagra_dev           = "'तमधीष्टो भृतो भूतो भावी' (तथा) 'तेन निर्वृत्तम्' (इति) वर्षात् द्विगोः खः ठञ् वा, लुक् च ।",
    padaccheda_dev        = "वर्षात् लुक् च",
    why_dev               = "(सूत्रम् 5.1.88) वर्षाल्लुक् च।",
    anuvritti_from        = ('5.1.78',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
