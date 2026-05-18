"""
3.1.135  इगुपधज्ञाप्रीकिरः कः  —  VIDHI

Padaccheda: इक्-उपध-ज्ञा-प्री-किरः कः

Krt suffix rule from dhatu: इगुपधज्ञाप्रीकिरः कः (135)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_135_igupaDajYApr_135"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_135_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.135"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.135",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "igupaDajYAprIkiraH kaH",
    text_dev              = "इगुपधज्ञाप्रीकिरः कः",
    padaccheda_dev        = "इक्-उपध-ज्ञा-प्री-किरः कः",
    why_dev               = "धातोः [इगुपधज्ञाप्रीकिरः कः]-प्रत्ययः विहितः (३.१.135)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
