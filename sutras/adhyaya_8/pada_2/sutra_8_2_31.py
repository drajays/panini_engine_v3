"""
8.2.31  हो ढः  —  VIDHI (narrow demo)

Demo slice (जिघृक्षति):
  In the grah-desiderative base, replace final `h` with `D` before following `s`
  (of san term).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82031 · हो ढः
              padaccheda: हः ढः
              anuvṛtti:   81016: पदस्य | 82026: झलि | 82029: अन्ते च
  Source #2 — Kāśikā 8.2.31 udāharaṇa:
                सोढा
                सोढुम्
                सोढव्यम्
  Cross-check — surface pinned by: tests/unit/test_jiGfkSati_grah_san_desiderative.py
  Reference record: sutra_ref_out/8_2_31.json
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
    for k in range(len(c)):
        if slp(c[k]) == "h" and followed_by_jhal_or_end(c, k):
            return c[k]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        substitute(hit, "Q")
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.31",
    sutra_type= SutraType.VIDHI,
    text_slp1='ho QaH',
    text_dev='हो ढः',
    padaccheda_dev="हो / ढः",
    why_dev= "हो ढः: ह् → ढ् before a jhal or at the pada end — लिह्+स्य → लिढ्+स्य.",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

