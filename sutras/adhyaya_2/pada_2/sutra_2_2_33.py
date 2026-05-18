"""
2.2.33  अजाद्यदन्तम्  —  VIDHI

Padaccheda: अजादि-अदन्तम्

Ajadi and adanta also in dvandva context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_33_ajadi_adanta"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_2_33_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvandva_kind"]             = "2.2.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ajAdyadantam",
    text_dev              = "अजाद्यदन्तम्",
    padaccheda_dev        = "अजादि-अदन्तम्",
    why_dev               = "अजादि-अदन्तं च (२.२.३३)।",
    anuvritti_from        = ('2.2.32',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
