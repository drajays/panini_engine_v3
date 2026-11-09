"""
8.3.17  भोभगोअघोअपूर्वस्य योऽशि  —  VIDHI

The ru-r (from 8.2.66) at the end of bho / bhago / agho, or after an a-varṇa, becomes y before an aś: भो अत्र, भो जनाः, देवा गच्छन्ति (the y is dropped later
by 8.3.19 / 8.3.20 / 8.3.22).
Works on two padas side by side on one tape (the left pada ends where its Term ends); a lone word has no seam, so nothing fires.
Pāṭha: ashtadhyayi.com data.txt row i=83017 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_8.pada_3._yatva import seams, pada_stem, AVARNA, BHOBHAGOAGHO, HAS, LAGHU

from phonology import mk

def _site(state: State):
    for t, u in seams(state):
        r = t.varnas[-1]
        if r.slp1 == "r" and "ru_intermediate" in r.tags and (pada_stem(t) in BHOBHAGOAGHO or (len(t.varnas) > 1 and t.varnas[-2].slp1 in AVARNA)):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    old = t.varnas[-1]
    t.varnas[-1] = mk("y", *old.tags)
    return state

SUTRA = SutraRecord(
    sutra_id         = "8.3.17",
    sutra_type       = SutraType.VIDHI,
    text_slp1        = 'BoBagoaGoapUrvasya yoSi',
    text_dev         = 'भोभगोअघोअपूर्वस्य योऽशि',
    samagra_slp1     = 'BoBagoaGoapUrvasya roH yaH aSi',
    samagra_dev      = 'भोभगोअघोअपूर्वस्य रोः यः अशि',
    padaccheda_dev   = 'भो-भगो-अघो-अपूर्वस्य यः अशि',
    why_dev          = 'भो-भगो-अघो-अवर्णात् परस्य रुँ-रेफस्य अशि परे यकारः।',
    anuvritti_from   = ('8.3.16',),
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
