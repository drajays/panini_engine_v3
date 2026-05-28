"""
2.4.55  वा लिटि  —  VIDHI

Padaccheda: वा लिटि

Optionally in lit (perfect).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_55_va_liti"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.55", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA liwi",
    text_dev              = "वा लिटि",
    padaccheda_dev        = "वा लिटि",
    why_dev               = "वा लिटि (२.४.५५)।",
    anuvritti_from        = ('2.4.54',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
