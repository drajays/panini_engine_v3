"""
3.3.90  यजयाचयतविच्छप्रच्छरक्षो नङ्  —  VIDHI

Padaccheda: यज-याच-यत-विच्छ-प्रच्छ-रक्षः नङ्

krt-suffix rule: यजयाचयतविच्छप्रच्छरक्षो नङ्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_90_yajayAcaya_90"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_90_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yajayAcayatavicCapracCarakzo naN",
    text_dev              = "यजयाचयतविच्छप्रच्छरक्षो नङ्",
    padaccheda_dev        = "यज-याच-यत-विच्छ-प्रच्छ-रक्षः नङ्",
    why_dev               = "धातोः प्रत्ययः (३.3.90)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
