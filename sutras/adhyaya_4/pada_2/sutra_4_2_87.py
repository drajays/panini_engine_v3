"""
4.2.87  कुमुदनडवेतसेभ्यो ड्मतुप्  —  VIDHI

Padaccheda: कुमुद-नड-वेतसेभ्यः ड्‍मतुप्

कुमुदनडवेतसेभ्यो ड्मतुप् (4.2.87)
Pāṭha: ashtadhyayi.com data.txt row i=42087 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita

_STEMS = frozenset({"kumuda", "naqa", "vetasa"})      # the three words the sūtra itself names


def cond(state: State) -> bool:
    return taddhita_site(state, "cAturarTika", stems=_STEMS) is not None      # the sense frame 4.2.67 opened (tad asmin asti iti deśe tannāmni)


def act(state: State) -> State:
    if cond(state):
        attach_taddhita(state, "qmatu~p")        # ḍ: it (1.3.7); u~: it (1.3.2); ḍit: ṭi-lopa 6.4.143; the m of matup: v by 8.2.10 jhayaḥ
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kumudanaqavetaseByo qmatup",
    text_dev              = "कुमुदनडवेतसेभ्यो ड्मतुप्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA kumuda-naqa-vetaseByaH qmatup",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा कुमुद-नड-वेतसेभ्यः ड्मतुप्",
    padaccheda_dev        = "कुमुद-नड-वेतसेभ्यः ड्‍मतुप्",
    why_dev               = "(सूत्रम् 4.2.87) कुमुदनडवेतसेभ्यो ड्मतुप्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.1.83',),      # the special over the default aṇ of the cāturarthika frame
    also_vidhi            = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
