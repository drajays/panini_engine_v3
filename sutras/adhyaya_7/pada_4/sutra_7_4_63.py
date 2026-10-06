"""
7.4.63  न कवतेर्यङि  —  VIDHI

Padaccheda: न कवतेः यङि

न कवतेर्यङि (7.4.63)
Pāṭha: ashtadhyayi.com data.txt row i=74063 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_63_na_63"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.63", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.63",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na kavateryaNi",
    text_dev              = "न कवतेर्यङि",
    samagra_slp1          = "aNgasya aByAsasya na kavateH yaNi cuH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अभ्यासस्य न कवतेः यङि चुः",
    padaccheda_dev        = "न कवतेः यङि",
    why_dev               = "(सूत्रम् 7.4.63) न कवतेर्यङि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
