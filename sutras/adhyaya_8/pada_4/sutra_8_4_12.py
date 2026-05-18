"""
8.4.12  एकाजुत्तरपदे णः  —  VIDHI

Padaccheda: एक-अच्-उत्तरपदे णः

एकाजुत्तरपदे णः (8.4.12)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_12_ekAjuttara_12"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_12_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ekAjuttarapade RaH",
    text_dev              = "एकाजुत्तरपदे णः",
    padaccheda_dev        = "एक-अच्-उत्तरपदे णः",
    why_dev               = "(सूत्रम् 8.4.12) एकाजुत्तरपदे णः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
