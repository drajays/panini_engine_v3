"""
3.3.68  प्रमदसम्मदौ हर्षे  —  VIDHI

Padaccheda: प्रमदसम्मदौ हर्षे

krt-suffix rule: प्रमदसम्मदौ हर्षे
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_68_pramadasam_68"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_68_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pramadasammadO harze",
    text_dev              = "प्रमदसम्मदौ हर्षे",
    padaccheda_dev        = "प्रमदसम्मदौ हर्षे",
    why_dev               = "धातोः प्रत्ययः (३.3.68)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
