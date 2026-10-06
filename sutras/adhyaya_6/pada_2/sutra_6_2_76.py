"""
6.2.76  शिल्पिनि चाकृञः  —  VIDHI

Padaccheda: शिल्पिनि च अ-कृञः

शिल्पिनि चाकृञः (6.2.76)
Pāṭha: ashtadhyayi.com data.txt row i=62076 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_76_Silpini_76"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.76", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.76"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.76",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Silpini cAkfYaH",
    text_dev              = "शिल्पिनि चाकृञः",
    samagra_slp1          = "AdiH udAttaH Silpini ca akfYaH pUrvapadam aRi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आदिः उदात्तः शिल्पिनि च अकृञः पूर्वपदम् अणि",
    padaccheda_dev        = "शिल्पिनि च अ-कृञः",
    why_dev               = "(सूत्रम् 6.2.76) शिल्पिनि चाकृञः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
