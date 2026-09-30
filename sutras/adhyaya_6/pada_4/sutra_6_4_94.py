"""
6.4.94  खचि ह्रस्वः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=64094
- Kāśikā: "परंतपः" (तापि + खच् → तप् via hrasva of the ṇic ā)
- Cross-validation: tests/unit/test_bhattikavya_1_1.py (परंतपः)

Before a *khit* affix (खच्), a long vowel of the aṅga is shortened.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_GATE_KEY: str = "6_4_94_Kaci_94"
_DIRGHA = {"A": "a", "I": "i", "U": "u", "F": "f", "X": "x"}


def _khit_after(state: State, i: int) -> bool:
    for t in state.terms[i + 1:]:
        if t.kind != "pratyaya":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        marks = t.meta.get("it_markers") or set()
        return up == "Kac" or t.meta.get("khit") is True or "K" in marks
    return False


def _site(state: State):
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags and "anga" not in t.tags:
            continue
        if t.meta.get("6_4_94_hrasva_done"):
            continue
        if not _khit_after(state, i):
            continue
        for vi, v in enumerate(t.varnas):
            if v.slp1 in _DIRGHA:
                return i, vi, _DIRGHA[v.slp1]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    hit = _site(state)
    if hit is None:
        return state
    i, vi, short = hit
    t = state.terms[i]
    t.varnas[vi] = mk(short)
    t.meta["6_4_94_hrasva_done"] = True
    state.paribhasha_gates[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.94",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "Kaci hrasvaH",
    text_dev              = "खचि ह्रस्वः",
    padaccheda_dev        = "खचि ह्रस्वः",
    why_dev               = "खिद्-प्रत्यये परे अङ्गस्य दीर्घ उपधा ह्रस्वः (ताप् → तप्)।",
    anuvritti_from        = ('6.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
