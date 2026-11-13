"""
8.2.53  क्षायो मः  —  VIDHI

Padaccheda: क्षायः मः

kṣai takes ma for the niṣṭhā's t: kṣā+ta → kṣāma.
Kāśikā 8.2.53: क्षैधातोरुत्तरस्य निष्ठातकारस्य मकारादेशो भवति। क्षामः। क्षामवान्॥
Pāṭha: ashtadhyayi.com data.txt row i=82053 (Art. 14).
The niṣṭhā-ta and its dhātu are read by sutras/adhyaya_8/pada_2/_nistha.py (loose tape or merged kṛdanta pada).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_2 import _nistha as N


def _sites(state: State):
    return [s for s in N.free(state) if s.root == "kzE"]


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    _sites(state)[0].put("m")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "kzAyo maH",
    text_dev              = "क्षायो मः",
    samagra_slp1          = "padasya pUrvatrAsidDam kzAyaH maH nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् क्षायः मः निष्ठातः नः",
    padaccheda_dev        = "क्षायः मः",
    why_dev               = "(सूत्रम् 8.2.53) क्षायो मः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
