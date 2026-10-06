"""
4.4.2  तेन दीव्यति खनति जयति जितम्  —  VIDHI

Padaccheda: तेन दीव्यति (क्रियापदम्) खनति (क्रियापदम्) जयति (क्रियापदम्) जितम्

तेन दीव्यति खनति जयति जितम् (4.4.2)
Pāṭha: ashtadhyayi.com data.txt row i=44002 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_2_tena_2"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.2", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tena dIvyati Kanati jayati jitam",
    text_dev              = "तेन दीव्यति खनति जयति जितम्",
    samagra_slp1          = "tena dIvyati Kanati jayati jitam iti samarTAnAm praTamAt paraH Wak ",
    samagra_dev           = "'तेन दीव्यति, खनति, जयति, जितम्' (इति) समर्थानाम् प्रथमात् परः ठक् ।",
    padaccheda_dev        = "तेन दीव्यति (क्रियापदम्) खनति (क्रियापदम्) जयति (क्रियापदम्) जितम्",
    why_dev               = "(सूत्रम् 4.4.2) तेन दीव्यति खनति जयति जितम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
