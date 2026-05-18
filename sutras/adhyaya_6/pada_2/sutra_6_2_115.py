"""
6.2.115  शृङ्गमवस्थायां च  —  VIDHI

Padaccheda: शृङ्गम् अवस्थायाम् च

शृङ्गमवस्थायां च (6.2.115)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_115_SfNgamavas_115"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_115_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SfNgamavasTAyAM ca",
    text_dev              = "शृङ्गमवस्थायां च",
    padaccheda_dev        = "शृङ्गम् अवस्थायाम् च",
    why_dev               = "(सूत्रम् 6.2.115) शृङ्गमवस्थायां च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
