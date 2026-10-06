"""
7.3.59  न क्वादेः  —  VIDHI

Padaccheda: न कु-आदेः

न क्वादेः (7.3.59)
Pāṭha: ashtadhyayi.com data.txt row i=73059 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_59_na_59"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.59", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.59",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na kvAdeH",
    text_dev              = "न क्वादेः",
    samagra_slp1          = "aNgasya na kvAdeH cajoH ku",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य न क्वादेः चजोः कु",
    padaccheda_dev        = "न कु-आदेः",
    why_dev               = "(सूत्रम् 7.3.59) न क्वादेः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
