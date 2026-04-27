"""
pipelines/asme_indrAbfhaspatI_pragRhya_demo.py — *अस्मे इन्द्राबृहस्पती* & related Vedic *śe* + *iti*.

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/अस्मे इन्द्राबृहस्पती.md``.

**7.1.39** *śe* substitute (with *it*-lopa etc.) yields forms ending in *e* (**``asme``**,
**``yuṣme``**, **``tve``**, **``me``** SLP1). Before a following *ac* (**6.1.78** *ecoyavāyāvaḥ*),
that *e* would split to *ay*. *Kāśikā* on **1.1.13** *śe* treats that residue as *pragṛhya*;
**6.1.125** *prakṛti-bhāva* blocks sandhi.

Engine path: arm ``SHE_PRAGHYA_TAG_ARM_META`` on ``State``, ``apply_rule("1.1.11", s)``
(so **1.1.11** *act* tags final-*e* *aṅga*/*prātipadika*), then **6.1.125** + **6.1.78**.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import SHE_PRAGHYA_TAG_ARM_META


def _two_word_state(left_slp1: str, right_slp1: str) -> State:
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(left_slp1),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": left_slp1},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(right_slp1),
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": right_slp1},
    )
    return State(terms=[left, right], meta={}, trace=[])


def _apply_she_pragrahya_then_block_ec78(s: State) -> State:
    s.meta[SHE_PRAGHYA_TAG_ARM_META] = True
    s = apply_rule("1.1.11", s)
    s = apply_rule("6.1.125", s)
    s = apply_rule("6.1.78", s)
    return s


def derive_asme_indrAbfhaspatI_pragrahya() -> State:
    """*asme* + *indrAbfhaspatI* — no *e*→*ay* before initial *i*."""
    s = _two_word_state("asme", "indrAbfhaspatI")
    return _apply_she_pragrahya_then_block_ec78(s)


def derive_tve_iti_pragrahya() -> State:
    """*tve* + *iti* (Vedic *yuṣmad* loc.–style residue)."""
    s = _two_word_state("tve", "iti")
    right = s.terms[1]
    right.tags.add("nipāta")
    return _apply_she_pragrahya_then_block_ec78(s)


def derive_me_iti_pragrahya() -> State:
    """*me* + *iti* (Vedic *asmad* residue)."""
    s = _two_word_state("me", "iti")
    s.terms[1].tags.add("nipāta")
    return _apply_she_pragrahya_then_block_ec78(s)


__all__ = [
    "derive_asme_indrAbfhaspatI_pragrahya",
    "derive_me_iti_pragrahya",
    "derive_tve_iti_pragrahya",
]
