"""
3.3.2  भूतेऽपि दृश्यन्ते  —  VIDHI

Padaccheda: भूते अपि दृश्यन्ते (क्रियापदम्)

krt-suffix rule: भूतेऽपि दृश्यन्ते
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_2_BUtepi_2"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BUte'pi dfSyante",
    text_dev              = "भूतेऽपि दृश्यन्ते",
    padaccheda_dev        = "भूते अपि दृश्यन्ते (क्रियापदम्)",
    why_dev               = "धातोः प्रत्ययः (३.3.2)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
