"""
3.1.16  बाष्पोष्माभ्यां उद्वमने  —  VIDHI

Padaccheda: बाष्प-ऊष्माभ्याम् उद्वमने

Krt suffix rule from dhatu: बाष्पोष्माभ्यां उद्वमने (16)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_16_bAzpozmAByAM_16"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_16_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.16"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bAzpozmAByAM udvamane",
    text_dev              = "बाष्पोष्माभ्यां उद्वमने",
    padaccheda_dev        = "बाष्प-ऊष्माभ्याम् उद्वमने",
    why_dev               = "धातोः [बाष्पोष्माभ्यां उद्वमने]-प्रत्ययः विहितः (३.१.16)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
