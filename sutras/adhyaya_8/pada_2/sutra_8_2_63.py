"""
8.2.63  नशेर्वा  —  VIBHASHA

Padaccheda: नशेः वा

नशेर्वा (8.2.63)
Pāṭha: ashtadhyayi.com data.txt row i=82063 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
 
from engine.tape_8_2 import dhatu_span, flat, followed_by_jhal_or_end, slp, substitute

_STEM = "na"      # naś minus its final; naś (the ś may already stand as ṣ, ḍ or ṭ by 8.2.36 / 8.2.39, which are earlier: still naś, 1.1.56)


def _site(state: State):
    """नशेर्वा — the final of naś, before a jhal or at the pada end, becomes a ku letter, or not (then 8.2.36's ṣ stays): नक् / नग् / नट् / नड्."""
    if not state.tripadi_zone:
        return None
    c = flat(state)
    for k in range(len(c)):
        if slp(c[k]) not in ("S", "z", "q", "w") or not followed_by_jhal_or_end(c, k):
            continue
        span = dhatu_span(c, k)
        if span and span[1] == k and "".join(slp(x) for x in c[span[0]:k]) == _STEM:
            return c[k]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    hit = _site(state)
    if hit is not None:
        substitute(hit, "g" if slp(hit) == "q" else "k")       # sthāne 'ntaratama: voiced for voiced; 8.2.39 / 8.4.56 settle the rest
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.63",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = True,
    vibhasha_scope        = lambda state: _site(state) is not None,
    text_slp1             = "naServA",
    text_dev              = "नशेर्वा",
    samagra_slp1          = "naSeH padasya ante ku vA",
    samagra_dev           = "नशेः पदस्य अन्ते कु वा",
    padaccheda_dev        = "नशेः वा",
    why_dev               = "(सूत्रम् 8.2.63) नशेर्वा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
