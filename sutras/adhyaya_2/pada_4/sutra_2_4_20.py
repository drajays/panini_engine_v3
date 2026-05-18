"""
2.4.20  संज्ञायां कन्थोशीनरेषु  —  VIDHI

Padaccheda: संज्ञायाम् कन्था उशीनरेषु

In samjna kantha etc. in Usinara territory.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_20_samjna_kantha"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_20_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAM kanToSInarezu",
    text_dev              = "संज्ञायां कन्थोशीनरेषु",
    padaccheda_dev        = "संज्ञायाम् कन्था उशीनरेषु",
    why_dev               = "संज्ञायाम् कन्था उशीनरेषु (२.४.२०)।",
    anuvritti_from        = ('2.4.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
