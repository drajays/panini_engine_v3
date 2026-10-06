"""
8.2.37  एकाचो बशो भष् झषन्तस्य स्ध्वोः  —  VIDHI (narrow demo)

Demo slice (जिघृक्षति):
  For a one-vowel (ekāc) base ending in jhaṣ (`D`), when `s` follows, replace the
  initial `g` (baś) with `G` (bhaṣ) i.e. g → gh.
Pāṭha: ashtadhyayi.com data.txt row i=82037 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from sutras.adhyaya_8.pada_2._tape import (
    AC, BAS_TO_BHAS, JHAS, dhatu_span, flat, followed_by_jhal_or_end, slp, substitute,
)


def _site(state: State):
    if not state.tripadi_zone:
        return None
    c = flat(state)
    k = 0
    while k < len(c):
        span = dhatu_span(c, k)
        if not span:
            k += 1
            continue
        a, b = span
        k = b + 1
        root = [slp(x) for x in c[a:b + 1]]
        if root[0] not in BAS_TO_BHAS or root[-1] not in JHAS:
            continue
        if sum(1 for ch in root if ch in AC) != 1:
            continue                                   # एकाचः
        nxt = slp(c[b + 1]) if b + 1 < len(c) else ""
        nxt2 = slp(c[b + 2]) if b + 2 < len(c) else ""
        if nxt == "s" or (nxt == "D" and nxt2 == "v") or b + 1 >= len(c):
            return c[a]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        substitute(hit, BAS_TO_BHAS[slp(hit)])
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.37",
    sutra_type= SutraType.VIDHI,
    text_slp1='ekAco baSo Baz Jazantasya sDvoH',
    text_dev='एकाचो बशो भष् झषन्तस्य स्ध्वोः',
    samagra_slp1="DAtoH ekAcaH Jazantasya baSaH sDvoH padasya ante ca Baz",
    samagra_dev="धातोः एकाचः झषन्तस्य बशः स्ध्वोः पदस्य अन्ते च भष्",
    padaccheda_dev="एकाचः / बशः / भष् / झषन्तस्य / स्ध्वोः",
    why_dev= "एकाचो बशो भष् झषन्तस्य स्ध्वोः: a one-vowel dhātu beginning with बश् and ending in झष् aspirates its initial before स्/ध्व् or at the end — दुघ्+स्य → धुघ्+स्य (धोक्ष्यति).",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

