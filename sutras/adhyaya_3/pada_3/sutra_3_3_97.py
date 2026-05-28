"""
3.3.97  ऊतियूतिजूतिसातिहेतिकीर्तयश्च  —  VIDHI

Padaccheda: ऊति-यूति-जूति-साति-हेति-कीर्त्तयः च

krt-suffix rule: ऊतियूतिजूतिसातिहेतिकीर्तयश्च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_97_UtiyUtijUt_97"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_97_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.97"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UtiyUtijUtisAtihetikIrtayaSca",
    text_dev              = "ऊतियूतिजूतिसातिहेतिकीर्तयश्च",
    padaccheda_dev        = "ऊति-यूति-जूति-साति-हेति-कीर्त्तयः च",
    why_dev               = "धातोः प्रत्ययः (३.3.97)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
