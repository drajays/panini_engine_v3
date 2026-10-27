"""
4.2.88  नडशादाड्ड्वलच्  —  VIDHI

Padaccheda: नड-शादात् ड्वलच्

नडशादाड्ड्वलच् (4.2.88)
Pāṭha: ashtadhyayi.com data.txt row i=42088 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita


def _site(state: State):
    return taddhita_site(state, "cAturarTika", stems=frozenset({"naqa","SAda"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "qvalac")


SUTRA = SutraRecord(
    sutra_id              = "4.2.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "naqaSAdAqqvalac",
    text_dev              = "नडशादाड्ड्वलच्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA naqa-SAdAt qvalac",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा नड-शादात् ड्वलच्",
    padaccheda_dev        = "नड-शादात् ड्वलच्",
    why_dev               = "(सूत्रम् 4.2.88) नडशादाड्ड्वलच्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
