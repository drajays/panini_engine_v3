"""
6.1.178  ङ्याश्छन्दसि बहुलम्  —  VIDHI

Padaccheda: ङ्याः छन्दसि बहुलम्

ङ्याश्छन्दसि बहुलम् (6.1.178)
Pāṭha: ashtadhyayi.com data.txt row i=61178 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_178_NyASCandas_178"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.178", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.178"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.178",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "NyASCandasi bahulam",
    text_dev              = "ङ्याश्छन्दसि बहुलम्",
    samagra_slp1          = "NyAH Candasi bahulam antaH udAttaH viBaktiH nAm anyatarasyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "ङ्याः छन्दसि बहुलम् अन्तः उदात्तः विभक्तिः नाम् अन्यतरस्याम्",
    padaccheda_dev        = "ङ्याः छन्दसि बहुलम्",
    why_dev               = "(सूत्रम् 6.1.178) ङ्याश्छन्दसि बहुलम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
