"""
8.2.13  उदन्वानुदधौ च  —  VIDHI

Padaccheda: उदन्वान् उदधौ च

उदन्वानुदधौ च (8.2.13)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_13_udanvAnuda_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_13_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udanvAnudaDO ca",
    text_dev              = "उदन्वानुदधौ च",
    padaccheda_dev        = "उदन्वान् उदधौ च",
    why_dev               = "(सूत्रम् 8.2.13) उदन्वानुदधौ च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
