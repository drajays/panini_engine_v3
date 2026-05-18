"""
3.4.49  सप्तम्यां चोपपीडरुधकर्षः  —  VIDHI

Padaccheda: सप्तम्याम् च उप-पीड-रुध-कर्षः (पञ्चम्यार्थे प्रथमा)

krt-suffix rule: सप्तम्यां चोपपीडरुधकर्षः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_49_saptamyAM_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_49_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saptamyAM copapIqaruDakarzaH",
    text_dev              = "सप्तम्यां चोपपीडरुधकर्षः",
    padaccheda_dev        = "सप्तम्याम् च उप-पीड-रुध-कर्षः (पञ्चम्यार्थे प्रथमा)",
    why_dev               = "धातोः प्रत्ययः (३.4.49)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
