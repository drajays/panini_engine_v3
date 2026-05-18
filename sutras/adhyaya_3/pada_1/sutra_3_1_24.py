"""
3.1.24  लुपसदचरजपजभदहदशगॄभ्यो भावगर्हायाम्  —  VIDHI

Padaccheda: लुप-सद-चर-जप-जभ-दह-दश-गॄभ्यः भावगर्हायाम्

Krt suffix rule from dhatu: लुपसदचरजपजभदहदशगॄभ्यो भावगर्हायाम् (24)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_24_lupasadacara_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_24_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lupasadacarajapajaBadahadaSagFByo BAvagarhAyAm",
    text_dev              = "लुपसदचरजपजभदहदशगॄभ्यो भावगर्हायाम्",
    padaccheda_dev        = "लुप-सद-चर-जप-जभ-दह-दश-गॄभ्यः भावगर्हायाम्",
    why_dev               = "धातोः [लुपसदचरजपजभदहदशगॄभ्यो भावगर्हायाम्]-प्रत्ययः विहितः (३.१.24)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
