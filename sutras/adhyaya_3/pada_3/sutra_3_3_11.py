"""
3.3.11  भाववचनाश्च  —  VIDHI

Padaccheda: भाव-वचनाः च

krt-suffix rule: भाववचनाश्च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_11_BAvavacanA_11"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_11_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BAvavacanASca",
    text_dev              = "भाववचनाश्च",
    padaccheda_dev        = "भाव-वचनाः च",
    why_dev               = "धातोः प्रत्ययः (३.3.11)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
