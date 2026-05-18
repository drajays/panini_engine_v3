"""
5.3.20  तयोर्दार्हिलौ च च्छन्दसि  —  VIDHI

Padaccheda: तयोः दा-र्हिलौ च च्छन्दसि

तयोर्दार्हिलौ च च्छन्दसि (5.3.20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_20_tayordArhi_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_20_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tayordArhilO ca cCandasi",
    text_dev              = "तयोर्दार्हिलौ च च्छन्दसि",
    padaccheda_dev        = "तयोः दा-र्हिलौ च च्छन्दसि",
    why_dev               = "(सूत्रम् 5.3.20) तयोर्दार्हिलौ च च्छन्दसि।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
