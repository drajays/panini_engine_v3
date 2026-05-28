"""
3.3.122  अध्यायन्यायोद्यावसंहाराधारावयाश्च  —  VIDHI

Padaccheda: अध्याय-न्याय-उद्याव-संहाराः च

krt-suffix rule: अध्यायन्यायोद्यावसंहाराधारावयाश्च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_122_aDyAyanyAy_122"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.122"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.122",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDyAyanyAyodyAvasaMhArADArAvayASca",
    text_dev              = "अध्यायन्यायोद्यावसंहाराधारावयाश्च",
    padaccheda_dev        = "अध्याय-न्याय-उद्याव-संहाराः च",
    why_dev               = "धातोः प्रत्ययः (३.3.122)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
