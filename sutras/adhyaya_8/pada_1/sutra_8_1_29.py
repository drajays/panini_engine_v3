"""
8.1.29  न लुट्  —  VIDHI

Padaccheda: न लुट्

न लुट् (8.1.29)
Pāṭha: ashtadhyayi.com data.txt row i=81029 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_29_na_29"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.29", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.29",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na luw",
    text_dev              = "न लुट्",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO na luw tiN",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ न लुट् तिङ्",
    padaccheda_dev        = "न लुट्",
    why_dev               = "(सूत्रम् 8.1.29) न लुट्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
