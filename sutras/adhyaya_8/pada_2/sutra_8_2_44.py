"""
8.2.44  ल्वादिभ्यः  —  VIDHI

Padaccheda: लू-आदिभ्यः

The lvādi dhātus (Dhātupāṭha 9.16 lūñ … 9.40 vrī) take na for the niṣṭhā's t: lūna, dhūna, jīna.
Kāśikā 8.2.44: तेभ्य उत्तरस्य निष्ठातकारस्य नकारादेशो भवति। लूनः। लूनवान्। धूनः। धूनवान्। जीनः। जीनवान्।
Pāṭha: ashtadhyayi.com data.txt row i=82044 (Art. 14).
The niṣṭhā-ta and its dhātu are read by sutras/adhyaya_8/pada_2/_nistha.py (loose tape or merged kṛdanta pada).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_2 import _nistha as N


def _sites(state: State):
    L = N.lvadi()
    return [s for s in N.free(state) if s.root in L]


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    _sites(state)[0].put("n")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "lvAdiByaH",
    text_dev              = "ल्वादिभ्यः",
    samagra_slp1          = "padasya pUrvatrAsidDam lvAdiByaH nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् ल्वादिभ्यः निष्ठातः नः",
    padaccheda_dev        = "लू-आदिभ्यः",
    why_dev               = "(सूत्रम् 8.2.44) ल्वादिभ्यः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
