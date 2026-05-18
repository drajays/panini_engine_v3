"""
4.1.134  मातृष्वसुश्च  —  VIDHI

Padaccheda: मातृष्वसुः च

मातृष्वसुश्च (4.1.134)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_134_mAtfzvasuS_134"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_134_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.134"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.134",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mAtfzvasuSca",
    text_dev              = "मातृष्वसुश्च",
    padaccheda_dev        = "मातृष्वसुः च",
    why_dev               = "(सूत्रम् 4.1.134) मातृष्वसुश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
