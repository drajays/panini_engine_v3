"""
8.4.42  न पदान्ताट्टोरनाम्  —  VIDHI

Padaccheda: न · पदान्तात् · टोः · नाम्

न पदान्ताट्टोरनाम् (8.4.42)
Pāṭha: ashtadhyayi.com data.txt row i=84042 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_TT = frozenset({"w", "W", "q", "Q", "R"})            # ṭ-varga
_STU = frozenset({"s", "t", "T", "d", "D", "n"})       # स्तु: s and the ta-varga


def _site(state: State):
    """न पदान्ताट्टोरनाम् — a ṭ-varga letter at the end of the stem-pada (before the sup) does not draw the following s / ta-varga into ṣṭutva:
    विट्सु, मधुलिट्सु (not *विट्षु); the आम् of षण्णाम् is excepted (अनाम्)."""
    if not state.tripadi_zone or len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "prātipadika" not in t.tags:
        return None
    for k in range(len(t.varnas) - 1):
        a, b = t.varnas[k], t.varnas[k + 1]
        if a.slp1 in _TT and b.slp1 in _STU and "pratyaya_start_v" in b.tags:
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    state.blocked_sutras.add("8.4.41")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.42",
    sutra_type            = SutraType.PRATISHEDHA,
    text_slp1             = "na padAntAwworanAm",
    text_dev              = "न पदान्ताट्टोरनाम्",
    samagra_slp1          = "padAntAt woH anAm stoH zwuH na ",
    samagra_dev           = "पदान्तात् टोः अनाम् स्तोः ष्टुः न ।",
    padaccheda_dev        = "न · पदान्तात् · टोः · नाम्",
    why_dev               = "(सूत्रम् 8.4.42) न पदान्ताट्टोरनाम्।",
    anuvritti_from        = ('8.1.1',),
    blocks_sutra_ids      = ('8.4.41',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
