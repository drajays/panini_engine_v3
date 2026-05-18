"""
7.3.60  अजिवृज्योश्च  —  VIDHI

Padaccheda: अजि-वृज्योः च

अजिवृज्योश्च (7.3.60)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_60_ajivfjyoSc_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_60_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ajivfjyoSca",
    text_dev              = "अजिवृज्योश्च",
    padaccheda_dev        = "अजि-वृज्योः च",
    why_dev               = "(सूत्रम् 7.3.60) अजिवृज्योश्च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
