"""
7.3.31  यथातथयथापुरयोः पर्यायेण  —  VIDHI

Padaccheda: यथातथ-यथापुरयोः पर्यायेण

यथातथयथापुरयोः पर्यायेण (7.3.31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_31_yaTAtaTaya_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaTAtaTayaTApurayoH paryAyeRa",
    text_dev              = "यथातथयथापुरयोः पर्यायेण",
    padaccheda_dev        = "यथातथ-यथापुरयोः पर्यायेण",
    why_dev               = "(सूत्रम् 7.3.31) यथातथयथापुरयोः पर्यायेण।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
