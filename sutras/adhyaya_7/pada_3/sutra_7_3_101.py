"""
7.3.101  अतो दीर्घो यञि  —  VIDHI

Padaccheda: अतः दीर्घः यञि

"Of a (short a), before a yañ consonant (y v r l ñ ṅ ṇ n m),
the ā (dīrgha) substitutes."

In the tiṅanta prakriyā: after vikaraṇa IT-lopa the aṅga/vikaraṇa ends
with short `a` and the tiṅ ādeśa begins with a yañ consonant (m in `mi`,
v in `vas`, m in `mas`).  This rule lengthens that `a` → `Ā`, producing
the correct uttama-puruṣa sandhi: bhav+A+mi = bhavāmi, bhav+A+vas →
bhavāvaḥ, bhav+A+mas → bhavāmaḥ.

Engine arm: ``state.meta["7_3_101_arm"] is True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology     import mk

# yañ pratyāhāra: semivowels + nasals (SLP1 single-char representations)
_YAJ: frozenset[str] = frozenset({
    "y",  # य
    "v",  # व
    "r",  # र
    "l",  # ल
    "Y",  # ञ
    "N",  # ण
    "n",  # न
    "m",  # म
})


def _find(state: State) -> int | None:
    """Return index i such that terms[i] ends with 'a' and terms[i+1] starts with yañ."""
    for i in range(len(state.terms) - 1):
        t1 = state.terms[i]
        t2 = state.terms[i + 1]
        if not t1.varnas or not t2.varnas:
            continue
        if t1.varnas[-1].slp1 != "a":
            continue
        if t2.varnas[0].slp1 not in _YAJ:
            continue
        if "pratyaya" not in t2.tags:
            continue
        if t1.meta.get("7_3_101_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("7_3_101_arm"):
        return False
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].varnas[-1] = mk("A")
    state.terms[i].meta["7_3_101_done"] = True
    state.samjna_registry["7_3_101_dirgha"] = (
        state.samjna_registry.get("7_3_101_dirgha", 0) + 1
    )
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.101",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "ato dIrGo yaYi",
    text_dev              = "अतो दीर्घो यञि",
    padaccheda_dev        = "अतः दीर्घः यञि",
    why_dev               = (
        "अङ्ग/विकरण-अन्तस्य ह्रस्व-अकारस्य, यञ्-आदि-प्रत्यय-परे, दीर्घादेशः; "
        "उत्तम-पुरुष-तिङन्ते: भव+अ+मि → भव+आ+मि → भवामि।"
    ),
    anuvritti_from        = ("7.1.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
