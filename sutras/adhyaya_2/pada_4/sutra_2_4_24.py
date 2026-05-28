"""
2.4.24  अशाला च  —  VIDHI

Padaccheda: अशाला च

Also ashala (without shala).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_24_asala_ca"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.24", state, "2.4.19")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aSAlA ca",
    text_dev              = "अशाला च",
    padaccheda_dev        = "अशाला च",
    why_dev               = "अशाला च (२.४.२४)।",
    anuvritti_from        = ('2.4.23',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
