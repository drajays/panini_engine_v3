"""
2.1.54  पापाणके कुत्सितैः  —  VIDHI

Padaccheda: पाप-अणके कुत्सितैः

papanaka with kutsita words forms karmadharaya compound.
Pāṭha: ashtadhyayi.com data.txt row i=21054 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_54_papanaka_kutsita"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pApARake kutsitEH",
    text_dev              = "पापाणके कुत्सितैः",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH pApARake kutsitEH samAnADikaraRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः पापाणके कुत्सितैः समानाधिकरणेन",
    padaccheda_dev        = "पाप-अणके कुत्सितैः",
    why_dev               = "पाप-अणके कुत्सितैः सह कर्मधारयः (२.१.५४)।",
    anuvritti_from        = ('2.1.53',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
