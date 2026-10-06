"""
8.1.45  लोपे विभाषा  —  VIDHI

Padaccheda: लोपे विभाषा

लोपे विभाषा (8.1.45)
Pāṭha: ashtadhyayi.com data.txt row i=81045 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_45_lope_45"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.45", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lope viBAzA",
    text_dev              = "लोपे विभाषा",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO lope viBAzA tiN na kim kriyApraSne anupasargam apratizidDam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ लोपे विभाषा तिङ् न किम् क्रियाप्रश्ने अनुपसर्गम् अप्रतिषिद्धम्",
    padaccheda_dev        = "लोपे विभाषा",
    why_dev               = "(सूत्रम् 8.1.45) लोपे विभाषा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
