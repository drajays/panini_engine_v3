"""
2.4.59  पैलादिभ्यश्च  —  VIDHI

Padaccheda: पैल-आदिभ्यः च

Also for paila etc.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_59_paila_adi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_59_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pElAdiByaSca",
    text_dev              = "पैलादिभ्यश्च",
    padaccheda_dev        = "पैल-आदिभ्यः च",
    why_dev               = "पैल-आदिभ्यः च (२.४.५९)।",
    anuvritti_from        = ('2.4.58',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
