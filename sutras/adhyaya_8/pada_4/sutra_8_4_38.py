"""
8.4.38  पदव्यवायेऽपि  —  VIDHI

Padaccheda: पद-व्यवाये अपि

पदव्यवायेऽपि (8.4.38)
Pāṭha: ashtadhyayi.com data.txt row i=84038 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_38_padavyavAy_38"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.38", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'padavyavAyepi',
    text_dev              = 'पदव्यवायेऽपि',
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm pada-vyavAye api razAByAm na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् पद-व्यवाये अपि रषाभ्याम् न",
    padaccheda_dev        = "पद-व्यवाये अपि",
    why_dev               = "(सूत्रम् 8.4.38) पदव्यवायेऽपि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
