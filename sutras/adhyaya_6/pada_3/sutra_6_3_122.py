"""
6.3.122  उपसर्गस्य घञ्यमनुष्ये बहुलम्  —  VIDHI

Padaccheda: उपसर्गस्य घञि अमनुष्ये बहुलम्

उपसर्गस्य घञ्यमनुष्ये बहुलम् (6.3.122)
Pāṭha: ashtadhyayi.com data.txt row i=63122 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_122_upasargasy_122"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.122", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.122"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.122",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargasya GaYyamanuzye bahulam",
    text_dev              = "उपसर्गस्य घञ्यमनुष्ये बहुलम्",
    samagra_slp1          = "uttarapade saMhitAyAm upasargasya GaYi amanuzye bahulam dIrGaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे संहितायाम् उपसर्गस्य घञि अमनुष्ये बहुलम् दीर्घः",
    padaccheda_dev        = "उपसर्गस्य घञि अमनुष्ये बहुलम्",
    why_dev               = "(सूत्रम् 6.3.122) उपसर्गस्य घञ्यमनुष्ये बहुलम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
