"""
8.4.7  अह्नोऽदन्तात्  —  VIDHI

Padaccheda: अह्नः (षष्ठीस्थाने प्रथमा) अत्-अन्तात्

अह्नोऽदन्तात् (8.4.7)
Pāṭha: ashtadhyayi.com data.txt row i=84007 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_7_ahnodantA_7"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.7", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'ahnodantAt',
    text_dev              = 'अह्नोऽदन्तात्',
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm ahnaH adantAt razAByAm pUrvapadAt saMjYAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अह्नः अदन्तात् रषाभ्याम् पूर्वपदात् संज्ञायाम्",
    padaccheda_dev        = "अह्नः (षष्ठीस्थाने प्रथमा) अत्-अन्तात्",
    why_dev               = "(सूत्रम् 8.4.7) अह्नोऽदन्तात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
