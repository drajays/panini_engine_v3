"""
4.2.109  उदीच्यग्रामाच्च बह्वचोऽन्तोदात्तात्  —  VIDHI

Padaccheda: उदीच्य-ग्रामात् च बहु-अचः अन्त-उदात्तात्

उदीच्यग्रामाच्च बह्वचोऽन्तोदात्तात् (4.2.109)
Pāṭha: ashtadhyayi.com data.txt row i=42109 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_109_udIcyagrAm_109"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.109", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.109"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.109",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'udIcyagrAmAcca bahvacontodAttAt',
    text_dev              = 'उदीच्यग्रामाच्च बह्वचोऽन्तोदात्तात्',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA udIcya-grAmAt ca bahu-acaH anta-udAttAt aY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा उदीच्य-ग्रामात् च बहु-अचः अन्त-उदात्तात् अञ्",
    padaccheda_dev        = "उदीच्य-ग्रामात् च बहु-अचः अन्त-उदात्तात्",
    why_dev               = "(सूत्रम् 4.2.109) उदीच्यग्रामाच्च बह्वचोऽन्तोदात्तात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
