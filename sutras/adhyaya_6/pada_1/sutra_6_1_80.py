"""
6.1.80  धातोस्तन्निमित्तस्यैव  —  VIDHI

Padaccheda: धातोः तन्निमित्तस्य अन्त्यस्य एव

धातोस्तन्निमित्तस्यैव (6.1.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_80_DAtostanni_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "DAtostannimittasyEva",
    text_dev              = "धातोस्तन्निमित्तस्यैव",
    padaccheda_dev        = "धातोः तन्निमित्तस्य अन्त्यस्य एव",
    why_dev               = "(सूत्रम् 6.1.80) धातोस्तन्निमित्तस्यैव।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
