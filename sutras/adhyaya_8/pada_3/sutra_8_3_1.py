"""
8.3.1  मतुवसो रु सम्बुद्धौ छन्दसि  —  VIDHI

Padaccheda: मतु-वसोः रु (लुप्तप्रथमान्तनिर्देशः) सम्बुद्धौ छन्दसि

मतुवसो रु सम्बुद्धौ छन्दसि (8.3.1)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_1_matuvaso_1"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.1", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.1"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.1",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "matuvaso ru sambudDO Candasi",
    text_dev              = "मतुवसो रु सम्बुद्धौ छन्दसि",
    padaccheda_dev        = "मतु-वसोः रु (लुप्तप्रथमान्तनिर्देशः) सम्बुद्धौ छन्दसि",
    why_dev               = "(सूत्रम् 8.3.1) मतुवसो रु सम्बुद्धौ छन्दसि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
