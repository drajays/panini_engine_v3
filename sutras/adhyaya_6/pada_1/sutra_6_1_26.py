"""
6.1.26  विभाषाऽभ्यवपूर्वस्य  —  VIDHI

Padaccheda: विभाषा अभि-अव-पूर्वस्य

विभाषाऽभ्यवपूर्वस्य (6.1.26)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_26_viBAzABya_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_26_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA'ByavapUrvasya",
    text_dev              = "विभाषाऽभ्यवपूर्वस्य",
    padaccheda_dev        = "विभाषा अभि-अव-पूर्वस्य",
    why_dev               = "(सूत्रम् 6.1.26) विभाषाऽभ्यवपूर्वस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
