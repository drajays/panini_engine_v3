"""
6.1.173  शतुरनुमो नद्यजादी  —  VIDHI

Padaccheda: शतुः अ-नुमः नदी-अच्-आदी

शतुरनुमो नद्यजादी (6.1.173)
Pāṭha: ashtadhyayi.com data.txt row i=61173 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_173_Saturanumo_173"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.173", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.173"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.173",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Saturanumo nadyajAdI",
    text_dev              = "शतुरनुमो नद्यजादी",
    samagra_slp1          = "SatuH anumaH nadI-ajAdI udAttaH antaH viBaktiH antodattAt aYceH Candasi asarvanAmasTAnam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "शतुः अनुमः नदी-अजादी उदात्तः अन्तः विभक्तिः अन्तोदत्तात् अञ्चेः छन्दसि असर्वनामस्थानम्",
    padaccheda_dev        = "शतुः अ-नुमः नदी-अच्-आदी",
    why_dev               = "(सूत्रम् 6.1.173) शतुरनुमो नद्यजादी।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
