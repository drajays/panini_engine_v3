"""
4.3.67  बह्वचोऽन्तोदात्ताट्ठञ्  —  VIDHI

Padaccheda: बहु-अचः अन्त-उदात्तात् ठञ्

बह्वचोऽन्तोदात्ताट्ठञ् (4.3.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_67_bahvacont_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_67_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahvaco'ntodAttAwWaY",
    text_dev              = "बह्वचोऽन्तोदात्ताट्ठञ्",
    padaccheda_dev        = "बहु-अचः अन्त-उदात्तात् ठञ्",
    why_dev               = "(सूत्रम् 4.3.67) बह्वचोऽन्तोदात्ताट्ठञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
