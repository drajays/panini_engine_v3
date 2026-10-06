"""
4.1.91  फक्फिञोरन्यतरस्याम्  —  VIDHI

Padaccheda: फक्-फिञोः अन्यतरस्याम्

फक्फिञोरन्यतरस्याम् (4.1.91)
Pāṭha: ashtadhyayi.com data.txt row i=41091 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_91_PakPiYoran_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.91", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "PakPiYoranyatarasyAm",
    text_dev              = "फक्फिञोरन्यतरस्याम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samarTAnAM praTamAdvA prAgdIvyatoR Pak-PiYoH anyatarasyAm aci yUni luk",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समर्थानां प्रथमाद्वा प्राग्दीव्यतोऽण् फक्-फिञोः अन्यतरस्याम् अचि यूनि लुक्",
    padaccheda_dev        = "फक्-फिञोः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 4.1.91) फक्फिञोरन्यतरस्याम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
