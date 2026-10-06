"""
8.1.44  किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम्  —  VIDHI

Padaccheda: किम् क्रियाप्रश्ने अन्-उपसर्गम् अप्रतिषिद्धम्

किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम् (8.1.44)
Pāṭha: ashtadhyayi.com data.txt row i=81044 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_44_kiM_44"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.44", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'kiM kriyApraSnenupasargamapratizidDam',
    text_dev              = 'किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम्',
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO kim kriyApraSne anupasargam apratizidDam tiN na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ किम् क्रियाप्रश्ने अनुपसर्गम् अप्रतिषिद्धम् तिङ् न",
    padaccheda_dev        = "किम् क्रियाप्रश्ने अन्-उपसर्गम् अप्रतिषिद्धम्",
    why_dev               = "(सूत्रम् 8.1.44) किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
