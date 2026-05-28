"""
4.4.89  संज्ञायां धेनुष्या  —  VIDHI

Padaccheda: संज्ञायाम् धेनुष्या

संज्ञायां धेनुष्या (4.4.89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_89_saMjYAyAM_89"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.89", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAM DenuzyA",
    text_dev              = "संज्ञायां धेनुष्या",
    padaccheda_dev        = "संज्ञायाम् धेनुष्या",
    why_dev               = "(सूत्रम् 4.4.89) संज्ञायां धेनुष्या।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
