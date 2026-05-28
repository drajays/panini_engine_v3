"""
3.3.44  अभिविधौ भाव इनुण्  —  VIDHI

Padaccheda: अभिविधौ भावे इनुण्

krt-suffix rule: अभिविधौ भाव इनुण्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_44_aBiviDO_44"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_44_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aBiviDO BAva inuR",
    text_dev              = "अभिविधौ भाव इनुण्",
    padaccheda_dev        = "अभिविधौ भावे इनुण्",
    why_dev               = "धातोः प्रत्ययः (३.3.44)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
