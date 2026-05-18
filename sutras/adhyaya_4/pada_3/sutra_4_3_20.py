"""
4.3.20  वसन्ताच्च  —  VIDHI

Padaccheda: वसन्तात् च

वसन्ताच्च (4.3.20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_20_vasantAcca_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_20_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vasantAcca",
    text_dev              = "वसन्ताच्च",
    padaccheda_dev        = "वसन्तात् च",
    why_dev               = "(सूत्रम् 4.3.20) वसन्ताच्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
