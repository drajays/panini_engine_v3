"""
5.1.79  तेन निर्वृत्तम्  —  VIDHI

Padaccheda: तेन निर्वृत्तम्

तेन निर्वृत्तम् (5.1.79)
Pāṭha: ashtadhyayi.com data.txt row i=51079 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_79_tena_79"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.79", state, "5.1.78"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.79"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.79",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tena nirvfttam",
    text_dev              = "तेन निर्वृत्तम्",
    samagra_slp1          = "tena nirvfttam iti samarTAnAm praTamAt kAlAt WaY pratyayaH",
    samagra_dev           = "'तेन निर्वृत्तम्' (इति) समर्थानाम् प्रथमात् कालात् ठञ् प्रत्ययः",
    padaccheda_dev        = "तेन निर्वृत्तम्",
    why_dev               = "(सूत्रम् 5.1.79) तेन निर्वृत्तम्।",
    anuvritti_from        = ('5.1.78',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
