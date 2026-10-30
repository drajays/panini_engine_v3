"""
6.1.76  पदान्ताद्वा  —  VIDHI

Padaccheda: पदान्तात् वा

पदान्ताद्वा (6.1.76)
Pāṭha: ashtadhyayi.com data.txt row i=61076 (Art. 14).
Kāśikā 6.1.76: kuṭīcchāyā, kuṭīchāyā; Laghukaumudī: lakṣmīcchāyā, lakṣmīchāyā — pūrveṇa nityaṃ prāptas tuk vā.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology import mk


def _live(state):
    return [i for i, t in enumerate(state.terms) if t.varnas]

_DIRGHA = frozenset("AIUFX")
META = "tuk_6_1_76"


def _find(state: State):
    live = _live(state)
    for i, j in zip(live, live[1:]):
        left, right = state.terms[i], state.terms[j]
        if "pada" not in left.tags or left.meta.get(META):
            continue
        if left.varnas[-1].slp1 in _DIRGHA and right.varnas[0].slp1 == "C":
            return i
    return None


def _new_cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    left = state.terms[i]
    left.varnas.append(mk("t"))        # tuk is kit (1.1.46): it stands after the dīrgha
    left.meta[META] = True
    state.meta["__why_now_dev__"] = "पदान्त-दीर्घात् परे छकारे तुक्-आगमः विकल्पेन (६.१.७६)।"
    return state

def cond(state: State) -> bool:
    return _new_cond(state)


SUTRA = SutraRecord(
    sutra_id              = "6.1.76",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "padAntAdvA",
    text_dev              = "पदान्ताद्वा",
    samagra_slp1          = "dIrGAt padAntAt saMhitAyAm Ce vA tugAgamaH",
    samagra_dev           = "दीर्घात् पदान्तात् संहितायाम् छे वा तुगागमः",
    padaccheda_dev        = "पदान्तात् वा",
    why_dev               = "काशिका ६.१.७६ — पदान्ताद् दीर्घात् परः छकारः चेत् तुगागमो वा (लक्ष्मीच्छाया, लक्ष्मीछाया); ६.१.७३ ह्रस्वस्य नित्यः, दीर्घस्य विकल्पः।",
    anuvritti_from        = ('6.1.1',),
    vibhasha_default=False,
    vibhasha_scope=_new_cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
