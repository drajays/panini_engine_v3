"""
6.4.58  युप्लुवोर्दीर्घश्छन्दसि  —  VIDHI

Padaccheda: यु-प्लुवोः दीर्घः छन्दसि

युप्लुवोर्दीर्घश्छन्दसि (6.4.58)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_58_yupluvordI_58"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_58_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yupluvordIrGaSCandasi",
    text_dev              = "युप्लुवोर्दीर्घश्छन्दसि",
    padaccheda_dev        = "यु-प्लुवोः दीर्घः छन्दसि",
    why_dev               = "(सूत्रम् 6.4.58) युप्लुवोर्दीर्घश्छन्दसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
