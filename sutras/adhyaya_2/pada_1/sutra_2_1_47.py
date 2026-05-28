"""
2.1.47  क्षेपे  —  VIDHI

Padaccheda: क्षेपे

ksepa-context saptami forms tatpurusha compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_47_ksepe_saptami"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzepe",
    text_dev              = "क्षेपे",
    padaccheda_dev        = "क्षेपे",
    why_dev               = "क्षेपे वर्तमानस्य सप्तम्यन्तस्य सह तत्पुरुषः (२.१.४७)।",
    anuvritti_from        = ('2.1.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
