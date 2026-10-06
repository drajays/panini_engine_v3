"""
7.4.30  यङि च  —  VIDHI

Padaccheda: यङि च

यङि च (7.4.30)
Pāṭha: ashtadhyayi.com data.txt row i=74030 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_30_yaNi_30"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.30", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaNi ca",
    text_dev              = "यङि च",
    samagra_slp1          = "aNgasya yaNi ca ftaH guRaH artisaMyogAdyoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य यङि च ऋतः गुणः अर्तिसंयोगाद्योः",
    padaccheda_dev        = "यङि च",
    why_dev               = "(सूत्रम् 7.4.30) यङि च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
