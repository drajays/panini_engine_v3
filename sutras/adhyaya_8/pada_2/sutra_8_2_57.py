"""
8.2.57  न ध्याख्यापॄमूर्छिमदाम्  —  PRATISHEDHA

Padaccheda: न ध्या-ख्या-पॄ-मूर्छि-मदाम्

dhyā, khyā, pṝ, mūrcchā, mad: the niṣṭhā's t does not become na (dhyāta, khyāta, pūrta, mūrta, matta). The act tags the t (8.2.42 / 8.2.43 / 8.2.44 pass over a tagged ta, like 8.4.44 over 8.4.40).
Kāśikā 8.2.57: ध्या ख्या पृृ मूर्च्छि मद इत्येतेषां निष्ठातकारस्य नकारादेशो न भवति। ध्यातः। ध्यातवान्। ख्यातः। ख्यातवान्। पूर्तः। पूर्तवान्। मूर्तः। मूर्तवान्। मत्तः। मत्तवान्।
Pāṭha: ashtadhyayi.com data.txt row i=82057 (Art. 14).
The niṣṭhā-ta and its dhātu are read by sutras/adhyaya_8/pada_2/_nistha.py (loose tape or merged kṛdanta pada).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_2 import _nistha as N

_ROOTS = frozenset({"DyE", "KyA", "pF", "mUrcCA", "mUrcCi", "madI", "mada"})      # dhyā, khyā, pṝ, mūrcchā, mad


def _sites(state: State):
    return [s for s in N.sites(state) if s.root in _ROOTS and N.BAR not in s.t.tags]


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    for s in _sites(state):
        s.t.tags.add(N.BAR)
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.57",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na DyAKyApFmUrCimadAm",
    text_dev              = "न ध्याख्यापॄमूर्छिमदाम्",
    samagra_slp1          = "padasya pUrvatrAsidDam na DyAKyApFmUrCimadAm nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् न ध्याख्यापॄमूर्छिमदाम् निष्ठातः नः",
    padaccheda_dev        = "न ध्या-ख्या-पॄ-मूर्छि-मदाम्",
    why_dev               = "(सूत्रम् 8.2.57) न ध्याख्यापॄमूर्छिमदाम्।",
    anuvritti_from        = ('8.1.1',),
    blocks_sutra_ids      = (),       # a per-ta bar by tag; a wholesale block would stop other sites
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
