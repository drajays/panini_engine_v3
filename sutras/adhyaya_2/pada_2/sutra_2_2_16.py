"""
2.2.16  कर्त्तरि च  —  VIDHI

Padaccheda: कर्तरि च

Also in kartri context tatpurusha is formed.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_16_kartari_ca"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.2.16"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karttari ca",
    text_dev              = "कर्त्तरि च",
    padaccheda_dev        = "कर्तरि च",
    why_dev               = "कर्तरि च तत्पुरुषः (२.२.१६)।",
    anuvritti_from        = ('2.2.15',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
