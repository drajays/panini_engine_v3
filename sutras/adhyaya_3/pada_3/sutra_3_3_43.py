"""
3.3.43  कर्मव्यतिहारे णच् स्त्रियाम्  —  VIDHI

Padaccheda: कर्म-व्यतिहारे णच् स्त्रियाम्

krt-suffix rule: कर्मव्यतिहारे णच् स्त्रियाम्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_43_karmavyati_43"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_43_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmavyatihAre Rac striyAm",
    text_dev              = "कर्मव्यतिहारे णच् स्त्रियाम्",
    padaccheda_dev        = "कर्म-व्यतिहारे णच् स्त्रियाम्",
    why_dev               = "धातोः प्रत्ययः (३.3.43)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
