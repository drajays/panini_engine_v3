"""
4.4.121  रक्षोयातूनां हननी  —  VIDHI

Padaccheda: रक्षः-यातूनाम् हननी

रक्षोयातूनां हननी (4.4.121)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_121_rakzoyAtUn_121"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_121_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rakzoyAtUnAM hananI",
    text_dev              = "रक्षोयातूनां हननी",
    padaccheda_dev        = "रक्षः-यातूनाम् हननी",
    why_dev               = "(सूत्रम् 4.4.121) रक्षोयातूनां हननी।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
