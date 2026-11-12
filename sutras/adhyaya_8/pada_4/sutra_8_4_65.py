"""
8.4.65  झरो झरि सवर्णे  —  VIBHASHA
After a hal, a jhar is dropped before a savarṇa jhar, optionally.
Works on the flat varṇa sequence of the tape (one pada, or two on a seam): a letter that stands between a hal and an identical-kind
(savarṇa) letter is dropped, optionally; each application removes one letter, so a cluster of three goes to two, then one.
Kāśikā 8.4.65: pratta from prattta; kṛnṭha beside kṛntṭha (t, ṭh are savarṇa); kṣuṇte.
Pāṭha: ashtadhyayi.com data.txt row i=84065 (Art. 14).
"""
from __future__ import annotations
from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.savarna import is_savarna

_HAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh")
_TARGET = frozenset('JBGQDjbgqdKPCWTcwtkpSzs')
_NEXT = frozenset('JBGQDjbgqdKPCWTcwtkpSzs')


def _site(state: State):
    """(term, index) of the letter to drop: hal, target, savarṇa-of-target — read off the flat tape."""
    if not state.tripadi_zone:
        return None
    flat = [(t, i, v.slp1) for t in state.terms for i, v in enumerate(t.varnas)]
    for k in range(len(flat) - 2):
        (_, _, a), (t, i, b), (_, _, c) = flat[k], flat[k + 1], flat[k + 2]
        if a in _HAL and b in _TARGET and c in _NEXT and is_savarna(b, c):
            return t, i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, i = _site(state)
    del t.varnas[i]
    return state


SUTRA = SutraRecord(
    sutra_id         = "8.4.65",
    sutra_type       = SutraType.VIBHASHA,
    vibhasha_default = False,
    text_slp1        = 'Jaro Jari savarRe',
    text_dev         = 'झरो झरि सवर्णे',
    samagra_slp1     = 'hallaH Jaro Jari savarRe anyatarasyAm',
    samagra_dev      = 'हलः झरो झरि सवर्णे अन्यतरस्याम्',
    padaccheda_dev   = 'झरो झरि सवर्णे',
    why_dev          = '(8.4.65) After a hal, a jhar is dropped before a savarṇa jhar, optionally.',
    anuvritti_from   = ("8.4.62",),
    vibhasha_scope   = cond,
    cond             = cond,
    act              = act,
)
register_sutra(SUTRA)
