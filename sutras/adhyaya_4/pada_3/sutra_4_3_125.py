"""
4.3.125  द्वन्द्वाद्वुन् वैरमैथुनिकयोः  —  VIDHI

Padaccheda: द्वन्द्वात् वुन् वैर-मैथुनिकयोः

द्वंद्वाद्वुन् वैरमैथुनिकयोः (4.3.125)
Pāṭha: ashtadhyayi.com data.txt row i=43125 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_125_dvaMdvAdvu_125"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.125", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'dvandvAdvun vEramETunikayoH',
    text_dev              = 'द्वन्द्वाद्वुन् वैरमैथुनिकयोः',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA dvandvAt vun vEra-mETunikayoH tasya idam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा द्वन्द्वात् वुन् वैर-मैथुनिकयोः तस्य इदम्",
    padaccheda_dev        = "द्वन्द्वात् वुन् वैर-मैथुनिकयोः",
    why_dev               = "(सूत्रम् 4.3.125) द्वंद्वाद्वुन् वैरमैथुनिकयोः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
