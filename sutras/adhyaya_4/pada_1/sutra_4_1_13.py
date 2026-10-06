"""
4.1.13  डाबुभाभ्यामन्यतरस्याम्  —  VIDHI

Padaccheda: डाप् उभाभ्याम् अन्यतरस्याम्

डाबुभाभ्यामन्यतरस्याम् (4.1.13)
Pāṭha: ashtadhyayi.com data.txt row i=41013 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_13_qAbuBAByAm_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.13", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "qAbuBAByAmanyatarasyAm",
    text_dev              = "डाबुभाभ्यामन्यतरस्याम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm qAp uBAByAm anyatarasyAm NIp manaH anaH bahuvrIheH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् डाप् उभाभ्याम् अन्यतरस्याम् ङीप् मनः अनः बहुव्रीहेः",
    padaccheda_dev        = "डाप् उभाभ्याम् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 4.1.13) डाबुभाभ्यामन्यतरस्याम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
