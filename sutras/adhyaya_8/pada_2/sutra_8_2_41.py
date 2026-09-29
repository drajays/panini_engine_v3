"""
8.2.41  षढोः कः सि  —  VIDHI (narrow demo)

Demo slice (जिघृक्षति):
  Replace final `D` with `k` when `s` follows: ...D + s... → ...k + s...

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82041 · षढोः कः सि
              padaccheda: ष-ढोः कः सि
  Source #2 — Kāśikā 8.2.41 udāharaṇa:
                षकारस्य — पिष् — पेक्ष्यति
                अपेक्ष्यत्
                पिपिक्षति
  Cross-check — surface pinned by: tests/unit/test_jiGfkSati_grah_san_desiderative.py
  Reference record: sutra_ref_out/8_2_41.json
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
    for k in range(len(c) - 1):
        if slp(c[k]) in ("z", "Q") and slp(c[k + 1]) == "s":
            return c[k]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        substitute(hit, "k")
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.41",
    sutra_type= SutraType.VIDHI,
    text_slp1='zaQoH kaH si',
    text_dev='षढोः कः सि',
    padaccheda_dev="षढोः / कः / सि",
    why_dev= "षढोः कः सि: ष्/ढ् before स् → क् — लेढ्+स्य → लेक्+स्य.",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

