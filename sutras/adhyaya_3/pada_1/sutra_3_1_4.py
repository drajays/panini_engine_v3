"""
3.1.4  अनुदात्तौ सुप्पितौ  —  SAMJNA (narrow)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=31004):** *anudattau suppitau* —
*sup*-affixes in the *pita* context are *anudātta* on their first syllable
(operational *saṃjñā* **suppita** here: register membership, no *svara* on
the flat tape in v3).

Narrow v3:
  • ``cond`` — last ``Term`` is ``sup`` + ``upadesha``; penultimate ``Term`` is
    tagged ``anga``; not yet marked ``3_1_4_suppita_registered``.
  • ``act`` — add that affix's ``upadesha_slp1`` to ``samjna_registry['suppita']``
    and set the one-shot meta flag on the pratyāya ``Term``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _eligible(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    sup_t = state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in sup_t.tags or "upadesha" not in sup_t.tags:
        return False
    if sup_t.meta.get("3_1_4_suppita_registered"):
        return False
    return True


def cond(state: State) -> bool:
    return _eligible(state)


def act(state: State) -> State:
    if not _eligible(state):
        return state
    sup_t = state.terms[-1]
    up = (sup_t.meta.get("upadesha_slp1") or "").strip() or "?"
    prev = set(state.samjna_registry.get("suppita", frozenset()))
    prev.add(up)
    state.samjna_registry["suppita"] = frozenset(prev)
    sup_t.meta["3_1_4_suppita_registered"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.4",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "anudattau suppitau",
    text_dev       = "अनुदात्तौ सुप्पितौ",
    padaccheda_dev = "अनुदात्तौ सुप्पितौ",
    why_dev        = "सुप्पित-प्रत्ययौ आद्यनुदात्तौ — संज्ञा-पञ्जीकरणम् (त्रैचिके अनुदात्त-चिह्नं नास्ति)।",
    anuvritti_from = ("3.1.1", "3.1.2", "3.1.3"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
