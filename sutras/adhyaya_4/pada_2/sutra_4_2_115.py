"""
4.2.115  भवतष्ठक्छसौ  —  VIDHI

Padaccheda: भवतः ठक्-छसौ

भवतष्ठक्छसौ (4.2.115)
Pāṭha: ashtadhyayi.com data.txt row i=42115 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick

_UPA = ("Wak", "Cas")      # ṭhak and chas: the two pratyayas the sūtra gives side by side (s: pada, 1.4.16)


def _site(state: State):
    return taddhita_site(state, "Seza", stems=frozenset({"Bavat"}))      # the word the sūtra names, in the śeṣa sense (4.2.92); bhavat is vṛddha as a tyadādi (Kāśikā)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, _UPA[policy_pick(state, "4.2.115", len(_UPA))])


SUTRA = SutraRecord(
    sutra_id              = "4.2.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BavatazWakCasO",
    text_dev              = "भवतष्ठक्छसौ",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA BavataH Wak-CasO vfdDAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा भवतः ठक्-छसौ वृद्धात्",
    padaccheda_dev        = "भवतः ठक्-छसौ",
    why_dev               = "(सूत्रम् 4.2.115) भवतष्ठक्छसौ।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.2.114', '4.1.83'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
