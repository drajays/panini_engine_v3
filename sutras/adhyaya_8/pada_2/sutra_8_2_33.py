"""
8.2.33  वा द्रुहमुहष्णुहष्णिहाम्  —  VIDHI

Padaccheda: वा द्रुह-मुह-ष्णुह-ष्णिहाम्

वा द्रुहमुहष्णुहष्णिहाम् (8.2.33)
Pāṭha: ashtadhyayi.com data.txt row i=82033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.tape_8_2 import dhatu_span, flat, followed_by_jhal_or_end, slp, substitute

_ROOTS = {"druh", "muh", "snuh", "snih"}      # द्रुह्, मुह्, ष्णुह्, ष्णिह् (the ष्-initial ones stand as snuh / snih on the tape)


def _site(state: State):
    """वा द्रुहमुहष्णुहष्णिहाम् — the h of these four dhātus before a jhal or at the pada end becomes gh, or not (then 8.2.31 gives ḍh): ध्रुक् / ध्रुट्."""
    if not state.tripadi_zone:
        return None
    c = flat(state)
    for k in range(len(c)):
        if slp(c[k]) != "h" or not followed_by_jhal_or_end(c, k):
            continue
        span = dhatu_span(c, k)
        if span and span[1] == k and "".join(slp(x) for x in c[span[0]:span[1] + 1]) in _ROOTS:
            return c[k]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        substitute(hit, "G")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.33",
    sutra_type            = SutraType.VIBHASHA,
    apavada_of            = ("8.2.31",),      # the vā: gh, or (declined) the general ho ḍhaḥ
    vibhasha_default      = True,
    vibhasha_scope        = lambda state: _site(state) is not None,
    text_slp1             = "vA druhamuhazRuhazRihAm",
    text_dev              = "वा द्रुहमुहष्णुहष्णिहाम्",
    samagra_slp1          = "druha-muha-zRuha-zRihAm DAtoH haH padasya ante Jali GaH vA",
    samagra_dev           = "द्रुह-मुह-ष्णुह-ष्णिहाम् धातोः हः पदस्य अन्ते झलि घः वा",
    padaccheda_dev        = "वा द्रुह-मुह-ष्णुह-ष्णिहाम्",
    why_dev               = "(सूत्रम् 8.2.33) वा द्रुहमुहष्णुहष्णिहाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
