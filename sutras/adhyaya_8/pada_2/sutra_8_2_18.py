"""
8.2.18  कृपो रो लः  —  VIDHI

Padaccheda: कृपः रः लः

कृपो रो लः (8.2.18)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_18_kfpo_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_18_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kfpo ro laH",
    text_dev              = "कृपो रो लः",
    padaccheda_dev        = "कृपः रः लः",
    why_dev               = "(सूत्रम् 8.2.18) कृपो रो लः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
