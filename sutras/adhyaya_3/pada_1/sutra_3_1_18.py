"""
3.1.18  सुखादिभ्यः कर्तृवेदनायाम्  —  VIDHI

Padaccheda: सुख-आदिभ्यः कर्तृ (लुप्तषष्ठ्यन्तनिर्देशः) वेदनायाम्

Krt suffix rule from dhatu: सुखादिभ्यः कर्तृवेदनायाम् (18)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_18_suKAdiByaH_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_18_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "suKAdiByaH kartfvedanAyAm",
    text_dev              = "सुखादिभ्यः कर्तृवेदनायाम्",
    padaccheda_dev        = "सुख-आदिभ्यः कर्तृ (लुप्तषष्ठ्यन्तनिर्देशः) वेदनायाम्",
    why_dev               = "धातोः [सुखादिभ्यः कर्तृवेदनायाम्]-प्रत्ययः विहितः (३.१.18)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
