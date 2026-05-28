"""
2.1.29  अत्यन्तसंयोगे च  —  VIDHI

Padaccheda: अत्यन्त-संयोगे च

atyanta-samyoga (excessive contact) with dvitiya forms avyayibhava.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_29_atyanta"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("avyayibhava" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]             = "2.1.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "atyantasaMyoge ca",
    text_dev              = "अत्यन्तसंयोगे च",
    padaccheda_dev        = "अत्यन्त-संयोगे च",
    why_dev               = "अत्यन्त-संयोगे द्वितीयान्तस्य सह अव्ययीभावः (२.१.२९)।",
    anuvritti_from        = ('2.1.5',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
