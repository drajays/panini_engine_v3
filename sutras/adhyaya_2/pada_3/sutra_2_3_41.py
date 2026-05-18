"""
2.3.41  यतश्च निर्धारणम्  —  VIDHI

Padaccheda: यतः च निर्द्धारणम्

From which nirdharana (specification) occurs, pancami/sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_41_yatas_nirdhara"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_41_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.41"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yataSca nirDAraRam",
    text_dev              = "यतश्च निर्धारणम्",
    padaccheda_dev        = "यतः च निर्द्धारणम्",
    why_dev               = "यतः च निर्धारणम् (२.३.४१)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
