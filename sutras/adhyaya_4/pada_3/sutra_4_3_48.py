"""
4.3.48  कलाप्यश्वत्थयवबुसाद्वुन्  —  VIDHI

Padaccheda: कलापि-अश्वत्थ-यवबुसात् वुन्

कलाप्यश्वत्थयवबुसाद्वुन् (4.3.48)
Pāṭha: ashtadhyayi.com data.txt row i=43048 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_48_kalApyaSva_48"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.48", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kalApyaSvatTayavabusAdvun",
    text_dev              = "कलाप्यश्वत्थयवबुसाद्वुन्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA kalApi-aSvatTa-yava-busAt vun tatra kAlAt deyam fRe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा कलापि-अश्वत्थ-यव-बुसात् वुन् तत्र कालात् देयम् ऋणे",
    padaccheda_dev        = "कलापि-अश्वत्थ-यवबुसात् वुन्",
    why_dev               = "(सूत्रम् 4.3.48) कलाप्यश्वत्थयवबुसाद्वुन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
