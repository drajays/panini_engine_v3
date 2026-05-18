"""
3.2.52  लक्षणे जायापत्योष्टक्  —  VIDHI

Padaccheda: लक्षणे जाया-पत्योः टक्

krt-suffix rule: लक्षणे जायापत्योष्टक् (52)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_52_lakzaRe_52"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_52_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lakzaRe jAyApatyozwak",
    text_dev              = "लक्षणे जायापत्योष्टक्",
    padaccheda_dev        = "लक्षणे जाया-पत्योः टक्",
    why_dev               = "धातोः कृत्-प्रत्ययः [लक्षणे जायापत्योष्टक्] विहितः (३.२.52)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
