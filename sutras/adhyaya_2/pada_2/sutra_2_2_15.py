"""
2.2.15  तृजकाभ्यां कर्तरि  —  VIDHI

Padaccheda: तृच्-अकाभ्याम् कर्तरि

trc and aka with kartri form tatpurusha.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_15_trj_aka_kartari"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_2_15_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.2.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tfjakAByAM kartari",
    text_dev              = "तृजकाभ्यां कर्तरि",
    padaccheda_dev        = "तृच्-अकाभ्याम् कर्तरि",
    why_dev               = "तृच्-अकाभ्यां कर्तरि तत्पुरुषः (२.२.१५)।",
    anuvritti_from        = ('2.2.13',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
