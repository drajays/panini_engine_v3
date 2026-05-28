"""
8.3.58  नुम्विसर्जनीयशर्व्यवायेऽपि  —  VIDHI

Padaccheda: नुम्-विसर्जनीय-शर्-व्यवाये अपि

नुम्विसर्जनीयशर्व्यवायेऽपि (8.3.58)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_58_numvisarja_58"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "numvisarjanIyaSarvyavAye'pi",
    text_dev              = "नुम्विसर्जनीयशर्व्यवायेऽपि",
    padaccheda_dev        = "नुम्-विसर्जनीय-शर्-व्यवाये अपि",
    why_dev               = "(सूत्रम् 8.3.58) नुम्विसर्जनीयशर्व्यवायेऽपि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
