"""
8.1.59  चवायोगे प्रथमा  —  VIDHI

Padaccheda: च-वा-योगे प्रथमा

चवायोगे प्रथमा (8.1.59)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_59_cavAyoge_59"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_59_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cavAyoge praTamA",
    text_dev              = "चवायोगे प्रथमा",
    padaccheda_dev        = "च-वा-योगे प्रथमा",
    why_dev               = "(सूत्रम् 8.1.59) चवायोगे प्रथमा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
