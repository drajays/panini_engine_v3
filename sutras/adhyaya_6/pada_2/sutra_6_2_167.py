"""
6.2.167  मुखं स्वाङ्गम्  —  VIDHI

Padaccheda: मुखम् स्वाङ्गम्

मुखं स्वाङ्गम् (6.2.167)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_167_muKaM_167"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_167_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.167"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.167",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "muKaM svANgam",
    text_dev              = "मुखं स्वाङ्गम्",
    padaccheda_dev        = "मुखम् स्वाङ्गम्",
    why_dev               = "(सूत्रम् 6.2.167) मुखं स्वाङ्गम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
