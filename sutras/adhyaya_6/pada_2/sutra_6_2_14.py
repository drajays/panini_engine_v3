"""
6.2.14  मात्रोपज्ञोपक्रमच्छाये नपुंसके  —  VIDHI

Padaccheda: मात्रा-उपज्ञा- उपक्रम-छाये नपुंसके

मात्रोपज्ञोपक्रमच्छाये नपुंसके (6.2.14)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_14_mAtropajYo_14"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mAtropajYopakramacCAye napuMsake",
    text_dev              = "मात्रोपज्ञोपक्रमच्छाये नपुंसके",
    padaccheda_dev        = "मात्रा-उपज्ञा- उपक्रम-छाये नपुंसके",
    why_dev               = "(सूत्रम् 6.2.14) मात्रोपज्ञोपक्रमच्छाये नपुंसके।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
