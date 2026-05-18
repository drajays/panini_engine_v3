"""
5.4.53  अभिविधौ सम्पदा च  —  VIDHI

Padaccheda: अभिविधौ सम्पदा च

अभिविधौ सम्पदा च (5.4.53)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_53_aBiviDO_53"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_53_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aBiviDO sampadA ca",
    text_dev              = "अभिविधौ सम्पदा च",
    padaccheda_dev        = "अभिविधौ सम्पदा च",
    why_dev               = "(सूत्रम् 5.4.53) अभिविधौ सम्पदा च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
