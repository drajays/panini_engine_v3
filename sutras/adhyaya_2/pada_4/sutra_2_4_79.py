"""
2.4.79  तनादिभ्यस्तथासोः  —  VIDHI

Padaccheda: तनादिभ्यः त-थासोः

luk of sic for tanadi roots in ta and thasa.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_79_tanadi_ta_thasa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_79_sic_lopa_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.79"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.79",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tanAdiByastaTAsoH",
    text_dev              = "तनादिभ्यस्तथासोः",
    padaccheda_dev        = "तनादिभ्यः त-थासोः",
    why_dev               = "तनादिभ्यः त-थासोः (२.४.७९)।",
    anuvritti_from        = ('2.4.77',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
