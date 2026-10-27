"""
4.2.104  अव्ययात्त्यप्  —  VIDHI

Padaccheda: अव्ययात् त्यप्

अव्ययात्त्यप् (4.2.104)
Pāṭha: ashtadhyayi.com data.txt row i=42104 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita


def _site(state: State):
    return taddhita_site(state, "Seza", stems=frozenset({"amA","iha","kva","tatra","tatas"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "tyap")


SUTRA = SutraRecord(
    sutra_id              = "4.2.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avyayAttyap",
    text_dev              = "अव्ययात्त्यप्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA avyayAt tyap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा अव्ययात् त्यप्",
    padaccheda_dev        = "अव्ययात् त्यप्",
    why_dev               = "(सूत्रम् 4.2.104) अव्ययात्त्यप्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
