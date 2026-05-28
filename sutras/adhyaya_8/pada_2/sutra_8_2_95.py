"""
8.2.95  आम्रेडितं भर्त्सने  —  VIDHI

Padaccheda: आम्रेडितम् भर्त्सने

आम्रेडितं भर्त्सने (8.2.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_95_AmreqitaM_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AmreqitaM Bartsane",
    text_dev              = "आम्रेडितं भर्त्सने",
    padaccheda_dev        = "आम्रेडितम् भर्त्सने",
    why_dev               = "(सूत्रम् 8.2.95) आम्रेडितं भर्त्सने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
