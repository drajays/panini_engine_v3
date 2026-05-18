"""
7.2.3  वदव्रजहलन्तस्याचः  —  VIDHI

Padaccheda: वद-व्रज-हल्-अन्तस्य अचः

वदव्रजहलन्तस्याचः (7.2.3)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_3_vadavrajah_3"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_3_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vadavrajahalantasyAcaH",
    text_dev              = "वदव्रजहलन्तस्याचः",
    padaccheda_dev        = "वद-व्रज-हल्-अन्तस्य अचः",
    why_dev               = "(सूत्रम् 7.2.3) वदव्रजहलन्तस्याचः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
