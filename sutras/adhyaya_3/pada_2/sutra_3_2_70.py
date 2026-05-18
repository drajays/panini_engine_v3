"""
3.2.70  दुहः कब् घश्च  —  VIDHI

Padaccheda: दुहः कप् घः च

krt-suffix rule: दुहः कब् घश्च (70)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_70_duhaH_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_70_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "duhaH kab GaSca",
    text_dev              = "दुहः कब् घश्च",
    padaccheda_dev        = "दुहः कप् घः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [दुहः कब् घश्च] विहितः (३.२.70)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
