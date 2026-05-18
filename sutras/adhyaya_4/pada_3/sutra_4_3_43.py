"""
4.3.43  कालात् साधुपुष्प्यत्पच्यमानेषु  —  VIDHI

Padaccheda: कालात् साधुपुष्प्यत्-पच्यमानेषु

कालात् साधुपुष्प्यत्पच्यमानेषु (4.3.43)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_43_kAlAt_43"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_43_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAlAt sADupuzpyatpacyamAnezu",
    text_dev              = "कालात् साधुपुष्प्यत्पच्यमानेषु",
    padaccheda_dev        = "कालात् साधुपुष्प्यत्-पच्यमानेषु",
    why_dev               = "(सूत्रम् 4.3.43) कालात् साधुपुष्प्यत्पच्यमानेषु।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
