"""
8.2.21  अचि विभाषा  —  VIBHASHA

Padaccheda: अचि विभाषा

अचि विभाषा (8.2.21)
Pāṭha: ashtadhyayi.com data.txt row i=82021 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.tape_8_2 import AC, dhatu_span, flat, slp, substitute

_STEM = "gir"      # gṝ (निगरणे) after 7.1.100 ir: girati / gilati


def _site(state: State):
    """अचि विभाषा — the r of gṝ before a vowel becomes l, or not: गिरति / गिलति."""
    if not state.tripadi_zone:
        return None
    c = flat(state)
    for k in range(len(c) - 1):
        if slp(c[k]) != "r" or slp(c[k + 1]) not in AC:
            continue
        span = dhatu_span(c, k)
        if span and span[1] == k and "".join(slp(x) for x in c[span[0]:k + 1]) == _STEM:
            return c[k]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    hit = _site(state)
    if hit is not None:
        substitute(hit, "l")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.21",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = True,
    vibhasha_scope        = lambda state: _site(state) is not None,
    text_slp1             = "aci viBAzA",
    text_dev              = "अचि विभाषा",
    samagra_slp1          = "padasya pUrvatrAsidDam aci viBAzA raH laH graH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् अचि विभाषा रः लः ग्रः",
    padaccheda_dev        = "अचि विभाषा",
    why_dev               = "(सूत्रम् 8.2.21) अचि विभाषा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
