"""
2.1.25  स्वयं क्तेन  —  VIDHI

Padaccheda: स्वयम् क्तेन

svayam with kta-derived adjective forms tatpurusha compound.
Pāṭha: ashtadhyayi.com data.txt row i=21025 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_25_svayam_kta"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svayaM ktena",
    text_dev              = "स्वयं क्तेन",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH svayam ktena dvitIyA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः स्वयम् क्तेन द्वितीया",
    padaccheda_dev        = "स्वयम् क्तेन",
    why_dev               = "स्वयम्-इत्येतस्य क्तान्तेन सह तत्पुरुषः (२.१.२५)।",
    anuvritti_from        = ('2.1.22',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
