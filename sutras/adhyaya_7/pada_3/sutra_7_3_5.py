"""
7.3.5  न्यग्रोधस्य च केवलस्य  —  VIDHI

Padaccheda: न्यग्रोधस्य च केवलस्य

न्यग्रोधस्य च केवलस्य (7.3.5)
Pāṭha: ashtadhyayi.com data.txt row i=73005 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_5_nyagroDasy_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.5", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nyagroDasya ca kevalasya",
    text_dev              = "न्यग्रोधस्य च केवलस्य",
    samagra_slp1          = "aNgasya nyagroDasya ca kevalasya vfdDiH YRiti acaH AdeH tadDitezu na yvAByAm padAntAByAm Ec",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य न्यग्रोधस्य च केवलस्य वृद्धिः ञ्णिति अचः आदेः तद्धितेषु न य्वाभ्याम् पदान्ताभ्याम् ऐच्",
    padaccheda_dev        = "न्यग्रोधस्य च केवलस्य",
    why_dev               = "(सूत्रम् 7.3.5) न्यग्रोधस्य च केवलस्य।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
