"""
8.2.99  प्रतिश्रवणे च  —  VIDHI

Padaccheda: प्रतिश्रवणे च

प्रतिश्रवणे च (8.2.99)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_99_pratiSrava_99"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_99_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratiSravaRe ca",
    text_dev              = "प्रतिश्रवणे च",
    padaccheda_dev        = "प्रतिश्रवणे च",
    why_dev               = "(सूत्रम् 8.2.99) प्रतिश्रवणे च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
