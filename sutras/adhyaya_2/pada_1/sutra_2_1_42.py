"""
2.1.42  ध्वाङ्क्षेण क्षेपे  —  VIDHI

Padaccheda: ध्वाङ्क्षेण क्षेपे

dhvanksa in ksepa context with saptami forms tatpurusha compound.
Pāṭha: ashtadhyayi.com data.txt row i=21042 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_42_dhvanksa_ksepe"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "DvANkzeRa kzepe",
    text_dev              = "ध्वाङ्क्षेण क्षेपे",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH DvANkzeRa kzepe saptamI",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः ध्वाङ्क्षेण क्षेपे सप्तमी",
    padaccheda_dev        = "ध्वाङ्क्षेण क्षेपे",
    why_dev               = "ध्वाङ्क्षेण क्षेपे सप्तम्यन्तस्य सह तत्पुरुषः (२.१.४२)।",
    anuvritti_from        = ('2.1.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
