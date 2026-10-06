"""
8.4.33  वा निंसनिक्षनिन्दाम्  —  VIDHI

Padaccheda: वा निंस-निक्ष-निन्दाम्

वा निंसनिक्षनिन्दाम् (8.4.33)
Pāṭha: ashtadhyayi.com data.txt row i=84033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_33_vA_33"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.33", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA niMsanikzanindAm",
    text_dev              = "वा निंसनिक्षनिन्दाम्",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm vA niMsa-nikza-nindAm razAByAm upasargAt kfti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् वा निंस-निक्ष-निन्दाम् रषाभ्याम् उपसर्गात् कृति",
    padaccheda_dev        = "वा निंस-निक्ष-निन्दाम्",
    why_dev               = "(सूत्रम् 8.4.33) वा निंसनिक्षनिन्दाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
