"""
8.3.69  वेश्च स्वनो भोजने  —  VIDHI

Padaccheda: वेः च स्वनः भोजने

वेश्च स्वनो भोजने (8.3.69)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_69_veSca_69"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_69_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "veSca svano Bojane",
    text_dev              = "वेश्च स्वनो भोजने",
    padaccheda_dev        = "वेः च स्वनः भोजने",
    why_dev               = "(सूत्रम् 8.3.69) वेश्च स्वनो भोजने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
