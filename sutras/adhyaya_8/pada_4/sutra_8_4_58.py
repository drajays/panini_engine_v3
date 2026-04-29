"""
8.4.58  अनुस्वारस्य ययि परसवर्णः  —  VIDHI (narrow demo)

Demo slice (मुञ्चति.md):
  If anusvāra (M) is followed by a yayi consonant (here: c), replace M by the
  corresponding nasal of that consonant's varga (here: Y = ñ).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


_MAP = {
    "c": "Y", "C": "Y", "j": "Y", "J": "Y",  # c-varga → ñ
    "g": "G",  # velar varga → ङ (सङ्ग…)
}


def _find(state: State):
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("8_4_58_parasavarna_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "M":
            nxt = vs[i + 1].slp1
            if nxt in _MAP:
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
    nxt = t.varnas[i + 1].slp1
    t.varnas[i] = mk(_MAP[nxt])
    t.meta["8_4_58_parasavarna_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.58",
    sutra_type=SutraType.VIDHI,
    text_slp1="anusvArasya yayi parasavarNaH",
    text_dev="अनुस्वारस्य ययि परसवर्णः",
    padaccheda_dev="अनुस्वारस्य / ययि / परसवर्णः",
    why_dev="ययि परे अनुस्वारस्य परसवर्णः (डेमो: मुञ्चति)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

