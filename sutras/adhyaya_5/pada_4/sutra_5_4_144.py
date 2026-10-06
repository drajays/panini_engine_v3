"""
5.4.144  विभाषा श्यावारोकाभ्याम्  —  VIDHI

Padaccheda: विभाषा श्याव-अरोकाभ्याम्

विभाषा श्यावारोकाभ्याम् (5.4.144)
Pāṭha: ashtadhyayi.com data.txt row i=54144 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_144_viBAzA_144"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.144", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.144"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.144",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA SyAvArokAByAm",
    text_dev              = "विभाषा श्यावारोकाभ्याम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samAsAntAH vA viBAzA SyAvArokAByAm bahuvrIhO dantasya datf",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समासान्ताः वा विभाषा श्यावारोकाभ्याम् बहुव्रीहौ दन्तस्य दतृ",
    padaccheda_dev        = "विभाषा श्याव-अरोकाभ्याम्",
    why_dev               = "(सूत्रम् 5.4.144) विभाषा श्यावारोकाभ्याम्।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
