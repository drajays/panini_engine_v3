"""
6.1.148  वर्चस्केऽवस्करः  —  VIDHI

Padaccheda: वर्चस्के अवस्करः

वर्चस्केऽवस्करः (6.1.148)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_148_varcaskev_148"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_148_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.148"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.148",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "varcaske'vaskaraH",
    text_dev              = "वर्चस्केऽवस्करः",
    padaccheda_dev        = "वर्चस्के अवस्करः",
    why_dev               = "(सूत्रम् 6.1.148) वर्चस्केऽवस्करः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
