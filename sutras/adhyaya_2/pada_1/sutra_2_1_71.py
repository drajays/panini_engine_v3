"""
2.1.71  चतुष्पादो गर्भिण्या  —  VIDHI

Padaccheda: चतुष्पादः गर्भिण्या

quadruped with pregnant (garbhini) forms karmadharaya compound.
Pāṭha: ashtadhyayi.com data.txt row i=21071 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_71_catuspada_garbhini"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.71"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "catuzpAdo garBiRyA",
    text_dev              = "चतुष्पादो गर्भिण्या",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH catuzpAdaH garBiRyA samAnADikaraRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः चतुष्पादः गर्भिण्या समानाधिकरणेन",
    padaccheda_dev        = "चतुष्पादः गर्भिण्या",
    why_dev               = "चतुष्पादः गर्भिण्या सह कर्मधारयः (२.१.७१)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
