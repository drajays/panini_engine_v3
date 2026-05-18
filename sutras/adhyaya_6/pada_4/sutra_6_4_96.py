"""
6.4.96  छादेर्घेऽद्व्युपसर्गस्य  —  VIDHI

Padaccheda: छादेः घे अ-द्वि-उपसर्गस्य

छादेर्घेऽद्व्युपसर्गस्य (6.4.96)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_96_CAderGedv_96"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_96_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CAderGe'dvyupasargasya",
    text_dev              = "छादेर्घेऽद्व्युपसर्गस्य",
    padaccheda_dev        = "छादेः घे अ-द्वि-उपसर्गस्य",
    why_dev               = "(सूत्रम् 6.4.96) छादेर्घेऽद्व्युपसर्गस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
