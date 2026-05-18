"""
5.1.27  शतमानविंशतिकसहस्रवसनादण्  —  VIDHI

Padaccheda: शतमान-विंशतिक-सहस्र-वसनात् अण्

शतमानविंशतिकसहस्रवसनादण् (5.1.27)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_27_SatamAnavi_27"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_27_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SatamAnaviMSatikasahasravasanAdaR",
    text_dev              = "शतमानविंशतिकसहस्रवसनादण्",
    padaccheda_dev        = "शतमान-विंशतिक-सहस्र-वसनात् अण्",
    why_dev               = "(सूत्रम् 5.1.27) शतमानविंशतिकसहस्रवसनादण्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
