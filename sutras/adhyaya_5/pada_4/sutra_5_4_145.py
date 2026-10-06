"""
5.4.145  अग्रान्तशुद्धशुभ्रवृषवराहेभ्यश्च  —  VIDHI

Padaccheda: अग्र-अन्त-शुद्ध-शुभ्र-वृष-वराहेभ्यः च

अग्रान्तशुद्धशुभ्रवृषवराहेभ्यश्च (5.4.145)
Pāṭha: ashtadhyayi.com data.txt row i=54145 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_145_agrAntaSud_145"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.145", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.145"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.145",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "agrAntaSudDaSuBravfzavarAheByaSca",
    text_dev              = "अग्रान्तशुद्धशुभ्रवृषवराहेभ्यश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samAsAntAH vA agrAntaSudDaSuBravfzavarAheByaH ca bahuvrIhO dantasya datf viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समासान्ताः वा अग्रान्तशुद्धशुभ्रवृषवराहेभ्यः च बहुव्रीहौ दन्तस्य दतृ विभाषा",
    padaccheda_dev        = "अग्र-अन्त-शुद्ध-शुभ्र-वृष-वराहेभ्यः च",
    why_dev               = "(सूत्रम् 5.4.145) अग्रान्तशुद्धशुभ्रवृषवराहेभ्यश्च।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
