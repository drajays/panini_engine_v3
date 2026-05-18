"""
4.1.102  शरद्वच्छुनकदर्भाद्भृगुवत्साग्रायणेषु  —  VIDHI

Padaccheda: शरद्वत्-शुनक-दर्भात् भृगु-वत्स-आग्रायणेषु

शरद्वच्छुनकदर्भाद्भृगुवत्साग्रायणेषु (4.1.102)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_102_SaradvacCu_102"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_102_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.102"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.102",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SaradvacCunakadarBAdBfguvatsAgrAyaRezu",
    text_dev              = "शरद्वच्छुनकदर्भाद्भृगुवत्साग्रायणेषु",
    padaccheda_dev        = "शरद्वत्-शुनक-दर्भात् भृगु-वत्स-आग्रायणेषु",
    why_dev               = "(सूत्रम् 4.1.102) शरद्वच्छुनकदर्भाद्भृगुवत्साग्रायणेषु।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
