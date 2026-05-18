"""
4.2.104  अव्ययात्त्यप्  —  VIDHI

Padaccheda: अव्ययात् त्यप्

अव्ययात्त्यप् (4.2.104)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_104_avyayAttya_104"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_104_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avyayAttyap",
    text_dev              = "अव्ययात्त्यप्",
    padaccheda_dev        = "अव्ययात् त्यप्",
    why_dev               = "(सूत्रम् 4.2.104) अव्ययात्त्यप्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
