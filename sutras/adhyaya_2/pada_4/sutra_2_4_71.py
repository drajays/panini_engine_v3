"""
2.4.71  सुपो धातुप्रातिपदिकयोः  —  VIDHI

Within dhātu/prātipadika contexts, *sup* affixes are deleted.

In v3 this rule is used (narrowly, but glass-box) for samāsa demos where
we start from a pair of prātipadikas with their internal sup markers, and
then delete those internal sups before samāsa prātipadika promotion.

Mechanical blindness: the trigger is purely structural/tag-based:
  - there are at least two samāsa members tagged ``samasa_member``
  - at least one Term tagged ``sup`` exists (internal)
The action deletes those sup Terms, mutating the surface (flat slp1).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _sup_term_indexes(state: State) -> list[int]:
    return [i for i, t in enumerate(state.terms) if "sup" in t.tags]


def cond(state: State) -> bool:
    # Require a samāsa context (two or more members).
    members = [t for t in state.terms if "samasa_member" in t.tags]
    if len(members) < 2:
        return False
    return len(_sup_term_indexes(state)) > 0


def act(state: State) -> State:
    idxs = _sup_term_indexes(state)
    if not idxs:
        return state
    # Delete from right to left to keep indexes stable.
    for i in reversed(idxs):
        del state.terms[i]
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.71",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "supo DhAtu-prAtipadikayoH",
    text_dev       = "सुपो धातुप्रातिपदिकयोः",
    padaccheda_dev = "सुपः / धातु-प्रातिपदिकयोः",
    why_dev        = "समास-आदि संरचनात्मक प्रसङ्गे आन्तर-सुप्-प्रत्ययस्य लोपः।",
    anuvritti_from = ("2.4.70",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

