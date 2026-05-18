"""
8.3.51  पञ्चम्याः परावध्यर्थे  —  VIDHI

Padaccheda: पञ्चम्याः परौ अधि-अर्थे

पञ्चम्याः परावध्यर्थे (8.3.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_51_paYcamyAH_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_51_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paYcamyAH parAvaDyarTe",
    text_dev              = "पञ्चम्याः परावध्यर्थे",
    padaccheda_dev        = "पञ्चम्याः परौ अधि-अर्थे",
    why_dev               = "(सूत्रम् 8.3.51) पञ्चम्याः परावध्यर्थे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
