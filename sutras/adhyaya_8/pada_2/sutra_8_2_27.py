"""
8.2.27  ह्रस्वादङ्गात्  —  VIDHI

Padaccheda: ह्रस्वात् अङ्गात्

ह्रस्वादङ्गात् (8.2.27)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
_HRASVA = frozenset("aiufx")
_JHAL = frozenset("kKgGcCjJwWqQtTdDpPbBSzsh")


def _find(state: State) -> int | None:
    """ह्रस्वादङ्गात् (सिचो लोपः 8.2.25 anuvṛtti, झलि 8.2.26): sic's s drops after a
    short-vowel-final aṅga before jhal — अकृत, अकृथाः (vs अकृषाताम्: ā is not jhal)."""
    if not state.tripadi_zone or not state.terms:
        return None
    vs = state.terms[0].varnas
    for i in range(1, len(vs) - 1):
        if ("sic_s" in vs[i].tags and vs[i - 1].slp1 in _HRASVA and "it_agama" not in vs[i - 1].tags
                and vs[i + 1].slp1 in _JHAL):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is not None:
        del state.terms[0].varnas[i]
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.27",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "hrasvAdaNgAt",
    text_dev              = "ह्रस्वादङ्गात्",
    padaccheda_dev        = "ह्रस्वात् अङ्गात्",
    why_dev               = "ह्रस्वान्ताद् अङ्गात् परस्य सिचः सस्य लोपो झलि — अकृत।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
