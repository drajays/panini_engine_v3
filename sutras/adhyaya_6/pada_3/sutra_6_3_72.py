"""
6.3.72  रात्रेः कृति विभाषा  —  VIDHI

Padaccheda: रात्रेः कृति विभाषा

रात्रेः कृति विभाषा (6.3.72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_72_rAtreH_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAtreH kfti viBAzA",
    text_dev              = "रात्रेः कृति विभाषा",
    padaccheda_dev        = "रात्रेः कृति विभाषा",
    why_dev               = "(सूत्रम् 6.3.72) रात्रेः कृति विभाषा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
