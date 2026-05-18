"""
4.1.63  जातेरस्त्रीविषयादयोपधात्  —  VIDHI

Padaccheda: जातेः अ-स्त्री-विषयात् अ-य-उपधात्

जातेरस्त्रीविषयादयोपधात् (4.1.63)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_63_jAterastrI_63"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_63_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jAterastrIvizayAdayopaDAt",
    text_dev              = "जातेरस्त्रीविषयादयोपधात्",
    padaccheda_dev        = "जातेः अ-स्त्री-विषयात् अ-य-उपधात्",
    why_dev               = "(सूत्रम् 4.1.63) जातेरस्त्रीविषयादयोपधात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
