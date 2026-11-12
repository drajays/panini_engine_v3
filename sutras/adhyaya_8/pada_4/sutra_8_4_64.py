"""
8.4.64  हलो यमां यमि लोपः  —  VIBHASHA
After a hal, a yam (y v r l ñ m ṅ ṇ n) is dropped before a savarṇa yam, optionally (anyatarasyām).
Works on the flat varṇa sequence of the tape (one pada, or two on a seam): a letter that stands between a hal and an identical-kind
(savarṇa) letter is dropped, optionally; each application removes one letter, so a cluster of three goes to two, then one.
Kāśikā 8.4.64: Sayyā / Sayyyā → Sayyā, Śayā; Ādityaḥ from Ādityyaḥ; (agnyā: n and y are not savarṇa, nothing drops).
Pāṭha: ashtadhyayi.com data.txt row i=84064 (Art. 14).
"""
from __future__ import annotations
from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.savarna import is_savarna

_HAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh")
_TARGET = frozenset('yvrlYmNRn')
_NEXT = frozenset('yvrlYmNRn')


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
    sutra_id         = "8.4.64",
    sutra_type       = SutraType.VIBHASHA,
    vibhasha_default = False,
    text_slp1        = 'halo yamAM yami lopaH',
    text_dev         = 'हलो यमां यमि लोपः',
    samagra_slp1     = 'hallaH halo yamAM yami lopaH anyatarasyAm',
    samagra_dev      = 'हलः हलो यमां यमि लोपः अन्यतरस्याम्',
    padaccheda_dev   = 'हलो यमां यमि लोपः',
    why_dev          = '(8.4.64) After a hal, a yam (y v r l ñ m ṅ ṇ n) is dropped before a savarṇa yam, optionally (anyatarasyām).',
    anuvritti_from   = ("8.4.62",),
    cond             = cond,
    act              = act,
)
register_sutra(SUTRA)
