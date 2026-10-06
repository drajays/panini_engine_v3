"""
2.1.30  तृतीया तत्कृतार्थेन गुणवचनेन  —  VIDHI

Padaccheda: तृतीया तत्कृत (लुप्ततृतीयान्तनिर्देशः) अर्थेन गुण-वचनेन

Tritiya with quality-denoting words forms tatpurusha compound.
Pāṭha: ashtadhyayi.com data.txt row i=21030 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_30_tritiya_guna"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tftIyA tatkftArTena guRavacanena",
    text_dev              = "तृतीया तत्कृतार्थेन गुणवचनेन",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH tftIyA tatkfta-arTena guRa-vacanena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः तृतीया तत्कृत-अर्थेन गुण-वचनेन",
    padaccheda_dev        = "तृतीया तत्कृत (लुप्ततृतीयान्तनिर्देशः) अर्थेन गुण-वचनेन",
    why_dev               = "तृतीयान्तस्य तत्कृत-अर्थेन गुण-वचनेन सह तत्पुरुषः (२.१.३०)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
