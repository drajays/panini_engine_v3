"""
7.1.26  नेतराच्छन्दसि  —  VIDHI

Padaccheda: न इतरात् छन्दसि

नेतराच्छन्दसि (7.1.26)
Pāṭha: ashtadhyayi.com data.txt row i=71026 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_26_netarAcCan_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.26", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.26",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "netarAcCandasi",
    text_dev              = "नेतराच्छन्दसि",
    samagra_slp1          = "itarAt napuMsakAt aNgAt svamoH adq na Candasi",
    samagra_dev           = "इतरात् नपुंसकात् अङ्गात् स्वमोः अद्ड् न छन्दसि",
    padaccheda_dev        = "न इतरात् छन्दसि",
    why_dev               = "(सूत्रम् 7.1.26) नेतराच्छन्दसि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
