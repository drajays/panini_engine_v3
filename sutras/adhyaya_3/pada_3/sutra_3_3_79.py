"""
3.3.79  अगारैकदेशे प्रघणः प्रघाणश्च  —  VIDHI

Padaccheda: अगार्-एकदेशे प्रघणः प्रघाणः च

krt-suffix rule: अगारैकदेशे प्रघणः प्रघाणश्च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_79_agArEkadeS_79"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_79_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.79"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.79",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "agArEkadeSe praGaRaH praGARaSca",
    text_dev              = "अगारैकदेशे प्रघणः प्रघाणश्च",
    padaccheda_dev        = "अगार्-एकदेशे प्रघणः प्रघाणः च",
    why_dev               = "धातोः प्रत्ययः (३.3.79)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
