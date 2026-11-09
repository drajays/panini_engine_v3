"""
8.4.37  पदान्तस्य  —  PRATISHEDHA

padāntasya: a pada-final n is not turned to ṇ (वृक्षान्, अरीन्, गिरीन्).
Pāṭha: ashtadhyayi.com data.txt row i=84037 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_4.sutra_8_4_2 import _BLOCKERS

TAG = "natva_done"          # the tag 8.4.1 / 8.4.2 already skip: ṇatva is settled for this n (here: barred)
_RASHA = frozenset("rfFz")


def _ns(state: State):
    """Every untagged n that 8.4.1 / 8.4.2 would turn to ṇ: after r / ṛ / ṣ with no blocker between, before a vowel or y v m n, or pada-final."""
    flat = [v for t in state.terms for v in t.varnas]
    out = []
    for k, v in enumerate(flat):
        if v.slp1 != "n" or TAG in v.tags:
            continue
        j = k - 1
        while j >= 0 and flat[j].slp1 not in _RASHA and flat[j].slp1 not in _BLOCKERS:
            j -= 1
        if j >= 0 and flat[j].slp1 in _RASHA:
            out.append((k, v, k == len(flat) - 1))
    return out


def cond(state: State) -> bool:
    return state.tripadi_zone and any(fin for _k, _v, fin in _ns(state))


def act(state: State) -> State:
    for _k, v, fin in _ns(state):
        if fin:
            v.tags.add(TAG)
    return state


SUTRA = SutraRecord(
    sutra_id         = "8.4.37",
    sutra_type       = SutraType.PRATISHEDHA,
    text_slp1        = 'padAntasya',
    text_dev         = 'पदान्तस्य',
    samagra_slp1     = 'razAByAm padAntasya naH RaH na',
    samagra_dev      = 'रषाभ्याम् पदान्तस्य नः णः न',
    padaccheda_dev   = 'पद-अन्तस्य',
    why_dev          = 'पदान्तस्य नस्य णत्वं न।',
    anuvritti_from   = ("8.4.1",),
    blocks_sutra_ids = (),   # per-position bar by tag; a wholesale block of the target would stop its other sites
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
