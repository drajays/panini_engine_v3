"""
6.3.123  इकः काशे  —  VIDHI

Padaccheda: इकः काशे

इकः काशे (6.3.123)
Pāṭha: ashtadhyayi.com data.txt row i=63123 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_123_ikaH_123"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.123", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.123"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.123",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ikaH kASe",
    text_dev              = "इकः काशे",
    samagra_slp1          = "uttarapade saMhitAyAm ikaH kASe dIrGaH upasargasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे संहितायाम् इकः काशे दीर्घः उपसर्गस्य",
    padaccheda_dev        = "इकः काशे",
    why_dev               = "(सूत्रम् 6.3.123) इकः काशे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
