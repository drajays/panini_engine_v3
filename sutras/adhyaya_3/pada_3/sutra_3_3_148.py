"""
3.3.148  यच्चयत्रयोः  —  VIDHI

Padaccheda: यच्च-यत्रयोः

krt-suffix rule: यच्चयत्रयोः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_148_yaccayatra_148"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_148_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.148"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.148",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaccayatrayoH",
    text_dev              = "यच्चयत्रयोः",
    padaccheda_dev        = "यच्च-यत्रयोः",
    why_dev               = "धातोः प्रत्ययः (३.3.148)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
