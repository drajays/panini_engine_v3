"""
8.1.38  उपसर्गव्यपेतं च  —  VIDHI

Padaccheda: उपसर्ग-व्यपेतम् च

उपसर्गव्यपेतं च (8.1.38)
Pāṭha: ashtadhyayi.com data.txt row i=81038 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_38_upasargavy_38"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.38", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargavyapetaM ca",
    text_dev              = "उपसर्गव्यपेतं च",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO upasargavyapetam ca tiN na yAvadyaTAByAm pUjAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ उपसर्गव्यपेतम् च तिङ् न यावद्यथाभ्याम् पूजायाम्",
    padaccheda_dev        = "उपसर्ग-व्यपेतम् च",
    why_dev               = "(सूत्रम् 8.1.38) उपसर्गव्यपेतं च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
