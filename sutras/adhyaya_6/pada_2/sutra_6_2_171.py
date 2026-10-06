"""
6.2.171  वा जाते  —  VIDHI

Padaccheda: वा जाते

वा जाते (6.2.171)
Pāṭha: ashtadhyayi.com data.txt row i=62171 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_171_vA_171"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.171", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.171"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.171",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA jAte",
    text_dev              = "वा जाते",
    samagra_slp1          = "uttarapadAdiH antaH vA jAte bahuvrIhO jAti-kAla-suKAdiByaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः वा जाते बहुव्रीहौ जाति-काल-सुखादिभ्यः",
    padaccheda_dev        = "वा जाते",
    why_dev               = "(सूत्रम् 6.2.171) वा जाते।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
