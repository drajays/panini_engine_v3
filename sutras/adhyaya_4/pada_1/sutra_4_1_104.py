"""
4.1.104  अनृष्यानन्तर्ये बिदादिभ्योऽञ्  —  VIDHI

Padaccheda: अनृषि (लुप्तपञ्चम्यन्तनिर्देशः) आनन्तर्ये बिद-आदिभ्यः अञ्

अनृष्यानन्तर्ये बिदादिभ्योऽञ् (4.1.104)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_104_anfzyAnant_104"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.104", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anfzyAnantarye bidAdiByo'Y",
    text_dev              = "अनृष्यानन्तर्ये बिदादिभ्योऽञ्",
    padaccheda_dev        = "अनृषि (लुप्तपञ्चम्यन्तनिर्देशः) आनन्तर्ये बिद-आदिभ्यः अञ्",
    why_dev               = "(सूत्रम् 4.1.104) अनृष्यानन्तर्ये बिदादिभ्योऽञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
