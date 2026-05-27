"""
2.2.17  नित्यं क्रीडाजीविकयोः  —  VIDHI

Padaccheda: नित्यम् क्रीडा-जीविकयोः

In krida and jivika context always tatpurusha.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_17_nitya_krida"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.2.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nityaM krIqAjIvikayoH",
    text_dev              = "नित्यं क्रीडाजीविकयोः",
    padaccheda_dev        = "नित्यम् क्रीडा-जीविकयोः",
    why_dev               = "क्रीडा-जीविका-अर्थे नित्यं तत्पुरुषः (२.२.१७)।",
    anuvritti_from        = ('2.2.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
