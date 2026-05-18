"""
3.2.108  भाषायां सदवसश्रुवः  —  VIDHI

Padaccheda: भाषायाम् सद-वस-श्रुवः

krt-suffix rule: भाषायां सदवसश्रुवः (108)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_108_BAzAyAM_108"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_108_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.108"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BAzAyAM sadavasaSruvaH",
    text_dev              = "भाषायां सदवसश्रुवः",
    padaccheda_dev        = "भाषायाम् सद-वस-श्रुवः",
    why_dev               = "धातोः कृत्-प्रत्ययः [भाषायां सदवसश्रुवः] विहितः (३.२.108)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
