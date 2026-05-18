"""
4.3.7  ग्रामजनपदैकदेशादञ्ठञौ  —  VIDHI

Padaccheda: ग्राम-जनपद-एकदेशात् अञ्-ठञौ

ग्रामजनपदैकदेशादञ्ठञौ (4.3.7)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_7_grAmajanap_7"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_7_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "grAmajanapadEkadeSAdaYWaYO",
    text_dev              = "ग्रामजनपदैकदेशादञ्ठञौ",
    padaccheda_dev        = "ग्राम-जनपद-एकदेशात् अञ्-ठञौ",
    why_dev               = "(सूत्रम् 4.3.7) ग्रामजनपदैकदेशादञ्ठञौ।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
