"""
4.3.167  हरीतक्यादिभ्यश्च  —  VIDHI

Padaccheda: हरीतकी-आदिभ्यः च

हरीतक्यादिभ्यश्च (4.3.167)
Pāṭha: ashtadhyayi.com data.txt row i=43167 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_167_harItakyAd_167"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.167", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.167"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.167",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "harItakyAdiByaSca",
    text_dev              = "हरीतक्यादिभ्यश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA harItakya-AdiByaH ca tasya vikAraH avayave lup",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा हरीतक्य-आदिभ्यः च तस्य विकारः अवयवे लुप्",
    padaccheda_dev        = "हरीतकी-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.3.167) हरीतक्यादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
