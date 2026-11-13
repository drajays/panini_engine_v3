"""
8.2.42  रदाभ्यां निष्ठातो नः पूर्वस्य च दः  —  VIDHI

Padaccheda: रदाभ्याम् / निष्ठातः / नः / पूर्वस्य / च / दः

After a dhātu-final r or d the niṣṭhā's t becomes n, and the d before it becomes n too: bhid+ta → bhinna, kṝ+ta → kīrṇa (8.4.1), svid+ta → svinna.
Kāśikā 8.2.42: रेफदकाराभ्यामुत्तरस्य निष्ठातकारस्य नकार आदेशो भवति, पूर्वस्य च दकारस्य रेफात् तावत् — आस्तीर्णम्। विस्तीर्णम्। विशीर्णम्। निगीर्णम्। अवगूर्णम्। दकारात् — भिन्नः। भिन्नवान्। छिन्नः। छिन्नवान्।
Pāṭha: ashtadhyayi.com data.txt row i=82042 (Art. 14).
The niṣṭhā-ta and its dhātu are read by sutras/adhyaya_8/pada_2/_nistha.py (loose tape or merged kṛdanta pada).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_2 import _nistha as N


def _sites(state: State):
    return [s for s in N.free(state) if s.pre and s.pre[-1].slp1 in ("r", "d")]


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    s = _sites(state)[0]
    if s.pre[-1].slp1 == "d":
        N.swap(s.pre[-1], "n")          # pūrvasya ca daḥ
    s.put("n")
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.42",
    sutra_type=SutraType.VIDHI,
    text_slp1='radAByAM nizWAto naH pUrvasya ca daH',
    text_dev='रदाभ्यां निष्ठातो नः पूर्वस्य च दः',
    samagra_slp1="padasya pUrvatrAsidDam radAByAm nizWAtaH naH pUrvasya ca daH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="पदस्य पूर्वत्रासिद्धम् रदाभ्याम् निष्ठातः नः पूर्वस्य च दः",
    padaccheda_dev="रदाभ्याम् / निष्ठातः / नः / पूर्वस्य / च / दः",
    why_dev="भिद् / स्विद् + निष्ठा-तकारः → भिन्न / स्विन्न (P001-A/C आर्म्)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
