"""
3.4.48  हिंसार्थानां च समानकर्मकाणाम्  —  VIDHI

Padaccheda: हिंसा-अर्थानाम् च समान-कर्मकाणाम्

krt-suffix rule: हिंसार्थानां च समानकर्मकाणाम्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_48_hiMsArTAnA_48"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hiMsArTAnAM ca samAnakarmakARAm",
    text_dev              = "हिंसार्थानां च समानकर्मकाणाम्",
    padaccheda_dev        = "हिंसा-अर्थानाम् च समान-कर्मकाणाम्",
    why_dev               = "धातोः प्रत्ययः (३.4.48)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
