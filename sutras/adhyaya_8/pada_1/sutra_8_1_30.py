"""
8.1.30  निपातैर्यद्यदिहन्तकुविन्नेच्चेच्चण्कच्चिद्यत्रयुक्तम्  —  VIDHI

Padaccheda: निपातैः यत्-यदि-हन्त-कुवित्-नेत्-चेत्-चण्-कच्चित्-यत्र-युक्तम्

निपातैर्यद्यदिहन्तकुविन्नेच्चेच्चण्कच्चिद्यत्रयुक्तम् (8.1.30)
Pāṭha: ashtadhyayi.com data.txt row i=81030 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_30_nipAtEryad_30"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.30", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nipAtEryadyadihantakuvinnecceccaRkaccidyatrayuktam",
    text_dev              = "निपातैर्यद्यदिहन्तकुविन्नेच्चेच्चण्कच्चिद्यत्रयुक्तम्",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO nipAtEH yadyadihantakuvinnecceccaRkaccidyatrayuktam tiN na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ निपातैः यद्यदिहन्तकुविन्नेच्चेच्चण्कच्चिद्यत्रयुक्तम् तिङ् न",
    padaccheda_dev        = "निपातैः यत्-यदि-हन्त-कुवित्-नेत्-चेत्-चण्-कच्चित्-यत्र-युक्तम्",
    why_dev               = "(सूत्रम् 8.1.30) निपातैर्यद्यदिहन्तकुविन्नेच्चेच्चण्कच्चिद्यत्रयुक्तम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
