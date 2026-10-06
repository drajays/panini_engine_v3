"""
8.1.47  जात्वपूर्वम्  —  VIDHI

Padaccheda: जातु अ-पूर्वम्

जात्वपूर्वम् (8.1.47)
Pāṭha: ashtadhyayi.com data.txt row i=81047 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_47_jAtvapUrva_47"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.47", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jAtvapUrvam",
    text_dev              = "जात्वपूर्वम्",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO jAtu apUrvam tiN na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ जातु अपूर्वम् तिङ् न",
    padaccheda_dev        = "जातु अ-पूर्वम्",
    why_dev               = "(सूत्रम् 8.1.47) जात्वपूर्वम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
