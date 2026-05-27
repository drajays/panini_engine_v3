"""
2.2.22  क्त्वा च  —  VIDHI

Padaccheda: क्त्वा च

ktva-suffixed words also combine.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_22_ktva_ca"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.2.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ktvA ca",
    text_dev              = "क्त्वा च",
    padaccheda_dev        = "क्त्वा च",
    why_dev               = "क्त्वान्तं च समस्यते (२.२.२२)।",
    anuvritti_from        = ('2.2.21',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
