"""
8.4.54  अभ्यासे चर्च  —  VIDHI (narrow demo)

Demo slice (विभिदतुः):
  In the abhyāsa, replace a jhaś consonant with its jaś counterpart.
  Here: भि- → बि- (B → b).

Engine:
  - applies only to the first varṇa of an `abhyasa` term (after 7.4.60 trim).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


_JHAS_TO_JAS = {
    "B": "b",  # bh -> b (narrow demo)
}


def _find(state: State):
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("8_4_54_carc_done"):
            continue
        if not t.varnas:
            continue
        ch = t.varnas[0].slp1
        rep = _JHAS_TO_JAS.get(ch)
        if rep is None:
            continue
        return ti, rep
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, rep = hit
    state.terms[ti].varnas[0] = mk(rep)
    state.terms[ti].meta["8_4_54_carc_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.54",
    sutra_type=SutraType.VIDHI,
    text_slp1="aByAse carc",
    text_dev="अभ्यासे चर्च",
    padaccheda_dev="अभ्यासे / चर्च",
    why_dev="अभ्यास-स्थिते झश्-वर्णस्य जश्-आदेशः (भि→बि) — विभिदतुः।",
    anuvritti_from=("8.4.53",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

