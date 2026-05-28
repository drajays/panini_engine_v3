"""
3.4.62  नाधाऽर्थप्रत्यये च्व्यर्थे  —  VIDHI

Padaccheda: ना-धा-अर्थ-प्रत्यये च्वि-अर्थे

krt-suffix rule: नाधाऽर्थप्रत्यये च्व्यर्थे
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_62_nADArTapr_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nADA'rTapratyaye cvyarTe",
    text_dev              = "नाधाऽर्थप्रत्यये च्व्यर्थे",
    padaccheda_dev        = "ना-धा-अर्थ-प्रत्यये च्वि-अर्थे",
    why_dev               = "धातोः प्रत्ययः (३.4.62)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
