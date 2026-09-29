"""
7.3.75  ष्ठिवुक्लमुचमां शिति  —  VIDHI

ष्ठिव्, क्लम् and आङ्+चम् lengthen their vowel before a śit: ष्ठीवति, क्लामति, आचामति.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.nimitta_predicates import dhatu_before_sit
from engine.state import State
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _stem(t) -> str:
    return "".join(v.slp1 for v in t.varnas)

_LONG = {"a": "A", "i": "I"}


def _hit(state: State):
    i = dhatu_before_sit(state)
    if i is None:
        return None
    st = _stem(state.terms[i])
    if st in ("zWiv", "sWiv", "klam"):
        return i
    if st == "cam" and i and "".join(v.slp1 for v in state.terms[i - 1].varnas) == "A":
        return i
    return None


def cond(state: State) -> bool:
    return _hit(state) is not None


def act(state: State) -> State:
    t = state.terms[_hit(state)]
    j = max(k for k, v in enumerate(t.varnas) if v.slp1 in _LONG)
    t.varnas[j] = mk(_LONG[t.varnas[j].slp1])
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.75",
    sutra_type=SutraType.VIDHI,
    text_slp1='zWivuklamucamAM Siti',
    text_dev='ष्ठिवुक्लमुचमां शिति',
    padaccheda_dev="ष्ठिवु-क्लमि-आचमाम् शिति",
    why_dev="ष्ठिव्-क्लम्-आङ्पूर्वचम्-धातूनाम् अचः दीर्घः शिति परे (ष्ठीवति, क्लामति, आचामति)।",
    anuvritti_from=("7.3.73",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
