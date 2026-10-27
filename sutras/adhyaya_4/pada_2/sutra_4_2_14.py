"""
4.2.14  तत्रोद्धृतममत्रेभ्यः  —  VIDHI

Padaccheda: तत्र उद्धृतम् अमत्रेभ्यः

तत्रोद्धृतममत्रेभ्यः (4.2.14)
Pāṭha: ashtadhyayi.com data.txt row i=42014 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "udDfta"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aR")


SUTRA = SutraRecord(
    sutra_id              = "4.2.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tatrodDftamamatreByaH",
    text_dev              = "तत्रोद्धृतममत्रेभ्यः",
    samagra_slp1          = "tatra udDftamamatreByaH iti samarTAnAm praTamAt paraH aR pratyayaH",
    samagra_dev           = "'तत्र उद्धृतममत्रेभ्यः' (इति) समर्थानाम् प्रथमात् परः अण् प्रत्ययः",
    padaccheda_dev        = "तत्र उद्धृतम् अमत्रेभ्यः",
    why_dev               = "(सूत्रम् 4.2.14) तत्रोद्धृतममत्रेभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
