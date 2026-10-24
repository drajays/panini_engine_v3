"""
3.1.98  पोरदुपधात्  —  VIDHI

Padaccheda: पोः अत्-उपधात्

Krt suffix rule from dhatu: पोरदुपधात् (98)
Pāṭha: ashtadhyayi.com data.txt row i=31098 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem



def cond(state: State) -> bool:
    """Pavargānta, a-upadha dhātu → yat, the apavāda of ṇyat (3.1.124): śapyam, labhyam."""
    if not kftya_open(state, "3.1.98"):
        return False
    st = kftya_stem(state)
    return len(st) >= 2 and st[-1] in "pPbBm" and st[-2] == "a"


def act(state: State) -> State:
    return kftya_attach(state, "3.1.98", "yat")


SUTRA = SutraRecord(
    sutra_id              = "3.1.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "poradupaDAt",
    text_dev              = "पोरदुपधात्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH poH adupaDAt kft yat",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः पोः अदुपधात् कृत् यत्",
    padaccheda_dev        = "पोः अत्-उपधात्",
    why_dev               = "धातोः [पोरदुपधात्]-प्रत्ययः विहितः (३.१.98)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.124',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
