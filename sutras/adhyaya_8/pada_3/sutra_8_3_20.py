"""
8.3.20  ओतो गार्ग्यस्य  —  VIDHI

After o a pada-final y is dropped before an aś, on Gārgya's view (always): भो अत्र, भगो अत्र. A laghuprayatnatara y (8.3.18) stays: भोयत्र.
Works on two padas side by side on one tape (the left pada ends where its Term ends); a lone word has no seam, so nothing fires.
Pāṭha: ashtadhyayi.com data.txt row i=83020 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_8.pada_3._yatva import seams, pada_stem, AVARNA, BHOBHAGOAGHO, HAS, LAGHU

from phonology import mk

def _site(state: State):
    for t, u in seams(state):
        c = t.varnas[-1]
        if c.slp1 == "y" and LAGHU not in c.tags and len(t.varnas) > 1 and t.varnas[-2].slp1 == "o" and u.varnas[0].slp1 not in HAS:   # before a haś 8.3.22 (apavāda) takes the y
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas.pop()
    return state

SUTRA = SutraRecord(
    sutra_id         = "8.3.20",
    sutra_type       = SutraType.VIDHI,
    text_slp1        = 'oto gArgyasya',
    text_dev         = 'ओतो गार्ग्यस्य',
    samagra_slp1     = 'BoBagoaGoapUrvasya aSi vyoH lopaH oto gArgyasya',
    samagra_dev      = 'भोभगोअघोअपूर्वस्य अशि व्योः लोपः ओतः गार्ग्यस्य',
    padaccheda_dev   = 'ओतः गार्ग्यस्य',
    why_dev          = 'ओकारात् परस्य पदान्तयकारस्य गार्ग्यमते नित्यं लोपः।',
    anuvritti_from   = ('8.3.19',),
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
