"""
8.2.76  र्वोरुपधाया दीर्घ इकः  —  VIDHI

Padaccheda: ऋ-वोः उपधाया दीर्घ इकः

र्वोरुपधाया दीर्घ इकः (8.2.76)
Pāṭha: ashtadhyayi.com data.txt row i=82076 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import dhatu_aṅga
from phonology import mk

_ZERO_KRT = frozenset({"origin_pratyaya:kvip", "origin_pratyaya:kvin"})     # lopa'd: the dhātu is the last thing in the pada
_SHORT_TO_LONG = {"i": "I", "u": "U", "f": "F", "x": "X"}


def _site(state: State):
    """A pada whose last sound is r or v and whose base is a dhātu (kṛdanta): its upadhā, if a short ik, is the sthānin (गीः, धूः, पूः, आशीः)."""
    if not state.tripadi_zone:
        return None
    for t in state.terms:
        if "pada" not in t.tags or len(t.varnas) < 2 or not dhatu_aṅga(t):
            continue
        if any(g.startswith("origin_pratyaya:") and g not in _ZERO_KRT for g in t.tags):
            continue                    # dhātoḥ: the r / v is the dhātu's own — a sounded krt (tṛc: bhavituḥ) is a pratyaya's
        if "ru_intermediate" in t.varnas[-1].tags:
            continue                    # a ru from a sup's s (DugBiH) is no dhātu's r; ponytail: a dhātu's own s→ru (pipaWIH) needs the s's origin kept through the merge
        if t.varnas[-1].slp1 not in ("r", "v") or t.varnas[-2].slp1 not in _SHORT_TO_LONG:
            continue
        return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        old = t.varnas[-2]
        t.varnas[-2] = mk(_SHORT_TO_LONG[old.slp1], *old.tags)
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.76",
    sutra_type            = SutraType.VIDHI,
        text_slp1             = "rvorupaDAyA dIrGa ikaH",
    text_dev              = "र्वोरुपधाया दीर्घ इकः",
    samagra_slp1          = "padasya rvoH DAtoH upaDAyAH ikaH dIrGaH",
    samagra_dev           = "पदस्य र्वोः धातोः उपधायाः इकः दीर्घः",
    padaccheda_dev        = "ऋ-वोः उपधाया दीर्घ इकः",
    why_dev               = "(सूत्रम् 8.2.76) र्वोरुपधाया दीर्घ इकः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
