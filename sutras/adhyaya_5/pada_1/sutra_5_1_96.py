"""
5.1.96  तत्र च दीयते कार्यं भववत्  —  VIDHI

Padaccheda: तत्र च दीयते (क्रियापदम्) कार्यम् भव-वत्

तत्र च दीयते कार्यं भववत् (5.1.96)
Pāṭha: ashtadhyayi.com data.txt row i=51096 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_96_tatra_96"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.96", state, "5.1.78"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tatra ca dIyate kAryaM Bavavat",
    text_dev              = "तत्र च दीयते कार्यं भववत्",
    samagra_slp1          = "tatra dIyate kAryam  iti kAlAt samarTAnAm praTamAt paraH Bavavat pratyayaH",
    samagra_dev           = "'तत्र दीयते, कार्यम् ' (इति) कालात् समर्थानाम् प्रथमात् परः भववत् प्रत्ययः",
    padaccheda_dev        = "तत्र च दीयते (क्रियापदम्) कार्यम् भव-वत्",
    why_dev               = "(सूत्रम् 5.1.96) तत्र च दीयते कार्यं भववत्।",
    anuvritti_from        = ('5.1.78',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
