"""
8.2.31  हो ढः  —  VIDHI

ह् → ढ् before a jhal or at the pada end. Utsarga: it yields to its apavādas
8.2.32 दादेर्धातोर्घः (the ह् of a द्-initial dhātu — दोग्धा) and 8.2.34 नहो धः
(नद्धा), whose sites are skipped here.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82031 · हो ढः
              padaccheda: हः ढः
              anuvṛtti:   81016: पदस्य | 82026: झलि | 82029: अन्ते च
  Source #2 — Kāśikā 8.2.31 udāharaṇa:
                सोढा
                सोढुम्
                सोढव्यम्
  Cross-check — surface pinned by: tests/unit/test_jiGfkSati_grah_san_desiderative.py;
                ashtadhyayi.com gold दोग्धा / नद्धा (bench/ashtadhyayi_gold.py luṭ)
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
        if slp(c[k]) == "h" and followed_by_jhal_or_end(c, k) and not _apavada_site(c, k):
            return c[k]
    return None


def _apavada_site(c, k: int) -> bool:
    span = dhatu_span(c, k)
    if not span or span[1] != k:
        return False
    root = "".join(slp(x) for x in c[span[0]:k + 1])
    return root.startswith("d") or root == "nah"


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

