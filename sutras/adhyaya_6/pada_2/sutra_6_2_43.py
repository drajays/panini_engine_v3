"""
6.2.43  चतुर्थी तदर्थे  —  VIDHI

Padaccheda: चतुर्थी तदर्थे

चतुर्थी तदर्थे (6.2.43)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_43_caturTI_43"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "caturTI tadarTe",
    text_dev              = "चतुर्थी तदर्थे",
    padaccheda_dev        = "चतुर्थी तदर्थे",
    why_dev               = "(सूत्रम् 6.2.43) चतुर्थी तदर्थे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
