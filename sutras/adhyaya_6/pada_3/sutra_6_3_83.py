"""
6.3.83  प्रकृत्याऽऽशिष्यगोवत्सहलेषु  —  VIDHI

Padaccheda: प्रकृत्या आशिषि अ-गो-वत्स-हलेषु

प्रकृत्याऽऽशिष्यगोवत्सहलेषु (6.3.83)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_83_prakftyA_83"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_83_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prakftyA''Sizyagovatsahalezu",
    text_dev              = "प्रकृत्याऽऽशिष्यगोवत्सहलेषु",
    padaccheda_dev        = "प्रकृत्या आशिषि अ-गो-वत्स-हलेषु",
    why_dev               = "(सूत्रम् 6.3.83) प्रकृत्याऽऽशिष्यगोवत्सहलेषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
