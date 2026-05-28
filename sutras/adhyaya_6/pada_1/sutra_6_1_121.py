"""
6.1.121  अवपथासि च  —  VIDHI

Padaccheda: अवपथासि च

अवपथासि च (6.1.121)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_121_avapaTAsi_121"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_121_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avapaTAsi ca",
    text_dev              = "अवपथासि च",
    padaccheda_dev        = "अवपथासि च",
    why_dev               = "(सूत्रम् 6.1.121) अवपथासि च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
