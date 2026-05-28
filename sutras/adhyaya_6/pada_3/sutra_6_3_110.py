"""
6.3.110  संख्याविसायपूर्वस्याह्नस्याहन्नन्यतरस्यां ङौ  —  VIDHI

Padaccheda: संख्या-वि-साय-पूर्वस्य अह्नस्य अहन् अन्यतरस्याम् ङौ

संख्याविसायपूर्वस्याह्नस्याहन्नन्यतरस्यां ङौ (6.3.110)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_110_saMKyAvisA_110"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.110"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyAvisAyapUrvasyAhnasyAhannanyatarasyAM NO",
    text_dev              = "संख्याविसायपूर्वस्याह्नस्याहन्नन्यतरस्यां ङौ",
    padaccheda_dev        = "संख्या-वि-साय-पूर्वस्य अह्नस्य अहन् अन्यतरस्याम् ङौ",
    why_dev               = "(सूत्रम् 6.3.110) संख्याविसायपूर्वस्याह्नस्याहन्नन्यतरस्यां ङौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
