"""
6.3.136  निपातस्य च  —  VIDHI

Padaccheda: निपातस्य च

निपातस्य च (6.3.136)
Pāṭha: ashtadhyayi.com data.txt row i=63136 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_136_nipAtasya_136"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.136", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.136"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.136",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nipAtasya ca",
    text_dev              = "निपातस्य च",
    samagra_slp1          = "uttarapade saMhitAyAm nipAtasya ca dIrGaH fci",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे संहितायाम् निपातस्य च दीर्घः ऋचि",
    padaccheda_dev        = "निपातस्य च",
    why_dev               = "(सूत्रम् 6.3.136) निपातस्य च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
