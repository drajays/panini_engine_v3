"""
2.4.78  विभाषा घ्राधेट्शाच्छासः  —  VIDHI

Padaccheda: विभाषा घ्रा-धेट्-शा-छा-सः

Optional luk for ghra, dhet, sha, cha, sa.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_78_ghra_dhet_sha"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_78_sic_lopa_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.78"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.78",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA GrADewSAcCAsaH",
    text_dev              = "विभाषा घ्राधेट्शाच्छासः",
    padaccheda_dev        = "विभाषा घ्रा-धेट्-शा-छा-सः",
    why_dev               = "घ्रा-धेट्-शा-छा-सः विभाषा (२.४.७८)।",
    anuvritti_from        = ('2.4.77',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
