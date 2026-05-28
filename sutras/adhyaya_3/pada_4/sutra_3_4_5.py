"""
3.4.5  समुच्चये सामान्यवचनस्य  —  VIDHI

Padaccheda: समुच्चये सामान्यवचनस्य

krt-suffix rule: समुच्चये सामान्यवचनस्य
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_5_samuccaye_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("3_4_5_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samuccaye sAmAnyavacanasya",
    text_dev              = "समुच्चये सामान्यवचनस्य",
    padaccheda_dev        = "समुच्चये सामान्यवचनस्य",
    why_dev               = "धातोः प्रत्ययः (३.4.5)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
