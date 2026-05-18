"""
7.4.39  कव्यध्वरपृतनस्यर्चि लोपः  —  VIDHI

Padaccheda: कवि-अध्वर-पृतनस्य ऋचि लोपः

कव्यध्वरपृतनस्यर्चि लोपः (7.4.39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_39_kavyaDvara_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_39_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kavyaDvarapftanasyarci lopaH",
    text_dev              = "कव्यध्वरपृतनस्यर्चि लोपः",
    padaccheda_dev        = "कवि-अध्वर-पृतनस्य ऋचि लोपः",
    why_dev               = "(सूत्रम् 7.4.39) कव्यध्वरपृतनस्यर्चि लोपः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
