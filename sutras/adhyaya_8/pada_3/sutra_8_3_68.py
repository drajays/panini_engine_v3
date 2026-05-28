"""
8.3.68  अवाच्चालम्बनाविदूर्ययोः  —  VIDHI

Padaccheda: अवात् च आलम्बन-आविदूर्ययोः

अवाच्चालम्बनाविदूर्ययोः (8.3.68)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_68_avAccAlamb_68"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_68_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avAccAlambanAvidUryayoH",
    text_dev              = "अवाच्चालम्बनाविदूर्ययोः",
    padaccheda_dev        = "अवात् च आलम्बन-आविदूर्ययोः",
    why_dev               = "(सूत्रम् 8.3.68) अवाच्चालम्बनाविदूर्ययोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
