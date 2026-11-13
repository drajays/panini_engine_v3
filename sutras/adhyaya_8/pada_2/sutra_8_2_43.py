"""
8.2.43  संयोगादेरातो धातोर्यण्वतः  —  VIDHI

Padaccheda: संयोग-आदेः आतः धातोः यण्-वतः

A saṃyogādi, ā-final dhātu with a yaṇ takes na for the niṣṭhā's t: mlā+ta → mlāna, dyā → dyāna, prā → prāṇa (8.4.1); snāta has no yaṇ, yāta no saṃyoga.
Kāśikā 8.2.43: संयोगादिर्यो धातुराकारान्तो यण्वान्, तस्मादुत्तरस्य निष्ठातकारस्य नकारादेशो भवति।
Pāṭha: ashtadhyayi.com data.txt row i=82043 (Art. 14).
The niṣṭhā-ta and its dhātu are read by sutras/adhyaya_8/pada_2/_nistha.py (loose tape or merged kṛdanta pada).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_2 import _nistha as N


def _sites(state: State):
    out = []
    for s in N.free(state):
        p = s.pre
        if len(p) >= 3 and p[-1].slp1 == "A" and N.is_hal(p[0]) and N.is_hal(p[1]) and any(v.slp1 in "yrlv" for v in p):
            out.append(s)
    return out


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    _sites(state)[0].put("n")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "saMyogAderAto DAtoryaRvataH",
    text_dev              = "संयोगादेरातो धातोर्यण्वतः",
    samagra_slp1          = "padasya pUrvatrAsidDam saMyogAdeH AtaH DAtoH yaRvataH nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् संयोगादेः आतः धातोः यण्वतः निष्ठातः नः",
    padaccheda_dev        = "संयोग-आदेः आतः धातोः यण्-वतः",
    why_dev               = "(सूत्रम् 8.2.43) संयोगादेरातो धातोर्यण्वतः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
