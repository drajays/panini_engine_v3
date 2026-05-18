"""
2.1.44  संज्ञायाम्  —  VIDHI

Padaccheda: संज्ञायाम्

In samjna context, saptami with kta forms tatpurusha compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_44_samjna_saptami"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_44_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAm",
    text_dev              = "संज्ञायाम्",
    padaccheda_dev        = "संज्ञायाम्",
    why_dev               = "संज्ञायां सप्तम्यन्तस्य क्तेन सह तत्पुरुषः (२.१.४४)।",
    anuvritti_from        = ('2.1.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
