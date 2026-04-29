"""
engine/it_phonetic.py — *it*-varṇa row vs ``State.flat_slp1()`` (trace / joiner).

*It*-saṃjñā sūtras (**1.3.2**–**1.3.8**) add tags; **1.3.9** is the *vidhi* that
removes the Varṇa rows.  ``State.flat_slp1()`` is therefore the concatenation of
*all* ``Term.varnas`` still on the tape, **including** *it*-tagged but not yet
*loped* letters — so trace ``form_before`` / ``form_after`` match śāstrīya
responsibility (no “phantom lopa” at 1.3.3/1.3.8; real lopa at 1.3.9).  No
separate *phonemic* hiding before **1.3.9**; *lopa* is the physical **pop** in
``sutra_1_3_9.act``.

``IT_LOPA_TAGS`` remains the single deletable set (see ``sutra_1_3_9``).
"""
from __future__ import annotations

from typing import Any, Final, FrozenSet, List

from engine.lopa_ghost import LUK_LOPA_GHOST_TAG

# Single source — must match ``sutra_1_3_9`` deletion set.
IT_LOPA_TAGS: Final[FrozenSet[str]] = frozenset((
    "it",
    "it_candidate_halantyam",
    "it_candidate_anunasika",
    "it_candidate_irit",
    "it_candidate_nit_tu_du",
    "it_candidate_sha_pratyaya",
    "it_candidate_cutu",
    "it_candidate_lasaku",
))


def varna_contributes_phonetically(_v: Any, _term: Any) -> bool:
    """
    All Varṇas on ``term.varnas`` contribute until **1.3.9** *pops* them; the
    parameters are kept for a stable public signature / future hooks.
    """
    return True


def term_phonetic_varnas(term: Any) -> List[Any]:
    """Linear ``Term.varnas`` in order (``flat_slp1`` = surface tape until 1.3.9 *lopa*)."""
    if LUK_LOPA_GHOST_TAG in getattr(term, "tags", ()):
        return []
    return [v for v in term.varnas if varna_contributes_phonetically(v, term)]


def term_phonetic_slp1(term: Any) -> str:
    return "".join(v.slp1 for v in term_phonetic_varnas(term))
