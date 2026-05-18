"""
4.1.54  स्वाङ्गाच्चोपसर्जनादसंयोगोपधात्  —  VIDHI

Padaccheda: स्वाङ्गात् च उपसर्जनात् अ-संयोग-उपधात्

स्वाङ्गाच्चोपसर्जनादसंयोगोपधात् (4.1.54)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_54_svANgAccop_54"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_54_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svANgAccopasarjanAdasaMyogopaDAt",
    text_dev              = "स्वाङ्गाच्चोपसर्जनादसंयोगोपधात्",
    padaccheda_dev        = "स्वाङ्गात् च उपसर्जनात् अ-संयोग-उपधात्",
    why_dev               = "(सूत्रम् 4.1.54) स्वाङ्गाच्चोपसर्जनादसंयोगोपधात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
