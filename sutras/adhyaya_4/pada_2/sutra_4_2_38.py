"""
4.2.38  भिक्षादिभ्योऽण्  —  VIDHI

Padaccheda: भिक्षा-आदिभ्यः अण्

भिक्षाऽऽदिभ्योऽण् (4.2.38)
Pāṭha: ashtadhyayi.com data.txt row i=42038 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "samUha"), gana_of="4.2.38")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aR")


SUTRA = SutraRecord(
    sutra_id              = "4.2.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'BikzAdiByoR',
    text_dev              = 'भिक्षादिभ्योऽण्',
    samagra_slp1          = "tasya samUhaH iti BikzAdiByaH aR",
    samagra_dev           = "तस्य समूहः (इति) भिक्षादिभ्यः अण्",
    padaccheda_dev        = "भिक्षा-आदिभ्यः अण्",
    why_dev               = "(सूत्रम् 4.2.38) भिक्षाऽऽदिभ्योऽण्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.2.37',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
