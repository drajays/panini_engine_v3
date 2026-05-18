"""
5.4.41  वृकज्येष्ठाभ्यां तिल्तातिलौ च च्छन्दसि  —  VIDHI

Padaccheda: वृक-ज्येष्ठाभ्याम् तिल्-तातिलौ च छन्दसि

वृकज्येष्ठाभ्यां तिल्तातिलौ च च्छन्दसि (5.4.41)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_41_vfkajyezWA_41"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_41_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.41"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vfkajyezWAByAM tiltAtilO ca cCandasi",
    text_dev              = "वृकज्येष्ठाभ्यां तिल्तातिलौ च च्छन्दसि",
    padaccheda_dev        = "वृक-ज्येष्ठाभ्याम् तिल्-तातिलौ च छन्दसि",
    why_dev               = "(सूत्रम् 5.4.41) वृकज्येष्ठाभ्यां तिल्तातिलौ च च्छन्दसि।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
