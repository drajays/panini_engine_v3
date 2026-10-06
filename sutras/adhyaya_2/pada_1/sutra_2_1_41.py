"""
2.1.41  सिद्धशुष्कपक्वबन्धैश्च  —  VIDHI

Padaccheda: सिद्ध-शुष्क-पक्व-बन्धैः च

siddha, suska, pakva, bandha with saptami forms tatpurusha compound.
Pāṭha: ashtadhyayi.com data.txt row i=21041 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_41_siddha_pakva"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.41"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sidDaSuzkapakvabanDESca",
    text_dev              = "सिद्धशुष्कपक्वबन्धैश्च",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH sidDa-Suzka-pakva-banDEH ca saptamI",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः सिद्ध-शुष्क-पक्व-बन्धैः च सप्तमी",
    padaccheda_dev        = "सिद्ध-शुष्क-पक्व-बन्धैः च",
    why_dev               = "सिद्ध-शुष्क-पक्व-बन्धैश्च सप्तम्यन्तस्य सह तत्पुरुषः (२.१.४१)।",
    anuvritti_from        = ('2.1.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
