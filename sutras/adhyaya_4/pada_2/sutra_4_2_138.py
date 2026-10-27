"""
4.2.138  गहादिभ्यश्च  —  VIDHI

Padaccheda: गह-आदिभ्यः च

गहादिभ्यश्च (4.2.138)
Pāṭha: ashtadhyayi.com data.txt row i=42138 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita


def _site(state: State):
    return taddhita_site(state, "Seza", gana_of="4.2.138")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "Ca")


SUTRA = SutraRecord(
    sutra_id              = "4.2.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gahAdiByaSca",
    text_dev              = "गहादिभ्यश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA gaha-AdiByaH ca CaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा गह-आदिभ्यः च छः",
    padaccheda_dev        = "गह-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.2.138) गहादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
