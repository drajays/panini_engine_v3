"""
8.3.82  अग्नेः स्तुत्स्तोमसोमाः  —  VIDHI

Padaccheda: अग्नेः स्तुत्-स्तोम-सोमाः

अग्नेः स्तुत्स्तोमसोमाः (8.3.82)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_82_agneH_82"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_82_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.82"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.82",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "agneH stutstomasomAH",
    text_dev              = "अग्नेः स्तुत्स्तोमसोमाः",
    padaccheda_dev        = "अग्नेः स्तुत्-स्तोम-सोमाः",
    why_dev               = "(सूत्रम् 8.3.82) अग्नेः स्तुत्स्तोमसोमाः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
