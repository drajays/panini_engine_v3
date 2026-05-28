"""
8.3.49  छन्दसि वाऽप्राम्रेडितयोः  —  VIDHI

Padaccheda: छन्दसि वा अ-प्र-आम्रेडितयोः

छन्दसि वाऽप्राम्रेडितयोः (8.3.49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_49_Candasi_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Candasi vA'prAmreqitayoH",
    text_dev              = "छन्दसि वाऽप्राम्रेडितयोः",
    padaccheda_dev        = "छन्दसि वा अ-प्र-आम्रेडितयोः",
    why_dev               = "(सूत्रम् 8.3.49) छन्दसि वाऽप्राम्रेडितयोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
