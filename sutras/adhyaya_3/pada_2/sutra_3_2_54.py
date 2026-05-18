"""
3.2.54  शक्तौ हस्तिकपाटयोः  —  VIDHI

Padaccheda: शक्तौ हस्ति-कपाटयोः

krt-suffix rule: शक्तौ हस्तिकपाटयोः (54)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_54_SaktO_54"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_54_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SaktO hastikapAwayoH",
    text_dev              = "शक्तौ हस्तिकपाटयोः",
    padaccheda_dev        = "शक्तौ हस्ति-कपाटयोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [शक्तौ हस्तिकपाटयोः] विहितः (३.२.54)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
