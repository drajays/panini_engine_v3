"""
8.2.8  न ङिसम्बुद्ध्योः  —  VIDHI

Padaccheda: न ङि-सम्बुद्ध्योः

न ङिसम्बुद्ध्योः (8.2.8)
Pāṭha: ashtadhyayi.com data.txt row i=82008 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_BLOCKS = ("8.2.7",)      # nalopaḥ prātipadikāntasya


def cond(state: State) -> bool:
    """The pada ends in the prātipadika's n and is a ṅi-sup form or a sambuddhi (he rājan; rājani)."""
    if not state.tripadi_zone or len(state.terms) != 1 or "pada" not in state.terms[0].tags:
        return False
    t = state.terms[0]
    return bool(t.varnas) and t.varnas[-1].slp1 == "n" and ("sambuddhi" in t.tags or "ngi" in t.tags) \
        and not set(_BLOCKS) <= state.blocked_sutras


def act(state: State) -> State:
    state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.8",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na NisambudDyoH",
    text_dev              = "न ङिसम्बुद्ध्योः",
    samagra_slp1          = "prAtipadikasya padasya antyasya naH lopaH Ni-sambudDyOH na",
    samagra_dev           = "प्रातिपदिकस्य पदस्य अन्त्यस्य नः लोपः ङि-सम्बुद्ध्यौः न",
    padaccheda_dev        = "न ङि-सम्बुद्ध्योः",
    why_dev               = "न ङिसम्बुद्ध्योः — ङौ सम्बुद्धौ च नलोपः न (हे राजन्)।",
    anuvritti_from        = ('8.1.1',),
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
