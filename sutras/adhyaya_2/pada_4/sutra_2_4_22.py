"""
2.4.22  छाया बाहुल्ये  —  VIDHI

Padaccheda: छाया बाहुल्ये

chaya in bahulya (abundance) context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_22_bahulye_chaya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_22_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CAyA bAhulye",
    text_dev              = "छाया बाहुल्ये",
    padaccheda_dev        = "छाया बाहुल्ये",
    why_dev               = "बाहुल्ये छाया (२.४.२२)।",
    anuvritti_from        = ('2.4.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
