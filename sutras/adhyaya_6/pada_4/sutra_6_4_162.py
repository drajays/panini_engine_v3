"""
6.4.162  विभाषर्जोश्छन्दसि  —  VIDHI

Padaccheda: विभाषा ऋजोः छन्दसि

विभाषर्जोश्छन्दसि (6.4.162)
Pāṭha: ashtadhyayi.com data.txt row i=64162 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_162_viBAzarjoS_162"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.162", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.162"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.162",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzarjoSCandasi",
    text_dev              = "विभाषर्जोश्छन्दसि",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya viBAzA fjoH Candasi izWa-iman-Iyassu raH ftaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य विभाषा ऋजोः छन्दसि इष्ठ-इमन्-ईयस्सु रः ऋतः",
    padaccheda_dev        = "विभाषा ऋजोः छन्दसि",
    why_dev               = "(सूत्रम् 6.4.162) विभाषर्जोश्छन्दसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
