"""
6.3.15  प्रावृट्शरत्कालदिवां जे  —  VIDHI

Padaccheda: प्रावृट्-शरत्-काल-दिवाम् जे

प्रावृट्शरत्कालदिवां जे (6.3.15)
Pāṭha: ashtadhyayi.com data.txt row i=63015 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_15_prAvfwSara_15"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.15", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prAvfwSaratkAladivAM je",
    text_dev              = "प्रावृट्शरत्कालदिवां जे",
    samagra_slp1          = "alug uttarapade prAvfw-Sarat-kAla-divAm je haladantAt saptamyAH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अलुग् उत्तरपदे प्रावृट्-शरत्-काल-दिवाम् जे हलदन्तात् सप्तम्याः",
    padaccheda_dev        = "प्रावृट्-शरत्-काल-दिवाम् जे",
    why_dev               = "(सूत्रम् 6.3.15) प्रावृट्शरत्कालदिवां जे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
