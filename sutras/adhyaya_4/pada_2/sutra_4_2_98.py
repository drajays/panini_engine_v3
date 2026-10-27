"""
4.2.98  दक्षिणापश्चात्पुरसस्त्यक्  —  VIDHI

Padaccheda: दक्षिणा-पश्चात्-पुरसः त्यक्

दक्षिणापश्चात्पुरसस्त्यक् (4.2.98)
Pāṭha: ashtadhyayi.com data.txt row i=42098 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita


def _site(state: State):
    return taddhita_site(state, "Seza", stems=frozenset({"dakziRA","paScAt","puras"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "tyak")


SUTRA = SutraRecord(
    sutra_id              = "4.2.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dakziRApaScAtpurasastyak",
    text_dev              = "दक्षिणापश्चात्पुरसस्त्यक्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA dakziRA-paScAt-purasaH tyak",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा दक्षिणा-पश्चात्-पुरसः त्यक्",
    padaccheda_dev        = "दक्षिणा-पश्चात्-पुरसः त्यक्",
    why_dev               = "(सूत्रम् 4.2.98) दक्षिणापश्चात्पुरसस्त्यक्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
