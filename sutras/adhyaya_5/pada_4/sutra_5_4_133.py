"""
5.4.133  वा संज्ञायाम्  —  VIDHI

Padaccheda: वा संज्ञायाम्

वा संज्ञायाम् (5.4.133)
Pāṭha: ashtadhyayi.com data.txt row i=54133 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_133_vA_133"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.133", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.133"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.133",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA saMjYAyAm",
    text_dev              = "वा संज्ञायाम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samAsAntAH vA saMjYAyAm bahuvrIhO anaN DanuzaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समासान्ताः वा संज्ञायाम् बहुव्रीहौ अनङ् धनुषः",
    padaccheda_dev        = "वा संज्ञायाम्",
    why_dev               = "(सूत्रम् 5.4.133) वा संज्ञायाम्।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
