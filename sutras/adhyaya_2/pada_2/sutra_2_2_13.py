"""
2.2.13  अधिकरणवाचिना च  —  VIDHI

Padaccheda: अधिकरण-वाचिना च

Adhikarana-denoting word with tatpurusha.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_13_adhikarana_vacina"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.2.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDikaraRavAcinA ca",
    text_dev              = "अधिकरणवाचिना च",
    padaccheda_dev        = "अधिकरण-वाचिना च",
    why_dev               = "अधिकरण-वाचिना सह तत्पुरुषः (२.२.१३)।",
    anuvritti_from        = ('2.2.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
