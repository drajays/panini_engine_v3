"""
2.4.39  बहुलं छन्दसि  —  VIDHI

Padaccheda: बहुलम् छन्दसि

Bahulam (varied) replacement in chandas.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_39_bahulam_chandas_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.39", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahulaM Candasi",
    text_dev              = "बहुलं छन्दसि",
    padaccheda_dev        = "बहुलम् छन्दसि",
    why_dev               = "बहुलम् छन्दसि (२.४.३९)।",
    anuvritti_from        = ('2.4.35',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
