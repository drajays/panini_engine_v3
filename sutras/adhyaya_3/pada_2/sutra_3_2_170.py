"""
3.2.170  क्याच्छन्दसि  —  VIDHI

Padaccheda: क्यात् छन्दसि

krt-suffix rule: क्याच्छन्दसि (170)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_170_kyAcCandas_170"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_170_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.170"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.170",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kyAcCandasi",
    text_dev              = "क्याच्छन्दसि",
    padaccheda_dev        = "क्यात् छन्दसि",
    why_dev               = "धातोः कृत्-प्रत्ययः [क्याच्छन्दसि] विहितः (३.२.170)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
