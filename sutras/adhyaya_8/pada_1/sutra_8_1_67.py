"""
8.1.67  पूजनात् पूजितमनुदात्तम् (काष्ठादिभ्यः)  —  VIDHI

Padaccheda: पूजनात् पूजितम् अनुदात्तम् (काष्ठादिभ्यः)

पूजनात् पूजितमनुदात्तम् (काष्ठादिभ्यः) (8.1.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_67_pUjanAt_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_1_67_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUjanAt pUjitamanudAttam (kAzWAdiByaH)",
    text_dev              = "पूजनात् पूजितमनुदात्तम् (काष्ठादिभ्यः)",
    padaccheda_dev        = "पूजनात् पूजितम् अनुदात्तम् (काष्ठादिभ्यः)",
    why_dev               = "(सूत्रम् 8.1.67) पूजनात् पूजितमनुदात्तम् (काष्ठादिभ्यः)।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
