"""
8.2.45  ओदितश्च  —  VIDHI

Padaccheda: ओत्-इतः च

An ōdit dhātu takes na for the niṣṭhā's t: ōlasj → lagna, ōvij → udvigna, ōpyāy → āpīna. SHORTCUT S165: the svādi ōdits (ṣūṅ, dūṅ, dīṅ …) are named by upadeśa from the Kāśikā list; the Dhātupāṭha data carries no o-marker for them.
Kāśikā 8.2.45: ओकारेतो धातोरुत्तरस्य निष्ठातकारस्य नकारादेशो भवति। ओलस्जी — लग्नः। लग्नवान्। ओविजी — उद्विग्नः। उद्विग्नवान्।
Pāṭha: ashtadhyayi.com data.txt row i=82045 (Art. 14).
The niṣṭhā-ta and its dhātu are read by sutras/adhyaya_8/pada_2/_nistha.py (loose tape or merged kṛdanta pada).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_2 import _nistha as N

_SVADI_ODIT = frozenset({"zUN", "dUN", "dIN", "qIN", "DIN", "mIN", "rIN", "lIN", "vrIN"})     # S165


def _sites(state: State):
    return [s for s in N.free(state) if s.up.startswith("o~") or s.root in _SVADI_ODIT]


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    _sites(state)[0].put("n")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "oditaSca",
    text_dev              = "ओदितश्च",
    samagra_slp1          = "padasya pUrvatrAsidDam oditaH ca nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् ओदितः च निष्ठातः नः",
    padaccheda_dev        = "ओत्-इतः च",
    why_dev               = "(सूत्रम् 8.2.45) ओदितश्च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
