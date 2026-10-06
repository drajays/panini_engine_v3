"""
2.1.55  उपमानानि सामान्यवचनैः  —  VIDHI

Padaccheda: उपमानानि सामान्य-वचनैः

Comparison bases (upamana) with samanya-vacana form karmadharaya.
Pāṭha: ashtadhyayi.com data.txt row i=21055 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_55_upamana_samanya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upamAnAni sAmAnyavacanEH",
    text_dev              = "उपमानानि सामान्यवचनैः",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH upamAnAni sAmAnya-vacanEH samAnADikaraRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः उपमानानि सामान्य-वचनैः समानाधिकरणेन",
    padaccheda_dev        = "उपमानानि सामान्य-वचनैः",
    why_dev               = "उपमानानि सामान्य-वचनैः सह कर्मधारयः (२.१.५५)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
