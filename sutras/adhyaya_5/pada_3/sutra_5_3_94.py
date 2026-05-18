"""
5.3.94  एकाच्च प्राचाम्  —  VIDHI

Padaccheda: एकात् च प्राचाम्

एकाच्च प्राचाम् (5.3.94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_94_ekAcca_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_94_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ekAcca prAcAm",
    text_dev              = "एकाच्च प्राचाम्",
    padaccheda_dev        = "एकात् च प्राचाम्",
    why_dev               = "(सूत्रम् 5.3.94) एकाच्च प्राचाम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
