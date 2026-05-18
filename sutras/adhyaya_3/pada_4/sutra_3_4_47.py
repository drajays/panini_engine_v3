"""
3.4.47  उपदंशस्तृतीयायाम्  —  VIDHI

Padaccheda: उपदंशः तृतीयायाम्

krt-suffix rule: उपदंशस्तृतीयायाम्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_47_upadaMSast_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_47_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upadaMSastftIyAyAm",
    text_dev              = "उपदंशस्तृतीयायाम्",
    padaccheda_dev        = "उपदंशः तृतीयायाम्",
    why_dev               = "धातोः प्रत्ययः (३.4.47)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
