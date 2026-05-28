"""
8.3.61  स्तौतिण्योरेव षण्यभ्यासात्  —  VIDHI

Padaccheda: स्तौति-ण्योः एव षणि अभ्यासात्

स्तौतिण्योरेव षण्यभ्यासात् (8.3.61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_61_stOtiRyore_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_61_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "stOtiRyoreva zaRyaByAsAt",
    text_dev              = "स्तौतिण्योरेव षण्यभ्यासात्",
    padaccheda_dev        = "स्तौति-ण्योः एव षणि अभ्यासात्",
    why_dev               = "(सूत्रम् 8.3.61) स्तौतिण्योरेव षण्यभ्यासात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
