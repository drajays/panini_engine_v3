"""
8.3.24  नश्चापदान्तस्य झलि  —  VIDHI (narrow demo)

Demo slice (मुञ्चति.md):
  In a single pada, if `n` is not pada-final and is followed by a jhal
  consonant (here: c), it becomes anusvāra (M).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import JHAL


def _find(state: State):
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("8_3_24_nasch_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "n" and vs[i + 1].slp1 in JHAL:
            if i == len(vs) - 1:
                continue
            return i
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[0]
    t.varnas[i] = mk("M")
    t.meta["8_3_24_nasch_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.3.24",
    sutra_type=SutraType.VIDHI,
    text_slp1="naSca apadAntasya Jhali",
    text_dev="नश्चापदान्तस्य झलि",
    padaccheda_dev="नः च / अपदान्तस्य / झलि",
    why_dev="अपदान्त-नकारस्य झलि परे अनुस्वारः (डेमो: मुञ्चति)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

