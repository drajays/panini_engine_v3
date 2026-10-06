"""
4.3.70  पौरोडाशपुरोडाशात् ष्ठन्  —  VIDHI

Padaccheda: पौरोडाश-पुरोडाशात् ष्ठन्

पौरोडाशपुरोडाशात् ष्ठन् (4.3.70)
Pāṭha: ashtadhyayi.com data.txt row i=43070 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_70_pOroqASapu_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.70", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pOroqASapuroqASAt zWan",
    text_dev              = "पौरोडाशपुरोडाशात् ष्ठन्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA pOroqASa-puroqASAt zWan tatra BavaH tasya vyAKyAne vyAKyAtavya-nAmnaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा पौरोडाश-पुरोडाशात् ष्ठन् तत्र भवः तस्य व्याख्याने व्याख्यातव्य-नाम्नः",
    padaccheda_dev        = "पौरोडाश-पुरोडाशात् ष्ठन्",
    why_dev               = "(सूत्रम् 4.3.70) पौरोडाशपुरोडाशात् ष्ठन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
