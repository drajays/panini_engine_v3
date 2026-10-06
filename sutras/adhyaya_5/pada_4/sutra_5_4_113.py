"""
5.4.113  बहुव्रीहौ सक्थ्यक्ष्णोः स्वाङ्गात् षच्  —  VIDHI

Padaccheda: बहुव्रीहौ सक्थि-अक्ष्णोः स्वाङ्गात् षच्

बहुव्रीहौ सक्थ्यक्ष्णोः स्वाङ्गात् षच् (5.4.113)
Pāṭha: ashtadhyayi.com data.txt row i=54113 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_113_bahuvrIhO_113"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.113", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.113"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.113",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahuvrIhO sakTyakzRoH svANgAt zac",
    text_dev              = "बहुव्रीहौ सक्थ्यक्ष्णोः स्वाङ्गात् षच्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samAsAntAH vA bahuvrIhO sakTyakzRoH svANgAt zac",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समासान्ताः वा बहुव्रीहौ सक्थ्यक्ष्णोः स्वाङ्गात् षच्",
    padaccheda_dev        = "बहुव्रीहौ सक्थि-अक्ष्णोः स्वाङ्गात् षच्",
    why_dev               = "(सूत्रम् 5.4.113) बहुव्रीहौ सक्थ्यक्ष्णोः स्वाङ्गात् षच्।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
