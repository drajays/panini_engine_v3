"""
7.3.25  जङ्गलधेनुवलजान्तस्य विभाषितमुत्तरम्  —  VIDHI

Padaccheda: जङ्गल-धेनु-वलज-अन्तस्य विभाषितम् उत्तरम्

जङ्गलधेनुवलजान्तस्य विभाषितमुत्तरम् (7.3.25)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_25_jaNgalaDen_25"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_25_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jaNgalaDenuvalajAntasya viBAzitamuttaram",
    text_dev              = "जङ्गलधेनुवलजान्तस्य विभाषितमुत्तरम्",
    padaccheda_dev        = "जङ्गल-धेनु-वलज-अन्तस्य विभाषितम् उत्तरम्",
    why_dev               = "(सूत्रम् 7.3.25) जङ्गलधेनुवलजान्तस्य विभाषितमुत्तरम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
