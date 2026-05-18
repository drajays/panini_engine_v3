"""
6.4.106  उतश्च प्रत्ययादसंयोगपूर्वात्  —  VIDHI

Padaccheda: उतः च प्रत्ययात् अ-संयोग-पूर्वात्

उतश्च प्रत्ययादसंयोगपूर्वात् (6.4.106)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_106_utaSca_106"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_106_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.106"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.106",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "utaSca pratyayAdasaMyogapUrvAt",
    text_dev              = "उतश्च प्रत्ययादसंयोगपूर्वात्",
    padaccheda_dev        = "उतः च प्रत्ययात् अ-संयोग-पूर्वात्",
    why_dev               = "(सूत्रम् 6.4.106) उतश्च प्रत्ययादसंयोगपूर्वात्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
