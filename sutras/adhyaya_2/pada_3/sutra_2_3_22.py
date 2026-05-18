"""
2.3.22  संज्ञोऽन्यतरस्यां कर्मणि  —  VIDHI

Padaccheda: संज्ञः अन्यतरस्याम् कर्मणि

samjna optionally takes karma vibhakti (tritiya/dvitiya).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_22_samjna_karmani"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_22_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYo'nyatarasyAM karmaRi",
    text_dev              = "संज्ञोऽन्यतरस्यां कर्मणि",
    padaccheda_dev        = "संज्ञः अन्यतरस्याम् कर्मणि",
    why_dev               = "संज्ञः अन्यतरस्याम् कर्मणि (२.३.२२)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
