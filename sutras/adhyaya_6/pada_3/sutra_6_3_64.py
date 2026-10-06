"""
6.3.64  त्वे च  —  VIDHI

Padaccheda: त्वे च

त्वे च (6.3.64)
Pāṭha: ashtadhyayi.com data.txt row i=63064 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_64_tve_64"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.64", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tve ca",
    text_dev              = "त्वे च",
    samagra_slp1          = "uttarapade tve ca treH hrasvaH Ni-ApoH bahulam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे त्वे च त्रेः ह्रस्वः ङि-आपोः बहुलम्",
    padaccheda_dev        = "त्वे च",
    why_dev               = "(सूत्रम् 6.3.64) त्वे च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
