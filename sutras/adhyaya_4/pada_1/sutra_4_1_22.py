"""
4.1.22  अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि  —  VIDHI

Padaccheda: अपरिमाण-बिस्त-अचित-कम्बल्येभ्यः न तद्धित-लुकि

अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि (4.1.22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_22_aparimARab_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_22_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aparimARabistAcitakambalyeByo na tadDitaluki",
    text_dev              = "अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि",
    padaccheda_dev        = "अपरिमाण-बिस्त-अचित-कम्बल्येभ्यः न तद्धित-लुकि",
    why_dev               = "(सूत्रम् 4.1.22) अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
