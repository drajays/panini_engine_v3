"""
7.3.6  न कर्मव्यतिहारे  —  VIDHI

Padaccheda: न कर्मव्यतिहारे

न कर्मव्यतिहारे (7.3.6)
Pāṭha: ashtadhyayi.com data.txt row i=73006 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_6_na_6"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.6", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.6",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na karmavyatihAre",
    text_dev              = "न कर्मव्यतिहारे",
    samagra_slp1          = "aNgasya na karmavyatihAre vfdDiH acaH YRiti tadDitezu AdeH Ec",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य न कर्मव्यतिहारे वृद्धिः अचः ञ्णिति तद्धितेषु आदेः ऐच्",
    padaccheda_dev        = "न कर्मव्यतिहारे",
    why_dev               = "(सूत्रम् 7.3.6) न कर्मव्यतिहारे।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
