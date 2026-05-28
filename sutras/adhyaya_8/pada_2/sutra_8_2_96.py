"""
8.2.96  अङ्गयुक्तं तिङ् आकाङ्क्षम्  —  VIDHI

Padaccheda: अङ्गयुक्तम् तिङ् आकाङ्क्षम्

अङ्गयुक्तं तिङ् आकाङ्क्षम् (8.2.96)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_96_aNgayuktaM_96"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_96_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aNgayuktaM tiN AkANkzam",
    text_dev              = "अङ्गयुक्तं तिङ् आकाङ्क्षम्",
    padaccheda_dev        = "अङ्गयुक्तम् तिङ् आकाङ्क्षम्",
    why_dev               = "(सूत्रम् 8.2.96) अङ्गयुक्तं तिङ् आकाङ्क्षम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
