"""
2.3.42  पञ्चमी विभक्ते  —  VIDHI

Padaccheda: पञ्चमी विभक्ते

Pancami marks the separated/distinguished item.
Pāṭha: ashtadhyayi.com data.txt row i=23042 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import karaka_gate_eligible

_GATE_KEY: str = "2_3_42_vibhakte_pancami"


def cond(state: State) -> bool:
    return karaka_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paYcamI viBakte",
    text_dev              = "पञ्चमी विभक्ते",
    samagra_slp1          = "anaBihite paYcamI viBakte yataH ca nirDAraRam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अनभिहिते पञ्चमी विभक्ते यतः च निर्धारणम्",
    padaccheda_dev        = "पञ्चमी विभक्ते",
    why_dev               = "विभक्ते पञ्चमी (२.३.४२)।",
    anuvritti_from        = ('2.3.28',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
