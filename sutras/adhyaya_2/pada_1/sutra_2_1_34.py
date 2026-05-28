"""
2.1.34  अन्नेन व्यञ्जनम्  —  VIDHI

Padaccheda: अन्नेन व्यञ्जनम्

Condiment (vyanjana) with anna forms tatpurusha compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_34_anna_vyanjana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "annena vyaYjanam",
    text_dev              = "अन्नेन व्यञ्जनम्",
    padaccheda_dev        = "अन्नेन व्यञ्जनम्",
    why_dev               = "अन्नेन व्यञ्जनवाचिना सह तत्पुरुषः (२.१.३४)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
