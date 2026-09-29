"""
7.3.74  शमामष्टानां दीर्घः श्यनि  —  VIDHI

The eight roots शम्, तम्, दम्, श्रम्, भ्रम्, क्षम्, क्लम्, मद् (divādi) lengthen
their vowel before श्यन्: शाम्यति, श्राम्यति, माद्यति.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.nimitta_predicates import dhatu_before_sit
from engine.state import State
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _stem(t) -> str:
    return "".join(v.slp1 for v in t.varnas)

_SAMADI = frozenset({"Sam", "tam", "dam", "Sram", "Bram", "kzam", "klam", "mad"})
_LONG = {"a": "A", "i": "I", "u": "U", "f": "F"}


def _hit(state: State):
    i = dhatu_before_sit(state)
    if i is None or state.terms[i].meta.get("gana") != 4:
        return None
    if (state.terms[i + 1].meta.get("upadesha_slp1") or "") != "Syan":
        return None
    return i if _stem(state.terms[i]) in _SAMADI else None


def cond(state: State) -> bool:
    return _hit(state) is not None


def act(state: State) -> State:
    t = state.terms[_hit(state)]
    j = max(k for k, v in enumerate(t.varnas) if v.slp1 in _LONG)
    t.varnas[j] = mk(_LONG[t.varnas[j].slp1])
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.74",
    sutra_type=SutraType.VIDHI,
    text_slp1="SamAmazwAnAM dIrGaH Syani",
    text_dev="शमामष्टानां दीर्घः श्यनि",
    padaccheda_dev="शमाम् अष्टानाम् दीर्घः श्यनि",
    why_dev="शमादीनाम् अष्टानां धातूनाम् अचः दीर्घः श्यनि परे (शाम्यति, भ्राम्यति, माद्यति)।",
    anuvritti_from=("7.3.73",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
