"""
8.3.63  प्राक्सितादड्व्यवायेऽपि  —  VIDHI

Padaccheda: प्राक् सितात् अट्-व्यवाये अपि

प्राक्सितादड्व्यवायेऽपि (8.3.63)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_63_prAksitAda_63"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_63_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prAksitAdaqvyavAye'pi",
    text_dev              = "प्राक्सितादड्व्यवायेऽपि",
    padaccheda_dev        = "प्राक् सितात् अट्-व्यवाये अपि",
    why_dev               = "(सूत्रम् 8.3.63) प्राक्सितादड्व्यवायेऽपि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
