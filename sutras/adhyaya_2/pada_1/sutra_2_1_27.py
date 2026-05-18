"""
2.1.27  सामि  —  VIDHI

Padaccheda: सामि

sami (proximity) with subanta forms avyayibhava compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_27_sami"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_27_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]             = "2.1.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sAmi",
    text_dev              = "सामि",
    padaccheda_dev        = "सामि",
    why_dev               = "सामि-वाचिना सुबन्तेन सह अव्ययीभावः (२.१.२७)।",
    anuvritti_from        = ('2.1.5',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
