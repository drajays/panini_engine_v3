"""
2.3.62  चतुर्थ्यर्थे बहुलं छन्दसि  —  VIDHI

Padaccheda: चतुर्थी-अर्थे बहुलम् छन्दसि

Bahulam (varied) use of caturthy-artha in chandas.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_62_caturthy_chandas"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_62_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "caturTyarTe bahulaM Candasi",
    text_dev              = "चतुर्थ्यर्थे बहुलं छन्दसि",
    padaccheda_dev        = "चतुर्थी-अर्थे बहुलम् छन्दसि",
    why_dev               = "चतुर्थी-अर्थे बहुलम् छन्दसि (२.३.६२)।",
    anuvritti_from        = ('2.3.13',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
