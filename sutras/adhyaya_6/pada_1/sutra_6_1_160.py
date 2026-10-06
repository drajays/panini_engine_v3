"""
6.1.160  उञ्छादीनां च  —  VIDHI

Padaccheda: उञ्छ-आदीनाम् च

उञ्छादीनां च (6.1.160)
Pāṭha: ashtadhyayi.com data.txt row i=61160 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_160_uYCAdInAM_160"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.160", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.160"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.160",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uYCAdInAM ca",
    text_dev              = "उञ्छादीनां च",
    samagra_slp1          = "uYCAdInAm ca antaH udAttaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उञ्छादीनाम् च अन्तः उदात्तः",
    padaccheda_dev        = "उञ्छ-आदीनाम् च",
    why_dev               = "(सूत्रम् 6.1.160) उञ्छादीनां च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
