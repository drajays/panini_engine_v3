"""
8.1.36  यावद्यथाभ्याम्  —  VIDHI

Padaccheda: यावत्-यथाभ्याम्

यावद्यथाभ्याम् (8.1.36)
Pāṭha: ashtadhyayi.com data.txt row i=81036 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_36_yAvadyaTAB_36"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.36", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yAvadyaTAByAm",
    text_dev              = "यावद्यथाभ्याम्",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO yAvadyaTAByAm tiN na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ यावद्यथाभ्याम् तिङ् न",
    padaccheda_dev        = "यावत्-यथाभ्याम्",
    why_dev               = "(सूत्रम् 8.1.36) यावद्यथाभ्याम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
