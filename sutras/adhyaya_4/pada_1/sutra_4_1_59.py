"""
4.1.59  दीर्घजिह्वी च च्छन्दसि  —  VIDHI

Padaccheda: दीर्घजिह्वी च छन्दसि

दीर्घजिह्वी च च्छन्दसि (4.1.59)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_59_dIrGajihvI_59"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_59_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dIrGajihvI ca cCandasi",
    text_dev              = "दीर्घजिह्वी च च्छन्दसि",
    padaccheda_dev        = "दीर्घजिह्वी च छन्दसि",
    why_dev               = "(सूत्रम् 4.1.59) दीर्घजिह्वी च च्छन्दसि।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
