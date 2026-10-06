"""
4.1.121  द्व्यचः  —  VIDHI

Padaccheda: द्वि-अचः

द्व्यचः (4.1.121)
Pāṭha: ashtadhyayi.com data.txt row i=41121 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_121_dvyacaH_121"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.121", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvyacaH",
    text_dev              = "द्व्यचः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samarTAnAM praTamAdvA prAgdIvyatoR dvyacaH apatyam tasya strIByaH Qak",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समर्थानां प्रथमाद्वा प्राग्दीव्यतोऽण् द्व्यचः अपत्यम् तस्य स्त्रीभ्यः ढक्",
    padaccheda_dev        = "द्वि-अचः",
    why_dev               = "(सूत्रम् 4.1.121) द्व्यचः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
