"""
3.4.56  विशिपतिपदिस्कन्दां व्याप्यमानासेव्यमानयोः  —  VIDHI

Padaccheda: विशि-पति-पदि-स्कन्दाम् व्याप्यमान-आसेव्यमानयोः

krt-suffix rule: विशिपतिपदिस्कन्दां व्याप्यमानासेव्यमानयोः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_56_viSipatipa_56"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("3_4_56_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viSipatipadiskandAM vyApyamAnAsevyamAnayoH",
    text_dev              = "विशिपतिपदिस्कन्दां व्याप्यमानासेव्यमानयोः",
    padaccheda_dev        = "विशि-पति-पदि-स्कन्दाम् व्याप्यमान-आसेव्यमानयोः",
    why_dev               = "धातोः प्रत्ययः (३.4.56)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
