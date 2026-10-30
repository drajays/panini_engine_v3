"""
6.1.128  ऋत्यकः  —  VIDHI

Padaccheda: ऋति अकः

ऋत्यकः (6.1.128)
Pāṭha: ashtadhyayi.com data.txt row i=61128 (Art. 14).
Kāśikā 6.1.128: khaṭva ṛśyaḥ, māla ṛśyaḥ, kumāri ṛśyaḥ, hotṛ ṛśyaḥ; Laghukaumudī: brahma ṛṣiḥ, brahmarṣiḥ.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology import mk


def _live(state):
    return [i for i, t in enumerate(state.terms) if t.varnas]

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG

_HRASVA = {"a": "a", "A": "a", "i": "i", "I": "i", "u": "u", "U": "u", "f": "f", "F": "f", "x": "x", "X": "x"}
_RI = frozenset("fFxX")      # ṛ with its savarṇas (no taparaṇa)
META = "prakritibhava_6_1_128"


def _find(state: State):
    live = _live(state)
    for i, j in zip(live, live[1:]):
        left, right = state.terms[i], state.terms[j]
        if "pada" not in left.tags or left.meta.get(META) or PRAGHYA_TERM_TAG in left.tags:
            continue
        if left.varnas[-1].slp1 in _HRASVA and right.varnas[0].slp1 in _RI:    # savarṇa too: hotṛ ṛśyaḥ
            return i
    return None


def _new_cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    left = state.terms[i]
    left.varnas[-1] = mk(_HRASVA[left.varnas[-1].slp1])
    left.tags.add(PRAGHYA_TERM_TAG)
    left.meta[META] = True
    state.meta["__why_now_dev__"] = "पदान्तस्य अकः ऋति परे शाकल्यमतेन ह्रस्वः प्रकृतिभावश्च (६.१.१२८)।"
    return state

def cond(state: State) -> bool:
    return _new_cond(state)


SUTRA = SutraRecord(
    sutra_id              = "6.1.128",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "ftyakaH",
    text_dev              = "ऋत्यकः",
    samagra_slp1          = "padAntasya akaH asavarRe fti hrasvaH prakftyA SAkalyasya",
    samagra_dev           = "पदान्तस्य  अकः असवर्णे ऋति ह्रस्वः  प्रकृत्या शाकल्यस्य",
    padaccheda_dev        = "ऋति अकः",
    why_dev               = "काशिका ६.१.१२८ — पदान्तस्य अकः ऋकारे परे शाकल्यमतेन प्रकृतिभावः ह्रस्वश्च (खट्व ऋश्यः, ब्रह्म ऋषिः); पक्षे गुणः।",
    anuvritti_from        = ('6.1.1',),
    vibhasha_default=False,
    vibhasha_scope=_new_cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
