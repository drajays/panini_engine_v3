"""
8.3.22  हलि सर्वेषाम्  —  VIDHI

A pada-final y after bho / bhago / agho or an a-varṇa is dropped before a hal (here: a haś), on every teacher's view, the laghuprayatnatara y too:
भो जनाः, भगो देवाः, देवा गच्छन्ति. It overrides 8.3.19 / 8.3.20 before a haś.
Works on two padas side by side on one tape (the left pada ends where its Term ends); a lone word has no seam, so nothing fires.
Pāṭha: ashtadhyayi.com data.txt row i=83022 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_8.pada_3._yatva import seams, pada_stem, AVARNA, BHOBHAGOAGHO, HAS, LAGHU

from phonology import mk

def _site(state: State):
    for t, u in seams(state):
        c = t.varnas[-1]
        if c.slp1 == "y" and u.varnas[0].slp1 in HAS and len(t.varnas) > 1 and (t.varnas[-2].slp1 in AVARNA or pada_stem(t) in BHOBHAGOAGHO):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas.pop()
    return state

SUTRA = SutraRecord(
    sutra_id         = "8.3.22",
    sutra_type       = SutraType.VIDHI,
    text_slp1        = 'hali sarveRAm',
    text_dev         = 'हलि सर्वेषाम्',
    samagra_slp1     = 'BoBagoaGoapUrvasya aSi vyoH lopaH hali sarveRAm',
    samagra_dev      = 'भोभगोअघोअपूर्वस्य अशि व्योः लोपः हलि सर्वेषाम्',
    padaccheda_dev   = 'हलि सर्वेषाम्',
    why_dev          = 'भो-भगो-अघो-अवर्णात् परस्य पदान्तयकारस्य हलि सर्वेषां लोपः।',
    anuvritti_from   = ('8.3.19',),
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
