"""
8.4.59  वा पदान्तस्य  —  VIBHASHA

Optional parasavarṇa of a pada-final anusvāra.

Traditional discussion connects this to the *savarṇa* notion (1.1.9): the
anusvāra may optionally be replaced by the nasal consonant homorganic with
the following consonant (परसवर्णः).

Engine (representative, glass-box):
  - After pada-merge (single `pada` term), when a varṇa 'M' (anusvāra) is
    immediately followed by a consonant, optionally replace 'M' with the
    appropriate nasal:

    before {k,K,g,G} → N   (ङ्)
    before {c,C,j,J} → Y   (ञ्)
    before {w,W,q,Q} → R   (ण्)
    before {t,T,d,D} → n   (न्)
    before {p,P,b,B} → m   (म्)

This is intentionally narrow and does not attempt full padānta + yay-only
scoping; pipelines schedule it only where needed.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


_PARASAVARNA = {
    "k": "N", "K": "N", "g": "N", "G": "N",
    "c": "Y", "C": "Y", "j": "Y", "J": "Y",
    "w": "R", "W": "R", "q": "R", "Q": "R",
    "t": "n", "T": "n", "d": "n", "D": "n",
    "p": "m", "P": "m", "b": "m", "B": "m",
    # semivowels (pragmatic homorganic choices)
    "y": "Y",
    "v": "m",
    "r": "n",
    "l": "n",
}


def _find(state: State):
    if not state.terms:
        return None
    t = state.terms[-1]
    if "pada" not in t.tags:
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 != "M":
            continue
        if "parasavarna_done" in vs[i].tags:
            continue
        nxt = vs[i + 1].slp1
        rep = _PARASAVARNA.get(nxt)
        if rep is None:
            continue
        return (len(state.terms) - 1, i, rep)
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, vi, rep = hit
    new_v = mk(rep)
    new_v.tags.add("parasavarna_done")
    state.terms[ti].varnas[vi] = new_v
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.4.59",
    sutra_type     = SutraType.VIBHASHA,
    text_slp1      = "vA padAntasya",
    text_dev       = "वा पदान्तस्य",
    padaccheda_dev = "वा / पदान्तस्य",
    why_dev        = "पदान्ते विद्यमानस्य अनुस्वारस्य परे वर्णे परसवर्णः विकल्पेन।",
    anuvritti_from = ("8.4.58",),
    vibhasha_default = True,
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

