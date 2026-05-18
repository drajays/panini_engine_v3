"""
3.4.4  यथाविध्यनुप्रयोगः पूर्वस्मिन्  —  VIDHI

Padaccheda: यथाविधि अनुप्रयोगः पूर्वस्मिन्

krt-suffix rule: यथाविध्यनुप्रयोगः पूर्वस्मिन्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_4_yaTAviDyan_4"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_4_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaTAviDyanuprayogaH pUrvasmin",
    text_dev              = "यथाविध्यनुप्रयोगः पूर्वस्मिन्",
    padaccheda_dev        = "यथाविधि अनुप्रयोगः पूर्वस्मिन्",
    why_dev               = "धातोः प्रत्ययः (३.4.4)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
