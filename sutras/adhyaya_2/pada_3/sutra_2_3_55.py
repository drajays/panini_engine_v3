"""
2.3.55  आशिषि नाथः  —  VIDHI

Padaccheda: आशिषि नाथः

natha in blessings takes sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_55_asisi_natha"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_55_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ASizi nATaH",
    text_dev              = "आशिषि नाथः",
    padaccheda_dev        = "आशिषि नाथः",
    why_dev               = "आशिषि नाथः (२.३.५५)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
