"""
8.2.56  नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्  —  VIBHASHA

Padaccheda: नुद-विद-उन्द-त्रा-घ्रा-ह्रीभ्यः अन्यतरस्याम्

nud, vid, und, trā, ghrā, hrī: na for the niṣṭhā's t is optional (nunna / nutta, vinna / vitta, trāṇa / trāta, hrīṇa / hrīta); the nitya 8.2.42 / 8.2.43 leave these dhātus to this vibhāṣā (_nistha.VIBHASHA_ROOTS). The default reading keeps the t; explore() gives the na. SHORTCUT S166: every vid (all four of them) is read, the Kāśikā means vid vicāraṇe and the verse extends it to the others.
Kāśikā 8.2.56: नुद विद उन्द त्रा घ्रा ह्री इत्येतेभ्य उत्तरस्य निष्ठातकारस्य नकार आदेशो भवत्यन्यतरस्याम्। नुद — नुन्नः, नुत्तः। विद — विन्नः, वित्तः।
Pāṭha: ashtadhyayi.com data.txt row i=82056 (Art. 14).
The niṣṭhā-ta and its dhātu are read by sutras/adhyaya_8/pada_2/_nistha.py (loose tape or merged kṛdanta pada).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_2 import _nistha as N


def _sites(state: State):
    return [s for s in N.sites(state) if s.root in N.VIBHASHA_ROOTS]


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    s = _sites(state)[0]
    if s.pre[-1].slp1 == "d":
        N.swap(s.pre[-1], "n")          # pūrvasya ca daḥ, by anuvṛtti from 8.2.42: nud+ta → nunna, vid+ta → vinna
    s.put("n")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.56",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = False,
    text_slp1             = 'nudavidondatrAGrAhrIByonyatarasyAm',
    text_dev              = 'नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्',
    samagra_slp1          = "padasya pUrvatrAsidDam nudavidondatrAGrAhrIByaH anyatarasyAm nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् नुदविदोन्दत्राघ्राह्रीभ्यः अन्यतरस्याम् निष्ठातः नः",
    padaccheda_dev        = "नुद-विद-उन्द-त्रा-घ्रा-ह्रीभ्यः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 8.2.56) नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्।",
    anuvritti_from        = ('8.1.1',),
    vibhasha_default      = False,     # the t stays by default; explore() gives the na
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
