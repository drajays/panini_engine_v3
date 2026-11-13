"""
8.2.52  पचो वः  —  VIDHI

Padaccheda: पचः वः

pac takes va for the niṣṭhā's t: pac+ta → pakva.
Kāśikā 8.2.52: पचेर्धातोरुत्तरस्य निष्ठातकारस्य वकारादेशो भवति। पक्वः। पक्ववान्॥
Pāṭha: ashtadhyayi.com data.txt row i=82052 (Art. 14).
The niṣṭhā-ta and its dhātu are read by sutras/adhyaya_8/pada_2/_nistha.py (loose tape or merged kṛdanta pada).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_2 import _nistha as N


def _sites(state: State):
    return [s for s in N.free(state) if s.root == "qupacaz"]


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    _sites(state)[0].put("v")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "paco vaH",
    text_dev              = "पचो वः",
    samagra_slp1          = "padasya pUrvatrAsidDam pacaH vaH nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् पचः वः निष्ठातः नः",
    padaccheda_dev        = "पचः वः",
    why_dev               = "(सूत्रम् 8.2.52) पचो वः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
