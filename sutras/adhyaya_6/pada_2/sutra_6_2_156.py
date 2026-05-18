"""
6.2.156  ययतोश्चातदर्थे  —  VIDHI

Padaccheda: य-यतोः च अतदर्थे

ययतोश्चातदर्थे (6.2.156)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_156_yayatoScAt_156"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_156_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.156"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.156",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yayatoScAtadarTe",
    text_dev              = "ययतोश्चातदर्थे",
    padaccheda_dev        = "य-यतोः च अतदर्थे",
    why_dev               = "(सूत्रम् 6.2.156) ययतोश्चातदर्थे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
