"""
8.2.32  दादेर्धातोर्घः  —  VIDHI

Padaccheda: द्-आदेः धातोः घः

A द्-initial धातु (दुह्, दिह्…) ending in ह्, before a झल्-initial affix,
takes घ् in place of that final ह् — the niyama exception to **8.2.31**
हो ढः (the general ह्→ढ् rule) for this specific root shape: दुह्+ति →
दुघ्+ति (→ 8.2.40 झषस्तथोर्धोऽधः → दुघ्+धि → 8.4.53 झलां जश् झशि → दुग्धि).

Structural like **8.2.7**'s pre-merge branch: needs the dhātu/pratyaya term
boundary the pada-merge is about to erase, so it fires on the still-separate
two-term state (dhātu ends in ह्, phonetically द्-initial; next term starts
with a झल् phoneme) — before ``_pada_merge``. Once this fires, 8.2.31's own
cond() naturally declines (the final phoneme is no longer 'h').

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82032 · दादेर्धातोर्घः
              padaccheda: द्-आदेः धातोः घः
              anuvṛtti:   82026: झलि | 82029: अन्ते च | 82031: होः (होः ढः → घः, अपवादः)
  Source #2 — Mīmāṃsaka Aṣṭādhyāyī-Bhāṣya, pariśiṣṭa (PDF p.784): दुह् + शप् +
              ते → (कर्मवद्भावे) दुघ्+ते, दादेर्धातोर्घः (8.2.32) उदाहृतम्।
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
        if slp(c[k]) != "h" or not followed_by_jhal_or_end(c, k):
            continue
        span = dhatu_span(c, k)
        if span and span[1] == k and slp(c[span[0]]) == "d":
            return c[k]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        substitute(hit, "G")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.32",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "dAderDAtorGaH",
    text_dev              = "दादेर्धातोर्घः",
    padaccheda_dev        = "द्-आदेः धातोः घः",
    why_dev               = "दादेर्धातोर्घः: the ह् of a द्-initial dhātu → घ् (apavāda of 8.2.31) — दुह् → दुघ्, दह् → दघ्.",
    anuvritti_from        = ('8.2.31',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
