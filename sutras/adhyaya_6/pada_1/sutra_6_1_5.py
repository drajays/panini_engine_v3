"""
6.1.5  उभे अभ्यस्तम्  —  VIDHI

Padaccheda: उभे अभ्यस्तम्

उभे अभ्यस्तम् (6.1.5)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_5_uBe_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_5_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uBe aByastam",
    text_dev              = "उभे अभ्यस्तम्",
    padaccheda_dev        = "उभे अभ्यस्तम्",
    why_dev               = "(सूत्रम् 6.1.5) उभे अभ्यस्तम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
