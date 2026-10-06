"""
6.2.100  अरिष्टगौडपूर्वे च  —  VIDHI

Padaccheda: अरिष्ट-गौड-पूर्वे च

अरिष्टगौडपूर्वे च (6.2.100)
Pāṭha: ashtadhyayi.com data.txt row i=62100 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_100_arizwagOqa_100"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.100", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.100"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arizwagOqapUrve ca",
    text_dev              = "अरिष्टगौडपूर्वे च",
    samagra_slp1          = "udAttaH antaH arizwa-gOqapUrve ca pUrvapadam pure",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः अन्तः अरिष्ट-गौडपूर्वे च पूर्वपदम् पुरे",
    padaccheda_dev        = "अरिष्ट-गौड-पूर्वे च",
    why_dev               = "(सूत्रम् 6.2.100) अरिष्टगौडपूर्वे च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
