"""
2.1.40  सप्तमी शौण्डैः  —  VIDHI

Padaccheda: सप्तमी शौण्डैः

saunda etc. with saptami forms tatpurusha compound.
Pāṭha: ashtadhyayi.com data.txt row i=21040 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_40_saptami_saunda"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saptamI SORqEH",
    text_dev              = "सप्तमी शौण्डैः",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH saptamI SORqEH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः सप्तमी शौण्डैः",
    padaccheda_dev        = "सप्तमी शौण्डैः",
    why_dev               = "सप्तम्यन्तस्य शौण्ड-आदिभिः सह तत्पुरुषः (२.१.४०)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
