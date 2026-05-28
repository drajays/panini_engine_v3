"""
8.2.6  स्वरितो वाऽनुदात्ते पदादौ  —  VIDHI

Padaccheda: स्वरितः वा अनुदात्ते पद-आदौ

स्वरितो वाऽनुदात्ते पदादौ (8.2.6)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_6_svarito_6"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_6_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svarito vA'nudAtte padAdO",
    text_dev              = "स्वरितो वाऽनुदात्ते पदादौ",
    padaccheda_dev        = "स्वरितः वा अनुदात्ते पद-आदौ",
    why_dev               = "(सूत्रम् 8.2.6) स्वरितो वाऽनुदात्ते पदादौ।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
