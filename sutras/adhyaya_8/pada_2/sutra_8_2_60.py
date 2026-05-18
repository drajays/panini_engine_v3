"""
8.2.60  ऋणमाधमर्ण्ये  —  VIDHI

Padaccheda: ऋणम् आधमर्ण्ये

ऋणमाधमर्ण्ये (8.2.60)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_60_fRamADamar_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_60_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fRamADamarRye",
    text_dev              = "ऋणमाधमर्ण्ये",
    padaccheda_dev        = "ऋणम् आधमर्ण्ये",
    why_dev               = "(सूत्रम् 8.2.60) ऋणमाधमर्ण्ये।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
