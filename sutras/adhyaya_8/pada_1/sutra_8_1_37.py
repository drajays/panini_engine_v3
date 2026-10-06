"""
8.1.37  पूजायां नानन्तरम्  —  VIDHI

Padaccheda: पूजायाम् न अनन्तरम्

पूजायां नानन्तरम् (8.1.37)
Pāṭha: ashtadhyayi.com data.txt row i=81037 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_37_pUjAyAM_37"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.37", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.37",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "pUjAyAM nAnantaram",
    text_dev              = "पूजायां नानन्तरम्",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO pUjAyAm na anantaram tiN yAvadyaTAByAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ पूजायाम् न अनन्तरम् तिङ् यावद्यथाभ्याम्",
    padaccheda_dev        = "पूजायाम् न अनन्तरम्",
    why_dev               = "(सूत्रम् 8.1.37) पूजायां नानन्तरम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
