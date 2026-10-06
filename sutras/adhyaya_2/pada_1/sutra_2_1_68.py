"""
2.1.68  कृत्यतुल्याख्या अजात्या  —  VIDHI

Padaccheda: कृत्य-तुल्याख्याः अजात्या

krtya and tulya-named words with non-jati form karmadharaya.
Pāṭha: ashtadhyayi.com data.txt row i=21068 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_68_krtya_tulya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kftyatulyAKyA ajAtyA",
    text_dev              = "कृत्यतुल्याख्या अजात्या",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH kftya-tulya-AKyAH ajAtyA samAnADikaraRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः कृत्य-तुल्य-आख्याः अजात्या समानाधिकरणेन",
    padaccheda_dev        = "कृत्य-तुल्याख्याः अजात्या",
    why_dev               = "कृत्य-तुल्याख्याः अजात्या कर्मधारये (२.१.६८)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
