"""
8.4.27  नश्च धातुस्थोरुषुभ्यः  —  VIDHI

Padaccheda: नः (लुप्तषष्ठ्यन्तनिर्देशः) च धातु-स्थ-उरु-षुभ्यः

नश्च धातुस्थोरुषुभ्यः (8.4.27)
Pāṭha: ashtadhyayi.com data.txt row i=84027 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_27_naSca_27"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.27", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "naSca DAtusToruzuByaH",
    text_dev              = "नश्च धातुस्थोरुषुभ्यः",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm naH ca DAtusTa-uru-zuByaH razAByAm Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् नः च धातुस्थ-उरु-षुभ्यः रषाभ्याम् छन्दसि",
    padaccheda_dev        = "नः (लुप्तषष्ठ्यन्तनिर्देशः) च धातु-स्थ-उरु-षुभ्यः",
    why_dev               = "(सूत्रम् 8.4.27) नश्च धातुस्थोरुषुभ्यः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
