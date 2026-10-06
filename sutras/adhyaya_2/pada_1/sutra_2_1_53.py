"""
2.1.53  कुत्सितानि कुत्सनैः  —  VIDHI

Padaccheda: कुत्सितानि कुत्सनैः

Despicable things with disparaging words form karmadharaya.
Pāṭha: ashtadhyayi.com data.txt row i=21053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_53_kutsita_kutsana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kutsitAni kutsanEH",
    text_dev              = "कुत्सितानि कुत्सनैः",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH kutsitAni kutsanEH samAnADikaraRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः कुत्सितानि कुत्सनैः समानाधिकरणेन",
    padaccheda_dev        = "कुत्सितानि कुत्सनैः",
    why_dev               = "कुत्सितानां कुत्सनैः सह कर्मधारयः (२.१.५३)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
