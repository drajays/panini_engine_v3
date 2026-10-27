"""
4.1.86  उत्सादिभ्योऽञ्  —  VIDHI

Padaccheda: उत्स-आदिभ्यः अञ्

उत्सादिभ्योऽञ् (4.1.86)
Pāṭha: ashtadhyayi.com data.txt row i=41086 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita  # noqa: F401


def _site(state: State):
    return taddhita_site(state, "apatya", gana_name="utsAdiH")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aY")


SUTRA = SutraRecord(
    sutra_id              = "4.1.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'utsAdiByoY',
    text_dev              = 'उत्सादिभ्योऽञ्',
    samagra_slp1          = "utsAdiByaH aY tadDitaH pratyayaH samarTAnAm praTamAt paraH vA",
    samagra_dev           = "उत्सादिभ्यः अञ् तद्धितः प्रत्ययः समर्थानाम् प्रथमात् परः वा",
    padaccheda_dev        = "उत्स-आदिभ्यः अञ्",
    why_dev               = "(सूत्रम् 4.1.86) उत्सादिभ्योऽञ्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83', '4.1.95'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
