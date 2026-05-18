"""
5.2.119  शतसहस्रान्ताच्च निष्कात्  —  VIDHI

Padaccheda: शत-सहस्र-अन्तात् च निष्कात्

शतसहस्रान्ताच्च निष्कात् (5.2.119)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_119_Satasahasr_119"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_119_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.119"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.119",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SatasahasrAntAcca nizkAt",
    text_dev              = "शतसहस्रान्ताच्च निष्कात्",
    padaccheda_dev        = "शत-सहस्र-अन्तात् च निष्कात्",
    why_dev               = "(सूत्रम् 5.2.119) शतसहस्रान्ताच्च निष्कात्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
