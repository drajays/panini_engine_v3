"""
2.3.68  अधिकरणवाचिनश्च  —  VIDHI

Padaccheda: अधिकरण-वाचिनः च

adhikarana-denoting words also take sasthi with krt.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_68_adhikarana_vacina"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_68_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDikaraRavAcinaSca",
    text_dev              = "अधिकरणवाचिनश्च",
    padaccheda_dev        = "अधिकरण-वाचिनः च",
    why_dev               = "अधिकरण-वाचिनः च (२.३.६८)।",
    anuvritti_from        = ('2.3.65',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
