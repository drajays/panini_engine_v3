"""
5.4.146  ककुदस्यावस्थायां लोपः  —  VIDHI

Padaccheda: ककुदस्य अवस्थायाम् लोपः

ककुदस्यावस्थायां लोपः (5.4.146)
Pāṭha: ashtadhyayi.com data.txt row i=54146 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_146_kakudasyAv_146"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.146", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.146"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.146",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kakudasyAvasTAyAM lopaH",
    text_dev              = "ककुदस्यावस्थायां लोपः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samAsAntAH vA kakudasya avasTAyAm lopaH bahuvrIhO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समासान्ताः वा ककुदस्य अवस्थायाम् लोपः बहुव्रीहौ",
    padaccheda_dev        = "ककुदस्य अवस्थायाम् लोपः",
    why_dev               = "(सूत्रम् 5.4.146) ककुदस्यावस्थायां लोपः।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
