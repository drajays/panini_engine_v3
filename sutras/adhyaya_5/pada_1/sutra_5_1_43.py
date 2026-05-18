"""
5.1.43  तत्र विदित इति च  —  VIDHI

Padaccheda: तत्र विदितः इति च

तत्र विदित इति च (5.1.43)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_43_tatra_43"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_43_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tatra vidita iti ca",
    text_dev              = "तत्र विदित इति च",
    padaccheda_dev        = "तत्र विदितः इति च",
    why_dev               = "(सूत्रम् 5.1.43) तत्र विदित इति च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
