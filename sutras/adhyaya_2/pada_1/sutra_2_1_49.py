"""
2.1.49  पूर्वकालैकसर्वजरत्पुराणनवकेवलाः समानाधिकरणेन  —  VIDHI

Padaccheda: पूर्वकाल-एक-सर्व-जरत्-पुराण-नव-केवलाः समानाधिकरणेन

purvakala, eka, sarva, jarat etc. with samana-adhikarana form karmadharaya.
Pāṭha: ashtadhyayi.com data.txt row i=21049 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_49_purvakala_samana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrvakAlEkasarvajaratpurARanavakevalAH samAnADikaraRena",
    text_dev              = "पूर्वकालैकसर्वजरत्पुराणनवकेवलाः समानाधिकरणेन",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH pUrvakAla-eka-sarva-jarat-purARa-nava-kevalAH samAna-aDikaraRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः पूर्वकाल-एक-सर्व-जरत्-पुराण-नव-केवलाः समान-अधिकरणेन",
    padaccheda_dev        = "पूर्वकाल-एक-सर्व-जरत्-पुराण-नव-केवलाः समानाधिकरणेन",
    why_dev               = "पूर्वकाल-एक-सर्व-आदयः समानाधिकरणेन सह कर्मधारयः (२.१.४९)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
