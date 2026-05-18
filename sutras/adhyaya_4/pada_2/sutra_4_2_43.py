"""
4.2.43  ग्रामजनबन्धुसहायेभ्यः तल्  —  VIDHI

Padaccheda: ग्राम-जन-बन्धु-सहायेभ्यः तल्

ग्रामजनबन्धुसहायेभ्यः तल् (4.2.43)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_43_grAmajanab_43"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_43_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "grAmajanabanDusahAyeByaH tal",
    text_dev              = "ग्रामजनबन्धुसहायेभ्यः तल्",
    padaccheda_dev        = "ग्राम-जन-बन्धु-सहायेभ्यः तल्",
    why_dev               = "(सूत्रम् 4.2.43) ग्रामजनबन्धुसहायेभ्यः तल्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
