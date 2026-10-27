"""
4.1.84  अश्वपत्यादिभ्यश्च  —  VIDHI

Padaccheda: अश्वपति-आदिभ्यः च

अश्वपत्यादिभ्यश्च (4.1.84)
Pāṭha: ashtadhyayi.com data.txt row i=41084 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita  # noqa: F401


def _site(state: State):
    return taddhita_site(state, gana_name="aSvapatyAdiH")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aR")


SUTRA = SutraRecord(
    sutra_id              = "4.1.84",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aSvapatyAdiByaSca",
    text_dev              = "अश्वपत्यादिभ्यश्च",
    samagra_slp1          = "aSvapatyAdiByaH ca prAgdIvyataH aR tadDitaH pratyayaH samarTAnAm praTamAt paraH vA",
    samagra_dev           = "अश्वपत्यादिभ्यः च प्राग्दीव्यतः अण् तद्धितः प्रत्ययः समर्थानाम् प्रथमात् परः वा",
    padaccheda_dev        = "अश्वपति-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.1.84) अश्वपत्यादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.85', '4.1.83'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
