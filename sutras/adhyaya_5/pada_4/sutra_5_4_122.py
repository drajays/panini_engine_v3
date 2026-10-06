"""
5.4.122  नित्यमसिच् प्रजामेधयोः  —  VIDHI

Padaccheda: नित्यम् असिच् प्रजा-मेधयोः

नित्यमसिच् प्रजामेधयोः (5.4.122)
Pāṭha: ashtadhyayi.com data.txt row i=54122 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_122_nityamasic_122"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.122", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.122"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.122",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nityamasic prajAmeDayoH",
    text_dev              = "नित्यमसिच् प्रजामेधयोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samAsAntAH vA nityam asic prajAmeDayoH bahuvrIhO naYduHsuByaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समासान्ताः वा नित्यम् असिच् प्रजामेधयोः बहुव्रीहौ नञ्दुःसुभ्यः",
    padaccheda_dev        = "नित्यम् असिच् प्रजा-मेधयोः",
    why_dev               = "(सूत्रम् 5.4.122) नित्यमसिच् प्रजामेधयोः।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
