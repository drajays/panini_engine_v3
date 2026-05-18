"""
8.3.18  व्योर्लघुप्रयत्नतरः शाकटायनस्य  —  VIDHI

Padaccheda: व्योः · लघुप्रयत्नतरः · शाकटायनस्य

व्योर्लघुप्रयत्नतरः शाकटायनस्य (8.3.18)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_18_vyorlaGupr_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_18_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vyorlaGuprayatnataraH SAkawAyanasya",
    text_dev              = "व्योर्लघुप्रयत्नतरः शाकटायनस्य",
    padaccheda_dev        = "व्योः · लघुप्रयत्नतरः · शाकटायनस्य",
    why_dev               = "(सूत्रम् 8.3.18) व्योर्लघुप्रयत्नतरः शाकटायनस्य।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
