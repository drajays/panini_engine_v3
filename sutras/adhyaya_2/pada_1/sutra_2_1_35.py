"""
2.1.35  भक्ष्येण मिश्रीकरणम्  —  VIDHI

Padaccheda: भक्ष्येण मिश्री-करणम्

Food-mixing context (bhaksya + misrikarana) forms tatpurusha.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_35_bhaksya_misra"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_35_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BakzyeRa miSrIkaraRam",
    text_dev              = "भक्ष्येण मिश्रीकरणम्",
    padaccheda_dev        = "भक्ष्येण मिश्री-करणम्",
    why_dev               = "भक्ष्येण मिश्रीकरण-वाचिना सह तत्पुरुषः (२.१.३५)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
