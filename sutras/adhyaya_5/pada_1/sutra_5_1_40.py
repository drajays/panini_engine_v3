"""
5.1.40  पुत्राच्छ च  —  VIDHI

Padaccheda: पुत्रात् छ (लुप्तप्रथमान्तनिर्देशः) च

पुत्राच्छ च (5.1.40)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_40_putrAcCa_40"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_40_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "putrAcCa ca",
    text_dev              = "पुत्राच्छ च",
    padaccheda_dev        = "पुत्रात् छ (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 5.1.40) पुत्राच्छ च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
