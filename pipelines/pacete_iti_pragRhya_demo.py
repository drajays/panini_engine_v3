"""
pipelines/pacete_iti_pragRhya_demo.py — *पचेते इति* (laṭ *ātmanepada* 3du *pac* + *iti*).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/पचेते इति.md``.

The note’s OCR thread: after *śap* / *ātmanepada* / *dvivacana* *tin* suffix work the
*tiṅanta* ends in *e* (e.g. *pacete*); before *iti*, **6.1.78** (*ecoyavāyāvaḥ*) would
split the final *e* before *iti*’s *i* (*e*+*i* → *a*+*y*+*i*), but **1.1.11** *pragṛhya*
on *dvivacana* *anta* *e* and **6.1.125** *prakṛti-bhāva* block that — surface
*pacete iti*, not *pacetayiti*.

Full *tiṅ* derivation for *pac*+laṭ+3du+Āt is not wired end-to-end here; the demo
isolates the sandhi slice (same pattern as ``mAle_iti_pragRhya_demo``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


def _pacete_iti_state() -> State:
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("pacete"),
        tags={"anga", "prātipadika", PRAGHYA_TERM_TAG},
        meta={"upadesha_slp1": "qupac~z"},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("iti"),
        tags={"nipāta"},
        meta={"upadesha_slp1": "iti"},
    )
    return State(terms=[left, right], meta={}, trace=[])


def derive_pacete_iti_pragrahya() -> State:
    """*pacete* + *iti* — no *e*→*ay* under **6.1.78** at pragṛhya ‖ *ac*."""
    s = _pacete_iti_state()
    s = apply_rule("6.1.125", s)
    s = apply_rule("6.1.78", s)
    return s


__all__ = ["derive_pacete_iti_pragrahya"]
