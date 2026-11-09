"""
8.3.111  सात्पदाद्योः  —  PRATISHEDHA

Padaccheda: सात्-पद-आद्योः
No ṣatva (8.3.59) for the s of the pratyaya sāt (अग्निसात्) or for a pada-initial s (दधि सिञ्चति).
The pada-initial ādeśa s here is the s that 6.1.64 धात्वादेः षः सः puts in place of a dhātu's initial ṣ (स्नाति, स्नौति, सुवति):
The s is an ādeśa, so 8.3.59 would reach it (the reason the sūtra is needed).
The act tags that s; 8.3.59 passes over a tagged s.
SHORTCUT S147: the sāt half needs 5.4.52 (a gate-only stub today); only the dhātu-initial ādeśa s is covered.
Pāṭha: ashtadhyayi.com data.txt row i=83111 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

TAG = "satva_barred_8_3_111"


def _sites(state: State):
    out = []
    for t in state.terms:
        if t.varnas:
            v = t.varnas[0]
            if v.slp1 == "s" and "origin:6.1.64" in v.tags and TAG not in v.tags:
                out.append(v)
    return out


def cond(state: State) -> bool:
    return state.tripadi_zone and bool(_sites(state))


def act(state: State) -> State:
    for v in _sites(state):
        v.tags.add(TAG)
    return state


SUTRA = SutraRecord(
    sutra_id         = "8.3.111",
    sutra_type       = SutraType.PRATISHEDHA,
    text_slp1        = "sAtpadAdyoH",
    text_dev         = "सात्पदाद्योः",
    samagra_slp1     = "saH iRkoH apadAntasya mUrDanyaH na sAtpadAdyoH",
    samagra_dev      = "सः इण्कोः अपदान्तस्य मूर्धन्यः न सात्पदाद्योः",
    padaccheda_dev   = "सात्-पद-आद्योः",
    why_dev          = "सात्-प्रत्ययस्य पदादेश्च सस्य षत्वं न (स्नाति)।",
    anuvritti_from   = ("8.3.110",),
    blocks_sutra_ids = (),     # per-site bar by tag; a wholesale block of 8.3.59 would stop its other sites
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
