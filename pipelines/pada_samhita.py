"""
pipelines/pada_samhita.py — two finished padas in saṃhitā (1.4.109 परः सन्निकर्षः संहिता): vowel sandhi at the seam.

``join(left_slp1, right_slp1)`` puts both padas on one tape, opens **6.1.72** संहितायाम्, and lets the
engine choose: of the ac-sandhi sūtras below, those that would change the tape
(``scheduler.effective_candidates``) go to the resolver, whose Ladder 1 puts the apavāda first
(**6.1.101** over **6.1.87** / **6.1.77**, **6.1.88** over **6.1.87**, **6.1.109** over **6.1.78**; Art. 21).
This file lists the candidates; it orders nothing.

Scope: a vowel–vowel seam. Visarga and consonant seams need the tripāḍī (8.2.66, 8.3.x, 8.4.x)
on a multi-pada tape, which does not exist yet — ``seam_kind`` names them so callers report a
gap (Art. 18) instead of joining them some other way. Pragṛhya (1.1.11–19 → **6.1.125**) needs the
pada's vacana; a pada given as a bare string carries none.

CONSTITUTION Art. 7: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.resolver import resolve
from engine.scheduler import effective_candidates
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

AC_SANDHI = ("6.1.77", "6.1.78", "6.1.87", "6.1.88", "6.1.101", "6.1.109", "6.1.125")
_VOWELS = set("aAiIuUfFxXeEoO")
MAX_STEPS = 6


def seam_kind(left_slp1: str, right_slp1: str) -> str:
    """'ac' when a vowel meets a vowel; otherwise the seam needs the (not yet multi-pada) tripāḍī."""
    if left_slp1[-1:] in _VOWELS and right_slp1[:1] in _VOWELS:
        return "ac"
    if left_slp1[-1:] in ("H", "s", "r"):
        return "visarga"
    return "hal"


def _pada(slp1: str) -> Term:
    return Term(kind="pada", varnas=list(parse_slp1_upadesha_sequence(slp1)), tags={"pada"}, meta={"upadesha_slp1": slp1})


def join(left_slp1: str, right_slp1: str) -> State:
    """Both padas in saṃhitā; the 6.1 ac-sandhi sūtras the resolver picks, one at a time, until none applies."""
    if seam_kind(left_slp1, right_slp1) != "ac":
        raise ValueError(f"{left_slp1} + {right_slp1}: {seam_kind(left_slp1, right_slp1)} seam — "
                         "needs the tripāḍī across padas (8.2.66 / 8.3 / 8.4), not yet built")
    s = State(terms=[_pada(left_slp1), _pada(right_slp1)], meta={}, trace=[])
    s = apply_rule("6.1.72", s)
    for _ in range(MAX_STEPS):
        usable = effective_candidates(list(AC_SANDHI), s)
        if not usable:
            break
        s = apply_rule(resolve(usable, s), s)
    return s


__all__ = ["AC_SANDHI", "join", "seam_kind"]
