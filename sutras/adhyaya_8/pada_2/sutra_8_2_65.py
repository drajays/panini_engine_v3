"""
8.2.65  म्वोश्च  —  VIDHI

Padaccheda: म्-वोः च

म्वोश्च (8.2.65)
Pāṭha: ashtadhyayi.com data.txt row i=82065 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
 
from engine.tape_8_2 import dhatu_span, flat, slp, substitute


def _site(state: State):
    """म्वोश्च — the m that ends a dhātu, before m or v, becomes n: चक्षण्व (क्षम् + व)."""
    if not state.tripadi_zone:
        return None
    c = flat(state)
    for k in range(len(c) - 1):
        if slp(c[k]) != "m" or slp(c[k + 1]) not in ("m", "v"):
            continue
        span = dhatu_span(c, k)
        if span and span[1] == k:
            return c[k]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        substitute(hit, "n")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.65",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "mvoSca",
    text_dev              = "म्वोश्च",
    samagra_slp1          = "padasya pUrvatrAsidDam mvoH ca maH naH DAtoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् म्वोः च मः नः धातोः",
    padaccheda_dev        = "म्-वोः च",
    why_dev               = "(सूत्रम् 8.2.65) म्वोश्च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
