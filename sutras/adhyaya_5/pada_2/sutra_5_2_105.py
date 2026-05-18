"""
5.2.105  देशे लुबिलचौ च  —  VIDHI

Padaccheda: देशे लुप्-इलचौ च

देशे लुबिलचौ च (5.2.105)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_105_deSe_105"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_105_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.105"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "deSe lubilacO ca",
    text_dev              = "देशे लुबिलचौ च",
    padaccheda_dev        = "देशे लुप्-इलचौ च",
    why_dev               = "(सूत्रम् 5.2.105) देशे लुबिलचौ च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
