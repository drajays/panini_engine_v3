"""
8.3.58  नुम्विसर्जनीयशर्व्यवायेऽपि  —  VIDHI

Padaccheda: नुम्-विसर्जनीय-शर्-व्यवाये अपि
Ṣatva (8.3.57 iṇkoḥ, 8.3.59) goes on even when ONE anusvāra (from num), one visarga or one śar stands between the
iṇ/ku and the s: धनूंषि, सर्पींषि, सर्पिःषु, सर्पिष्षु. Each interveners alone, never two together (निंस्से: no ṣatva — Kāśikā 8.3.58,
Bālamanoramā "प्रत्येकमेव").
The act tags that intervening varṇa; 8.3.59's look-back passes only over a tagged one.
Pāṭha: ashtadhyayi.com data.txt row i=83058 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_3.sutra_8_3_59 import _IN_KUK_PREV, VYAVAYA_TAG, eligible_s

_INTERVENERS = frozenset({"M", "H", "S", "z", "s"})        # anusvāra (num), visarjanīya, śar


def _sites(state: State):
    if not state.tripadi_zone or not state.terms:
        return []
    t = state.terms[0]
    out = []
    for i in range(2, len(t.varnas)):
        mid = t.varnas[i - 1]
        if (eligible_s(t, i) and mid.slp1 in _INTERVENERS and VYAVAYA_TAG not in mid.tags
                and t.varnas[i - 2].slp1 in _IN_KUK_PREV):
            out.append(mid)
    return out


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    for v in _sites(state):
        v.tags.add(VYAVAYA_TAG)
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.58",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "numvisarjanIyaSarvyavAye 'pi",
    text_dev              = "नुम्विसर्जनीयशर्व्यवायेऽपि",
    samagra_slp1          = "saH iRkoH apadAntasya mUrDanyaH numvisarjanIyaSarvyavAye api",
    samagra_dev           = "सः इण्कोः अपदान्तस्य मूर्धन्यः नुम्विसर्जनीयशर्व्यवायेऽपि",
    padaccheda_dev        = "नुम्-विसर्जनीय-शर्-व्यवाये अपि",
    why_dev               = "नुम्, विसर्जनीय वा शर् मध्ये एकः स्थितोऽपि इण्कु-परस्य सस्य षत्वम् (धनूंषि, सर्पिःषु)।",
    anuvritti_from        = ('8.3.56',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
