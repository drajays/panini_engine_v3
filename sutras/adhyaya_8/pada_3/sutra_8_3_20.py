"""
8.3.20  ओतो गार्ग्यस्य  —  VIDHI

Padaccheda: ओतः · गार्ग्यस्य

ओतो गार्ग्यस्य (8.3.20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_20_oto_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_20_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "oto gArgyasya",
    text_dev              = "ओतो गार्ग्यस्य",
    padaccheda_dev        = "ओतः · गार्ग्यस्य",
    why_dev               = "(सूत्रम् 8.3.20) ओतो गार्ग्यस्य।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
