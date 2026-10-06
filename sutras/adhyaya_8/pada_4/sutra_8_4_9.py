"""
8.4.9  पानं देशे  —  VIDHI

Padaccheda: पानम् देशे

पानं देशे (8.4.9)
Pāṭha: ashtadhyayi.com data.txt row i=84009 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_9_pAnaM_9"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.9", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pAnaM deSe",
    text_dev              = "पानं देशे",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm pAnam deSe razAByAm pUrvapadAt saMjYAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् पानम् देशे रषाभ्याम् पूर्वपदात् संज्ञायाम्",
    padaccheda_dev        = "पानम् देशे",
    why_dev               = "(सूत्रम् 8.4.9) पानं देशे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
