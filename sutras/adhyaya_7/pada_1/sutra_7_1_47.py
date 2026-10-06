"""
7.1.47  क्त्वो यक्  —  VIDHI

Padaccheda: क्त्वः यक्

क्त्वो यक् (7.1.47)
Pāṭha: ashtadhyayi.com data.txt row i=71047 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_47_ktvo_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.47", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ktvo yak",
    text_dev              = "क्त्वो यक्",
    samagra_slp1          = "aNgasya ktvaH yak Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य क्त्वः यक् छन्दसि",
    padaccheda_dev        = "क्त्वः यक्",
    why_dev               = "(सूत्रम् 7.1.47) क्त्वो यक्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
