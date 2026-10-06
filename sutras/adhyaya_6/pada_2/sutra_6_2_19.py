"""
6.2.19  न भूवाक्चिद्दिधिषु  —  VIDHI

Padaccheda: न भू-वाक्-चित्-दिधिषु

न भूवाक्चिद्दिधिषु (6.2.19)
Pāṭha: ashtadhyayi.com data.txt row i=62019 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_19_na_19"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.19", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.19",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na BUvAkciddiDizu",
    text_dev              = "न भूवाक्चिद्दिधिषु",
    samagra_slp1          = "na BU-vAk-cit-diDizu pUrvapadam prakftyA tatpuruze patyO ESvarye",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "न भू-वाक्-चित्-दिधिषु पूर्वपदम् प्रकृत्या तत्पुरुषे पत्यौ ऐश्वर्ये",
    padaccheda_dev        = "न भू-वाक्-चित्-दिधिषु",
    why_dev               = "(सूत्रम् 6.2.19) न भूवाक्चिद्दिधिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
