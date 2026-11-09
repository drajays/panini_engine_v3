"""Shared by 8.3.17–8.3.22: the seam between two padas on one tape, and the three kinds of left pada they speak of."""
from __future__ import annotations

from engine.state import State

AS = frozenset("aAiIuUfFxXeEoOhyvrlYmNRnJBGQDjbgqd")      # aś: every vowel and every haś
HAS = frozenset("hyvrlYmNRnJBGQDjbgqd")
AVARNA = frozenset("aA")
BHOBHAGOAGHO = ("Bo", "Bago", "aGo")
LAGHU = "laghuprayatnatara_8_3_18"


def seams(state: State):
    """(left Term, right Term) for each pair of neighbouring padas whose seam starts with an aś."""
    for t, u in zip(state.terms, state.terms[1:]):
        if t.varnas and u.varnas and "pada" in t.tags and u.varnas[0].slp1 in AS:
            yield t, u


def pada_stem(t) -> str:
    """The left pada without its last varṇa (what 'bho-', 'bhago-', 'agho-' and 'avarṇa-pūrva' look at)."""
    return "".join(v.slp1 for v in t.varnas[:-1])
