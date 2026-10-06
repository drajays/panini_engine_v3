"""
7.4.5  तिष्ठतेरित्  —  VIDHI

Padaccheda: तिष्ठतेः इत्

तिष्ठतेरित् (7.4.5)
Pāṭha: ashtadhyayi.com data.txt row i=74005 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_5_tizWaterit_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.5", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tizWaterit",
    text_dev              = "तिष्ठतेरित्",
    samagra_slp1          = "aNgasya tizWateH it RO caNi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य तिष्ठतेः इत् णौ चङि",
    padaccheda_dev        = "तिष्ठतेः इत्",
    why_dev               = "(सूत्रम् 7.4.5) तिष्ठतेरित्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
