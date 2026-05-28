"""
3.3.111  पर्यायार्हर्णोत्पत्तिषु ण्वुच्  —  VIDHI

Padaccheda: पर्याय-अर्हण-उत्पत्तिषु ण्वुच्

krt-suffix rule: पर्यायार्हर्णोत्पत्तिषु ण्वुच्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_111_paryAyArha_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_111_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paryAyArharRotpattizu Rvuc",
    text_dev              = "पर्यायार्हर्णोत्पत्तिषु ण्वुच्",
    padaccheda_dev        = "पर्याय-अर्हण-उत्पत्तिषु ण्वुच्",
    why_dev               = "धातोः प्रत्ययः (३.3.111)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
