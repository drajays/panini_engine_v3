"""
5.2.55  त्रेः सम्प्रसारणम् च  —  VIDHI

Padaccheda: त्रेः सम्प्रसारणम् च

त्रेः सम्प्रसारणम् च (5.2.55)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_55_treH_55"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_55_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "treH samprasAraRam ca",
    text_dev              = "त्रेः सम्प्रसारणम् च",
    padaccheda_dev        = "त्रेः सम्प्रसारणम् च",
    why_dev               = "(सूत्रम् 5.2.55) त्रेः सम्प्रसारणम् च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
