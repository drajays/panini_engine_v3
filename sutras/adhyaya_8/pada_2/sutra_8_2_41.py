"""
8.2.41  षढोः कः सि  —  VIDHI (narrow demo)

Demo slice (जिघृक्षति):
  Replace final `D` with `k` when `s` follows: ...D + s... → ...k + s...
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State):
    for i in range(len(state.terms) - 1):
        t = state.terms[i]
        nxt = state.terms[i + 1]
        if "dhatu" not in t.tags and "anga" not in t.tags:
            continue
        if t.meta.get("8_2_41_shadhoh_done"):
            continue
        if not t.varnas or not nxt.varnas:
            continue
        if not any(v.slp1 == "s" for v in nxt.varnas):
            continue
        if t.varnas[-1].slp1 != "D":
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
    t.varnas[-1] = mk("k")
    t.meta["8_2_41_shadhoh_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.41",
    sutra_type=SutraType.VIDHI,
    text_slp1="zaDoh kaH si (narrow)",
    text_dev="षढोः कः सि",
    padaccheda_dev="षढोः / कः / सि",
    why_dev="सकारपरे ढकारस्य ककारादेशः (जिघृक्षति)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

