"""
4.3.99  गोत्रक्षत्रियाख्येभ्यो बहुलं वुञ्  —  VIDHI

Padaccheda: गोत्र-क्षत्रिय-अख्येभ्यः बहुलम् वुञ्

गोत्रक्षत्रियाख्येभ्यो बहुलं वुञ् (4.3.99)
Pāṭha: ashtadhyayi.com data.txt row i=43099 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_99_gotrakzatr_99"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.99", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gotrakzatriyAKyeByo bahulaM vuY",
    text_dev              = "गोत्रक्षत्रियाख्येभ्यो बहुलं वुञ्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA gotra-kzatriya-AKyeByaH bahulam vuY saH asya BaktiH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा गोत्र-क्षत्रिय-आख्येभ्यः बहुलम् वुञ् सः अस्य भक्तिः",
    padaccheda_dev        = "गोत्र-क्षत्रिय-अख्येभ्यः बहुलम् वुञ्",
    why_dev               = "(सूत्रम् 4.3.99) गोत्रक्षत्रियाख्येभ्यो बहुलं वुञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
