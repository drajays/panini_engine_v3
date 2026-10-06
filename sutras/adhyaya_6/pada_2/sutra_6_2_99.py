"""
6.2.99  पुरे प्राचाम्  —  VIDHI

Padaccheda: पुरे प्राचाम्

पुरे प्राचाम् (6.2.99)
Pāṭha: ashtadhyayi.com data.txt row i=62099 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_99_pure_99"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.99", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pure prAcAm",
    text_dev              = "पुरे प्राचाम्",
    samagra_slp1          = "udAttaH antaH pure prAcAm pUrvapadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः अन्तः पुरे प्राचाम् पूर्वपदम्",
    padaccheda_dev        = "पुरे प्राचाम्",
    why_dev               = "(सूत्रम् 6.2.99) पुरे प्राचाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
