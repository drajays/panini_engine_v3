"""
8.1.57  चनचिदिवगोत्रादितद्धिताम्रेडितेष्वगतेः  —  VIDHI

Padaccheda: चन-चित्-इव-गोत्र-आदि-तद्धित-आम्रेडितेषु अ-गतेः

चनचिदिवगोत्रादितद्धिताम्रेडितेष्वगतेः (8.1.57)
Pāṭha: ashtadhyayi.com data.txt row i=81057 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_57_canacidiva_57"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.57", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "canacidivagotrAditadDitAmreqitezvagateH",
    text_dev              = "चनचिदिवगोत्रादितद्धिताम्रेडितेष्वगतेः",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO canacidivagotrAditadDitAmreqitezu AgateH tiN na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ चनचिदिवगोत्रादितद्धिताम्रेडितेषु आगतेः तिङ् न",
    padaccheda_dev        = "चन-चित्-इव-गोत्र-आदि-तद्धित-आम्रेडितेषु अ-गतेः",
    why_dev               = "(सूत्रम् 8.1.57) चनचिदिवगोत्रादितद्धिताम्रेडितेष्वगतेः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
