"""
3.1.125  ओरावश्यके  —  VIDHI

Padaccheda: ओः आवश्यके

Krt suffix rule from dhatu: ओरावश्यके (125)
Pāṭha: ashtadhyayi.com data.txt row i=31125 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem
from engine.vivaksha import vivaksita
from phonology import mk

def cond(state: State) -> bool:
    """u-final dhātu → ṇyat when the thing must be done (lAvyam, pAvyam); apavāda of yat."""
    return kftya_open(state, "3.1.125") and vivaksita(state, "artha", "AvaSyaka") and kftya_stem(state)[-1:] in ("u", "U")


def act(state: State) -> State:
    return kftya_attach(state, "3.1.125", "Ryat")


SUTRA = SutraRecord(
    sutra_id              = "3.1.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "orAvaSyake",
    text_dev              = "ओरावश्यके",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH oH AvaSyake kft Ryat",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः ओः आवश्यके कृत् ण्यत्",
    padaccheda_dev        = "ओः आवश्यके",
    why_dev               = "धातोः [ओरावश्यके]-प्रत्ययः विहितः (३.१.125)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.97',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
