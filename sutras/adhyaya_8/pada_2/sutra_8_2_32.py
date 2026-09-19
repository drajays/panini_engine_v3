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

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk
from phonology.pratyahara import JHAL


def _find(state: State):
    if len(state.terms) < 2:
        return None
    for i in range(len(state.terms) - 1):
        t, nxt = state.terms[i], state.terms[i + 1]
        if "dhatu" not in t.tags and "anga" not in t.tags:
            continue
        if t.meta.get("8_2_32_dader_Gah_done"):
            continue
        if not t.varnas or t.varnas[0].slp1 != "d" or t.varnas[-1].slp1 != "h":
            continue
        if not nxt.varnas or nxt.varnas[0].slp1 not in JHAL:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas[-1] = mk("G")
    t.meta["8_2_32_dader_Gah_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dAderDAtorGaH",
    text_dev              = "दादेर्धातोर्घः",
    padaccheda_dev        = "द्-आदेः धातोः घः",
    why_dev               = "द्-आदि धातोः हकारस्य झलि घकारादेशः (दुह्→दुघ्, अपवादः 8.2.31)।",
    anuvritti_from        = ('8.2.31',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
