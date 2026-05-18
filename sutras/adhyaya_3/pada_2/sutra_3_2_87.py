"""
3.2.87  ब्रह्मभ्रूणवृत्रेषु क्विप्  —  VIDHI

Padaccheda: ब्रह्म-भ्रूण-वृत्रेषु क्विँप्

krt-suffix rule: ब्रह्मभ्रूणवृत्रेषु क्विप् (87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_87_brahmaBrUR_87"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_87_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "brahmaBrURavftrezu kvip",
    text_dev              = "ब्रह्मभ्रूणवृत्रेषु क्विप्",
    padaccheda_dev        = "ब्रह्म-भ्रूण-वृत्रेषु क्विँप्",
    why_dev               = "धातोः कृत्-प्रत्ययः [ब्रह्मभ्रूणवृत्रेषु क्विप्] विहितः (३.२.87)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
