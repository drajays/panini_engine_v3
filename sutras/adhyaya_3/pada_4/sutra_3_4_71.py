"""
3.4.71  अदिकर्मणि क्तः कर्तरि च  —  VIDHI

Padaccheda: आदिकर्मणि क्तः कर्तरि च

krt-suffix rule: अदिकर्मणि क्तः कर्तरि च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_71_adikarmaRi_71"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.71"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "adikarmaRi ktaH kartari ca",
    text_dev              = "अदिकर्मणि क्तः कर्तरि च",
    padaccheda_dev        = "आदिकर्मणि क्तः कर्तरि च",
    why_dev               = "धातोः प्रत्ययः (३.4.71)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
