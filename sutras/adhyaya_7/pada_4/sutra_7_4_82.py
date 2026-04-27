"""
7.4.82  गुणो यङ्लुकोः  —  VIDHI (narrow: abhyāsa guṇa for yaG)

Glass-box scope for `loluv`:
  Apply guṇa to the abhyāsa vowel U→o (lU → lo).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_82_abhyasa_guna_done"):
            continue
        for j, v in enumerate(t.varnas):
            if v.slp1 == "U":
                return (ti, j)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, j = hit
    state.terms[ti].varnas[j] = mk("o")
    state.terms[ti].meta["7_4_82_abhyasa_guna_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.4.82",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "guRo yaG-lukoH",
    text_dev       = "गुणो यङ्लुकोः",
    padaccheda_dev = "गुणः / यङ्-लुकोः",
    why_dev        = "यङ्-प्रसङ्गे अभ्यासस्य गुणः (लू→लो)।",
    anuvritti_from = ("7.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

