"""
8.1.35  छन्दस्यनेकमपि साकाङ्क्षम्  —  VIDHI

Padaccheda: छन्दसि अनेकम् अपि साकाङ्क्षम्

छन्दस्यनेकमपि साकाङ्क्षम् (8.1.35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_35_Candasyane_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_35_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Candasyanekamapi sAkANkzam",
    text_dev              = "छन्दस्यनेकमपि साकाङ्क्षम्",
    padaccheda_dev        = "छन्दसि अनेकम् अपि साकाङ्क्षम्",
    why_dev               = "(सूत्रम् 8.1.35) छन्दस्यनेकमपि साकाङ्क्षम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
