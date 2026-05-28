"""
6.2.58  आर्यो ब्राह्मणकुमारयोः  —  VIDHI

Padaccheda: आर्यः ब्राह्मण-कुमारयोः

आर्यो ब्राह्मणकुमारयोः (6.2.58)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_58_Aryo_58"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Aryo brAhmaRakumArayoH",
    text_dev              = "आर्यो ब्राह्मणकुमारयोः",
    padaccheda_dev        = "आर्यः ब्राह्मण-कुमारयोः",
    why_dev               = "(सूत्रम् 6.2.58) आर्यो ब्राह्मणकुमारयोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
