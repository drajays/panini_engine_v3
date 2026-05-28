"""
2.1.57  विशेषणं विशेष्येण बहुलम्  —  VIDHI

Padaccheda: विशेषणम् विशेष्येण बहुलम्

Adjective with adjective (visesana+visesya) bahula karmadharaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_57_visesana_bahulam"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viSezaRaM viSezyeRa bahulam",
    text_dev              = "विशेषणं विशेष्येण बहुलम्",
    padaccheda_dev        = "विशेषणम् विशेष्येण बहुलम्",
    why_dev               = "विशेषणं विशेष्येण बहुलं कर्मधारयः (२.१.५७)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
