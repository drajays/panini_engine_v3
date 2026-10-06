"""
8.1.52  लोट् च  —  VIDHI

Padaccheda: लोट् च

लोट् च (8.1.52)
Pāṭha: ashtadhyayi.com data.txt row i=81052 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_52_low_52"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.52", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "low ca",
    text_dev              = "लोट् च",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO low ca tiN na gatyarTalowA cet kArakam sarvAnyat",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ लोट् च तिङ् न गत्यर्थलोटा चेत् कारकम् सर्वान्यत्",
    padaccheda_dev        = "लोट् च",
    why_dev               = "(सूत्रम् 8.1.52) लोट् च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
