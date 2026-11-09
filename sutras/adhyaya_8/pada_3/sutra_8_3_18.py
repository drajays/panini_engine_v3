"""
8.3.18  व्योर्लघुप्रयत्नतरः शाकटायनस्य  —  VIBHASHA

After bho / bhago / agho or an a-varṇa, a pada-final y or v before an aś may be the lighter-spoken (laghuprayatnatara) one, on Śākaṭāyana's view:
भोयत्र / भो अत्र. The act tags the varṇa; 8.3.20 leaves a tagged y alone.
Works on two padas side by side on one tape (the left pada ends where its Term ends); a lone word has no seam, so nothing fires.
Pāṭha: ashtadhyayi.com data.txt row i=83018 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_8.pada_3._yatva import seams, pada_stem, AVARNA, BHOBHAGOAGHO, HAS, LAGHU

from phonology import mk

def _site(state: State):
    for t, u in seams(state):
        c = t.varnas[-1]
        if c.slp1 not in ("y", "v") or LAGHU in c.tags or len(t.varnas) < 2:
            continue
        prev = t.varnas[-2].slp1
        if prev in AVARNA or (c.slp1 == "y" and prev == "o" and pada_stem(t)[:-1] in ("B", "Bag", "aG")):
            return c
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).tags.add(LAGHU)
    return state

SUTRA = SutraRecord(
    sutra_id         = "8.3.18",
    sutra_type       = SutraType.VIBHASHA,
    vibhasha_default = False,
    vibhasha_scope   = lambda state: _site(state) is not None,
    text_slp1        = 'vyorlaGuprayatnataraH SAkawAyanasya',
    text_dev         = 'व्योर्लघुप्रयत्नतरः शाकटायनस्य',
    samagra_slp1     = 'BoBagoaGoapUrvasya aSi vyoH laGuprayatnataraH SAkawAyanasya',
    samagra_dev      = 'भोभगोअघोअपूर्वस्य अशि व्योः लघुप्रयत्नतरः शाकटायनस्य',
    padaccheda_dev   = 'व्योः लघुप्रयत्नतरः शाकटायनस्य',
    why_dev          = 'पदान्तयोर्वयोः शाकटायनमते लघुप्रयत्नतरादेशः।',
    anuvritti_from   = ('8.3.17',),
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
