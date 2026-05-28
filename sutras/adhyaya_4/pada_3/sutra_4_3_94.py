"""
4.3.94  तूदीशलातुरवर्मतीकूचवाराड्ढक्छण्ढञ्यकः  —  VIDHI

Padaccheda: तूदी-शलातुर-वर्मती-कूचवारात् ढक्-छण्-ढञ्-यकः

तूदीशलातुरवर्मतीकूचवाराड्ढक्छण्ढञ्यकः (4.3.94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_94_tUdISalAtu_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.94", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tUdISalAturavarmatIkUcavArAqQakCaRQaYyakaH",
    text_dev              = "तूदीशलातुरवर्मतीकूचवाराड्ढक्छण्ढञ्यकः",
    padaccheda_dev        = "तूदी-शलातुर-वर्मती-कूचवारात् ढक्-छण्-ढञ्-यकः",
    why_dev               = "(सूत्रम् 4.3.94) तूदीशलातुरवर्मतीकूचवाराड्ढक्छण्ढञ्यकः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
