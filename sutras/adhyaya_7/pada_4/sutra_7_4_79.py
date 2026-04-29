"""
7.4.79  सन्यतः  —  VIDHI (narrow demo)

Demo slice (जिघृक्षति):
  In the abhyāsa, replace `a` with `i` when a sanādi (here `is`) follows.

Engine:
  - recipe arms via ``state.meta['7_4_79_sanyatah_abhyasa_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _sanadi_present(state: State) -> bool:
    return any("sanadi" in t.tags for t in state.terms)


def _find(state: State):
    if not state.meta.get("7_4_79_sanyatah_abhyasa_arm"):
        return None
    if not _sanadi_present(state):
        return None
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_79_done"):
            continue
        for j, v in enumerate(t.varnas):
            if v.slp1 == "a":
                return ti, j
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, j = hit
    t = state.terms[ti]
    t.varnas[j] = mk("i")
    t.meta["7_4_79_done"] = True
    state.meta["7_4_79_sanyatah_abhyasa_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.79",
    sutra_type=SutraType.VIDHI,
    text_slp1="sanyataH (narrow)",
    text_dev="सन्यतः",
    padaccheda_dev="सन्यतः",
    why_dev="सन्-प्रत्यये परे अभ्यासस्य अकारः इकारः (जि-)।",
    anuvritti_from=("7.4.60",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

