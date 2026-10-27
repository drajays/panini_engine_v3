"""
4.2.16  संस्कृतं भक्षाः  —  VIDHI

Padaccheda: संस्कृतम् भक्षाः

संस्कृतं भक्षाः (4.2.16)
Pāṭha: ashtadhyayi.com data.txt row i=42016 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "saMskfta"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aR")


SUTRA = SutraRecord(
    sutra_id              = "4.2.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMskftaM BakzAH",
    text_dev              = "संस्कृतं भक्षाः",
    samagra_slp1          = "tatra saMskftaM BakzAH iti samarTAnAm praTamAt paraH tadDitaH pratyayaH aR vA",
    samagra_dev           = "'तत्र संस्कृतं भक्षाः' (इति) समर्थानाम् प्रथमात् परः तद्धितः प्रत्ययः अण् वा",
    padaccheda_dev        = "संस्कृतम् भक्षाः",
    why_dev               = "(सूत्रम् 4.2.16) संस्कृतं भक्षाः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
