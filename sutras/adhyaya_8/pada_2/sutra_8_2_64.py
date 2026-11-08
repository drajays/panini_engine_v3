"""
8.2.64  मो नो धातोः  —  VIDHI

Padaccheda: मः नः धातोः

मो नो धातोः (8.2.64)
Pāṭha: ashtadhyayi.com data.txt row i=82064 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
 
from engine.tape_8_2 import dhatu_span, flat, followed_by_jhal_or_end, slp, substitute


def _site(state: State):
    """मो नो धातोः — the m that ends a dhātu, at the pada end or before a jhal (a pada-making sup: -bhyām, -su), becomes n: प्रशान्, प्रशान्भ्याम्."""
    if not state.tripadi_zone:
        return None
    c = flat(state)
    for k in range(len(c)):
        if slp(c[k]) != "m" or not followed_by_jhal_or_end(c, k):
            continue
        if k + 1 < len(c) and "origin:4.1.2" not in c[k + 1][0].varnas[c[k + 1][1]].tags:
            continue                # inside a pada (kṣam + sya): only a sup makes the stem a pada, 1.4.17
        span = dhatu_span(c, k)
        if span and span[1] == k:
            return c[k]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        t, i, _ = hit
        substitute(hit, "n")
        t.varnas[i].tags.add("padanta_v")      # the pada ends here (the sup makes the stem a pada, 1.4.17): 8.3.24 (apadāntasya) must not take this n
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.64",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "mo no DAtoH",
    text_dev              = "मो नो धातोः",
    samagra_slp1          = "maH DAtoH padasya naH",
    samagra_dev           = "मः धातोः पदस्य नः",
    padaccheda_dev        = "मः नः धातोः",
    why_dev               = "(सूत्रम् 8.2.64) मो नो धातोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
