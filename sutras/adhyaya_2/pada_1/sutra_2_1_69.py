"""
2.1.69  वर्णो वर्णेन  —  VIDHI

Padaccheda: वर्णः वर्णेन

varṇa with varṇa (by instrumental) forms karmadharaya.
Pāṭha: ashtadhyayi.com data.txt row i=21069 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_69_varna_varnena"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "varRo varRena",
    text_dev              = "वर्णो वर्णेन",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH varRaH varRena samAnADikaraRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः वर्णः वर्णेन समानाधिकरणेन",
    padaccheda_dev        = "वर्णः वर्णेन",
    why_dev               = "वर्णः वर्णेन सह कर्मधारयः (२.१.६९)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
