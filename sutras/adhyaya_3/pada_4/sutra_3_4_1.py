"""
3.4.1  धातुसम्बन्धे प्रत्ययाः  —  VIDHI

Padaccheda: धातु-सम्बन्धे प्रत्ययाः

krt-suffix rule: धातुसम्बन्धे प्रत्ययाः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_1_DAtusamban_1"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("3_4_1_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.1"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.1",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "DAtusambanDe pratyayAH",
    text_dev              = "धातुसम्बन्धे प्रत्ययाः",
    padaccheda_dev        = "धातु-सम्बन्धे प्रत्ययाः",
    why_dev               = "धातोः प्रत्ययः (३.4.1)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
