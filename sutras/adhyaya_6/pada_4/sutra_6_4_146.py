"""
6.4.146  ओर्गुणः  —  VIDHI

Under *bhasya*, *guṇa* of stem-final *o* (ओ) before a *y*-initial affix —
operational slice for *mādho* + *y* → *mādha* + *y* … (then **6.1.79** *vānto
yi*, etc., in fuller prakriyā).

Engine: if *bha* *aṅga* ends in ``o`` and the following pratyaya's first
phoneme is ``y``, replace final ``o`` with ``a`` (*guṇa* substitute anchor).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State
from phonology     import mk


def _find_o_before_y(state: State):
    if len(state.terms) < 2:
        return None
    for ti in range(len(state.terms) - 1):
        anga = state.terms[ti]
        pr = state.terms[ti + 1]
        if "anga" not in anga.tags or "bha" not in anga.tags:
            continue
        if not pr.varnas or not anga.varnas:
            continue
        if not adhikara_in_effect("6.4.146", state, "6.4.1"):
            continue
        if not adhikara_in_effect("6.4.146", state, "6.4.129"):
            continue
        if anga.varnas[-1].slp1 != "o":
            continue
        if pr.varnas[0].slp1 != "y":
            continue
        return (ti, len(anga.varnas) - 1)
    return None


def cond(state: State) -> bool:
    return _find_o_before_y(state) is not None or _find_u_before_a(state) is not None


def act(state: State) -> State:
    hit = _find_o_before_y(state)
    if hit is None:
        hit2 = _find_u_before_a(state)
        if hit2 is None:
            return state
        ti, vi = hit2
        state.terms[ti].varnas[vi] = mk("o")
        return state
    ti, vi = hit
    state.terms[ti].varnas[vi] = mk("a")
    return state


def _find_u_before_a(state: State):
    """
    v3 extension for taddhita glass-box spines (e.g. औपगव):
    under 6.4.1 + 6.4.129 (*bhasya*), if a *bha* aṅga ends in 'u' and the
    following pratyaya begins with 'a', apply guṇa: u → o.
    """
    if len(state.terms) < 2:
        return None
    for ti in range(len(state.terms) - 1):
        anga = state.terms[ti]
        pr = state.terms[ti + 1]
        if "anga" not in anga.tags or "bha" not in anga.tags:
            continue
        if not pr.varnas or not anga.varnas:
            continue
        if not adhikara_in_effect("6.4.146", state, "6.4.1"):
            continue
        if not adhikara_in_effect("6.4.146", state, "6.4.129"):
            continue
        if anga.varnas[-1].slp1 != "u":
            continue
        if pr.varnas[0].slp1 != "a":
            continue
        return (ti, len(anga.varnas) - 1)
    return None


SUTRA = SutraRecord(
    sutra_id       = "6.4.146",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "orguRaH",
    text_dev       = "ओर्गुणः",
    padaccheda_dev = "ओः गुणः",
    why_dev        = "भस्य अङ्गस्य अन्त्यस्य ओकारस्य यकारादौ परे गुण आदेशः।",
    anuvritti_from = ("6.4.1", "6.4.129"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
