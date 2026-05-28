"""
8.2.100  अनुदात्तं प्रश्नान्ताभिपूजितयोः  —  VIDHI

Padaccheda: अनुदात्तम् प्रश्नान्त-अभिपूजितयोः

अनुदात्तं प्रश्नान्ताभिपूजितयोः (8.2.100)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_100_anudAttaM_100"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.100"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anudAttaM praSnAntABipUjitayoH",
    text_dev              = "अनुदात्तं प्रश्नान्ताभिपूजितयोः",
    padaccheda_dev        = "अनुदात्तम् प्रश्नान्त-अभिपूजितयोः",
    why_dev               = "(सूत्रम् 8.2.100) अनुदात्तं प्रश्नान्ताभिपूजितयोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
