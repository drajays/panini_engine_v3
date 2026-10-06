"""
8.3.99  एति संज्ञायामगात्  —  VIDHI

Padaccheda: एति संज्ञायाम् अ-गात्

ऐति संज्ञायामगात् (8.3.99)
Pāṭha: ashtadhyayi.com data.txt row i=83099 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_99_Eti_99"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.99", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'eti saMjYAyAmagAt',
    text_dev              = 'एति संज्ञायामगात्',
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH eti saMjYAyAm agAt saH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः एति संज्ञायाम् अगात् सः",
    padaccheda_dev        = "एति संज्ञायाम् अ-गात्",
    why_dev               = "(सूत्रम् 8.3.99) ऐति संज्ञायामगात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
