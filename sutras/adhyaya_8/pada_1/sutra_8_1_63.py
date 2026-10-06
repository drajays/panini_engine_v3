"""
8.1.63  चादिलोपे विभाषा  —  VIDHI

Padaccheda: च-आदि-लोपे विभाषा

चादिलोपे विभाषा (8.1.63)
Pāṭha: ashtadhyayi.com data.txt row i=81063 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_63_cAdilope_63"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.63", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cAdilope viBAzA",
    text_dev              = "चादिलोपे विभाषा",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO cAdilope viBAzA tiN na praTamA kziyAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ चादिलोपे विभाषा तिङ् न प्रथमा क्षियायाम्",
    padaccheda_dev        = "च-आदि-लोपे विभाषा",
    why_dev               = "(सूत्रम् 8.1.63) चादिलोपे विभाषा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
