"""
2.3.34  दूरान्तिकार्थैः षष्ठ्यन्यतरस्याम्  —  VIDHI

Padaccheda: दूर-अन्तिक-अर्थैः षष्ठी अन्यतरस्याम्

Distant/near words optionally take sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_34_dura_antika_sasthi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dUrAntikArTEH zazWyanyatarasyAm",
    text_dev              = "दूरान्तिकार्थैः षष्ठ्यन्यतरस्याम्",
    padaccheda_dev        = "दूर-अन्तिक-अर्थैः षष्ठी अन्यतरस्याम्",
    why_dev               = "दूर-अन्तिक-अर्थैः षष्ठी अन्यतरस्याम् (२.३.३४)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
