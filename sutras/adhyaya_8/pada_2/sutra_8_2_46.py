"""
8.2.46  क्षियो दीर्घात्  —  VIDHI

Padaccheda: क्षियः दीर्घात्

kṣi, lengthened (6.4.59-61), takes na: kṣīṇa. A short kṣi (akṣitam) does not.
Kāśikā 8.2.46: क्षियो धातोर्दीर्घादुत्तरस्य निष्ठातकारस्य नकारादेशो भवति। क्षीणाः क्लेशाः। क्षीणो जाल्मः। क्षीणस्तपस्वी।
Pāṭha: ashtadhyayi.com data.txt row i=82046 (Art. 14).
The niṣṭhā-ta and its dhātu are read by sutras/adhyaya_8/pada_2/_nistha.py (loose tape or merged kṛdanta pada).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_2 import _nistha as N


def _sites(state: State):
    return [s for s in N.free(state) if s.root in ("kzi", "kzI", "kzIz") and s.pre[-1].slp1 == "I"]


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    _sites(state)[0].put("n")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "kziyo dIrGAt",
    text_dev              = "क्षियो दीर्घात्",
    samagra_slp1          = "padasya pUrvatrAsidDam kziyaH dIrGAt nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् क्षियः दीर्घात् निष्ठातः नः",
    padaccheda_dev        = "क्षियः दीर्घात्",
    why_dev               = "(सूत्रम् 8.2.46) क्षियो दीर्घात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
