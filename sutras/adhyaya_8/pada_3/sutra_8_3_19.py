"""
8.3.19  लोपः शाकल्यस्य  —  VIBHASHA

A pada-final y or v after an a-varṇa is dropped before an aś, on Śākalya's view (optional): क आस्ते / कयास्ते, असा आदित्यः / असावादित्यः.
Works on two padas side by side on one tape (the left pada ends where its Term ends); a lone word has no seam, so nothing fires.
Pāṭha: ashtadhyayi.com data.txt row i=83019 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_8.pada_3._yatva import seams, pada_stem, AVARNA, BHOBHAGOAGHO, HAS, LAGHU

from phonology import mk

def _site(state: State):
    for t, u in seams(state):
        c = t.varnas[-1]
        if c.slp1 in ("y", "v") and len(t.varnas) > 1 and t.varnas[-2].slp1 in AVARNA and "8_3_19_done" not in c.tags:
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    t.varnas.pop()
    if t.varnas:
        t.varnas[-1].tags.add("8_3_19_done")
    return state

SUTRA = SutraRecord(
    sutra_id         = "8.3.19",
    sutra_type       = SutraType.VIBHASHA,
    vibhasha_default = False,
    vibhasha_scope   = lambda state: _site(state) is not None,
    text_slp1        = 'lopaH SAkalyasya',
    text_dev         = 'लोपः शाकल्यस्य',
    samagra_slp1     = 'BoBagoaGoapUrvasya aSi vyoH lopaH SAkalyasya',
    samagra_dev      = 'भोभगोअघोअपूर्वस्य अशि व्योः लोपः शाकल्यस्य',
    padaccheda_dev   = 'लोपः शाकल्यस्य',
    why_dev          = 'अवर्णपूर्वयोः पदान्तयोः वयोः शाकल्यमते वा लोपः।',
    anuvritti_from   = ('8.3.18',),
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
