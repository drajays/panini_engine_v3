"""
8.2.104  क्षियाऽऽशीःप्रैषेषु तिङ् आकाङ्क्षम्  —  VIDHI

Padaccheda: क्षिया-आशीः-प्रैषेषु तिङ् आकाङ्क्षम्

क्षियाऽऽशीःप्रैषेषु तिङ् आकाङ्क्षम् (8.2.104)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_104_kziyASIH_104"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_104_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kziyA''SIHprEzezu tiN AkANkzam",
    text_dev              = "क्षियाऽऽशीःप्रैषेषु तिङ् आकाङ्क्षम्",
    padaccheda_dev        = "क्षिया-आशीः-प्रैषेषु तिङ् आकाङ्क्षम्",
    why_dev               = "(सूत्रम् 8.2.104) क्षियाऽऽशीःप्रैषेषु तिङ् आकाङ्क्षम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
