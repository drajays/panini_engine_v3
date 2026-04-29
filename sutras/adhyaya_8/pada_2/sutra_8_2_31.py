"""
8.2.31  हो ढः  —  VIDHI (narrow demo)

Demo slice (जिघृक्षति):
  In the grah-desiderative base, replace final `h` with `D` before following `s`
  (of san term).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State):
    # Look for [dhatu-like term ending in h] + [pratyaya containing s].
    for i in range(len(state.terms) - 1):
        t = state.terms[i]
        nxt = state.terms[i + 1]
        if "dhatu" not in t.tags and "anga" not in t.tags:
            continue
        if t.meta.get("8_2_31_ho_dha_done"):
            continue
        if not t.varnas:
            continue
        if t.varnas[-1].slp1 != "h":
            continue
        if not nxt.varnas or not any(v.slp1 == "s" for v in nxt.varnas):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas[-1] = mk("D")
    t.meta["8_2_31_ho_dha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.31",
    sutra_type=SutraType.VIDHI,
    text_slp1="ho QaH (narrow)",
    text_dev="हो ढः",
    padaccheda_dev="हो / ढः",
    why_dev="सकारपरे हकारस्य ढकारादेशः (जिघृक्षति)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

