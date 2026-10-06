"""
8.1.42  पुरा च परीप्सायाम्  —  VIDHI

Padaccheda: पुरा च परीप्सायाम्

पुरा च परीप्सायाम् (8.1.42)
Pāṭha: ashtadhyayi.com data.txt row i=81042 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_42_purA_42"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.42", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "purA ca parIpsAyAm",
    text_dev              = "पुरा च परीप्सायाम्",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO purA ca parIpsAyAm tiN na Seze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ पुरा च परीप्सायाम् तिङ् न शेषे",
    padaccheda_dev        = "पुरा च परीप्सायाम्",
    why_dev               = "(सूत्रम् 8.1.42) पुरा च परीप्सायाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
