"""
2.3.20  येनाङ्गविकारः  —  VIDHI

Padaccheda: येन अङ्गविकारः

Instrumental marks that by which a bodily defect is caused.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_20_yena_anga"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yenANgavikAraH",
    text_dev              = "येनाङ्गविकारः",
    padaccheda_dev        = "येन अङ्गविकारः",
    why_dev               = "येन अङ्गविकारे (२.३.२०)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
