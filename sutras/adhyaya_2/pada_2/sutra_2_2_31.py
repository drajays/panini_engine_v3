"""
2.2.31  राजदन्तादिषु परम्  —  VIDHI

Padaccheda: राजदन्त-आदिषु परम्

In rajadanta etc. the latter member prevails.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_31_rajadanta_param"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_2_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.2.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAjadantAdizu param",
    text_dev              = "राजदन्तादिषु परम्",
    padaccheda_dev        = "राजदन्त-आदिषु परम्",
    why_dev               = "राजदन्त-आदिषु पूर्वपदं परम् (२.२.३१)।",
    anuvritti_from        = ('2.2.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
