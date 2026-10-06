"""
4.3.164  प्लक्षादिभ्योऽण्  —  VIDHI

Padaccheda: प्लक्ष-आदिभ्यः अण्

प्लक्षादिभ्योऽण् (4.3.164)
Pāṭha: ashtadhyayi.com data.txt row i=43164 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_164_plakzAdiBy_164"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.164", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.164"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.164",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'plakzAdiByoR',
    text_dev              = 'प्लक्षादिभ्योऽण्',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA plakza-AdiByaH aR tasya vikAraH avayave Pale",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा प्लक्ष-आदिभ्यः अण् तस्य विकारः अवयवे फले",
    padaccheda_dev        = "प्लक्ष-आदिभ्यः अण्",
    why_dev               = "(सूत्रम् 4.3.164) प्लक्षादिभ्योऽण्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
