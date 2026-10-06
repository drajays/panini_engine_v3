"""
8.2.18  कृपो रो लः  —  VIDHI

In kṛp (कृपू) the r — and the ṛ vowel, as ḷ — become l: कल्पते, चक्लृपे, अक्लृप्त (KV/SK §43; Vidyut: kalpate, cakxpe, akxpat).
Source: ashtadhyayi.com data row 82018.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


_STEMS = frozenset({"kfp", "karp", "kArp", "kFp"})       # kṛp as the tape shows it after guṇa/vṛddhi (the merged pada keeps no root meta)


def _site(state: State):
    if not state.tripadi_zone:
        return None
    from sutras.adhyaya_8.pada_2._tape import dhatu_span, flat, slp
    c = flat(state)
    k = 0
    while k < len(c):
        span = dhatu_span(c, k)
        if not span:
            k += 1
            continue
        a, b = span
        k = b + 1
        if "".join(slp(x) for x in c[a:b + 1]) in _STEMS and any(slp(x) in ("r", "f", "F") for x in c[a:b + 1]):
            return c[a:b + 1]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    from sutras.adhyaya_8.pada_2._tape import slp, substitute
    cells = _site(state)
    if cells is not None:
        for x in cells:
            new = {"r": "l", "f": "x", "F": "X"}.get(slp(x))
            if new:
                substitute(x, new)
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.18",
    sutra_type=SutraType.VIDHI,
    text_slp1="kfpo ro laH",
    text_dev="कृपो रो लः",
    padaccheda_dev="कृपः रः लः",
    why_dev="कृपू-धातोः रेफस्य लकारः (कल्पते)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
