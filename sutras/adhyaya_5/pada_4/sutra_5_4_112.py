"""
5.4.112  गिरेश्च सेनकस्य  —  VIDHI

Padaccheda: गिरेः च सेनकस्य

गिरेश्च सेनकस्य (5.4.112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_112_gireSca_112"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_112_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.112"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gireSca senakasya",
    text_dev              = "गिरेश्च सेनकस्य",
    padaccheda_dev        = "गिरेः च सेनकस्य",
    why_dev               = "(सूत्रम् 5.4.112) गिरेश्च सेनकस्य।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
