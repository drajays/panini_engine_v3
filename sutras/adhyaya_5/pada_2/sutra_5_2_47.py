"""
5.2.47  संख्याया गुणस्य निमाने मयट्  —  VIDHI

Padaccheda: संख्यायाः गुणस्य निमाने मयट्

संख्याया गुणस्य निमाने मयट् (5.2.47)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_47_saMKyAyA_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_47_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyAyA guRasya nimAne mayaw",
    text_dev              = "संख्याया गुणस्य निमाने मयट्",
    padaccheda_dev        = "संख्यायाः गुणस्य निमाने मयट्",
    why_dev               = "(सूत्रम् 5.2.47) संख्याया गुणस्य निमाने मयट्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
