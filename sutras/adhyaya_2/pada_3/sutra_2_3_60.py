"""
2.3.60  द्वितीया ब्राह्मणे  —  VIDHI

Padaccheda: द्वितीया ब्राह्मणे

dvitiya in brahman context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_60_brahmane_dvitiya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_60_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvitIyA brAhmaRe",
    text_dev              = "द्वितीया ब्राह्मणे",
    padaccheda_dev        = "द्वितीया ब्राह्मणे",
    why_dev               = "ब्राह्मणे द्वितीया (२.३.६०)।",
    anuvritti_from        = ('2.3.2',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
