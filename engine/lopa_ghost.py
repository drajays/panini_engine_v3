"""
engine/lopa_ghost.py — *luk*/*lopa* “zero-width” *Term* contract (v3.1+).

**1.1.60** *adarśanaṃ lopaḥ*: deletion is invisibility, not removal from the
structural tape. After **2.4.71** *supo luk*, internal *sup* ``Term``s stay in
``state.terms`` with:

  • ``varnas`` cleared (no phonetic contribution to ``flat_slp1()``);
  • ``LUK_LOPA_GHOST_TAG`` (``luk_lopa``) added;
  • original tags retained (e.g. ``sup``, ``pratyaya``) so *pratyayalakṣaṇam*
    scans can still see the affix *class*.

Downstream *vidhi* that need **phonetic** *sup* material must exclude ghosts
via ``term_sup_phonetically_live``; rules that mean “any *sup* slot” may still
use ``\"sup\" in t.tags`` (includes ghosts — e.g. **4.1.2** must not attach a
second *sup*).
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.state import State, Term

LUK_LOPA_GHOST_TAG: str = "luk_lopa"


def term_sup_phonetically_live(t: "Term") -> bool:
    """True iff this *sup* still has phonetic body (not yet *luk*-ghosted)."""
    return "sup" in t.tags and LUK_LOPA_GHOST_TAG not in t.tags


def term_is_sup_luk_ghost(t: "Term") -> bool:
    return "sup" in t.tags and LUK_LOPA_GHOST_TAG in t.tags


def state_sup_luk_ghost_indexes(state: "State") -> list[int]:
    return [i for i, t in enumerate(state.terms) if term_is_sup_luk_ghost(t)]


def state_live_sup_indexes(state: "State") -> list[int]:
    """Indexes of *sup* terms that **2.4.71** may still annihilate (not yet ghost)."""
    return [i for i, t in enumerate(state.terms) if term_sup_phonetically_live(t)]


def state_has_sup_luk_ghost(state: "State") -> bool:
    return any(term_is_sup_luk_ghost(t) for t in state.terms)


def iter_anga_to_following_pratyaya_pairs(state: "State"):
    """
    Yield ``(anga_index, pratyaya_index)`` for tape scans that used to assume
    consecutive ``terms[i], terms[i+1]`` — skips **2.4.71** *sup* ghosts between.
    """
    for j in range(1, len(state.terms)):
        pr = state.terms[j]
        if term_is_sup_luk_ghost(pr):
            continue
        k = j - 1
        while k >= 0 and term_is_sup_luk_ghost(state.terms[k]):
            k -= 1
        if k < 0:
            continue
        yield k, j
