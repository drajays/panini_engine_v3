"""
8.2.51  शुषः कः  —  VIDHI

Padaccheda: शुषः कः

śuṣ takes ka for the niṣṭhā's t: śuṣ+ta → śuṣka.
Kāśikā 8.2.51: शुषेर्धातोरुत्तरस्य निष्ठातकारस्य ककारादेशो भवति। शुष्कः। शुष्कवान्॥
Pāṭha: ashtadhyayi.com data.txt row i=82051 (Art. 14).
The niṣṭhā-ta and its dhātu are read by sutras/adhyaya_8/pada_2/_nistha.py (loose tape or merged kṛdanta pada).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_2 import _nistha as N


def _sites(state: State):
    return [s for s in N.free(state) if s.root == "Suza"]


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    _sites(state)[0].put("k")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "SuzaH kaH",
    text_dev              = "शुषः कः",
    samagra_slp1          = "padasya pUrvatrAsidDam SuzaH kaH nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् शुषः कः निष्ठातः नः",
    padaccheda_dev        = "शुषः कः",
    why_dev               = "(सूत्रम् 8.2.51) शुषः कः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
