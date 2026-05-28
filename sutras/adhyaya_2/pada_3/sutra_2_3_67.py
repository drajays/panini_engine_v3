"""
2.3.67  क्तस्य च वर्तमाने  —  VIDHI

Padaccheda: क्तस्य च वर्त्तमाने

In present context kta also takes kartri/karma as sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_67_vartamane_kta"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_67_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ktasya ca vartamAne",
    text_dev              = "क्तस्य च वर्तमाने",
    padaccheda_dev        = "क्तस्य च वर्त्तमाने",
    why_dev               = "वर्त्तमाने क्तस्य च (२.३.६७)।",
    anuvritti_from        = ('2.3.65',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
