"""
6.1.27  शृतं पाके  —  VIDHI

Padaccheda: शृतम् पाके

शृतं पाके (6.1.27)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_27_SftaM_27"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_27_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SftaM pAke",
    text_dev              = "शृतं पाके",
    padaccheda_dev        = "शृतम् पाके",
    why_dev               = "(सूत्रम् 6.1.27) शृतं पाके।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
