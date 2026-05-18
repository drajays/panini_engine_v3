"""
2.4.49  गाङ् लिटि  —  VIDHI

Padaccheda: गाङ् लिटि

gang root in lit (perfect).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_49_gang_liti"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_49_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gAN liwi",
    text_dev              = "गाङ् लिटि",
    padaccheda_dev        = "गाङ् लिटि",
    why_dev               = "गाङ् लिटि (२.४.४९)।",
    anuvritti_from        = ('2.4.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
