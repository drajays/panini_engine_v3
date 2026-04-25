"""
6.4.130  पादः पत्  —  VIDHI

Under *bhasya* (6.4.129), the sequence *pād* (पाद्) in a *bha*-marked *aṅga*
is replaced by *pad* (पद्) before a following affix — operational slice for
*supād* + *ṭā* → *supad* + *ṭā* (then *supadā*).

Engine: locate contiguous ``p`` + long ``A`` + ``d`` in the *aṅga* and
shorten ``A`` → ``a`` (same consonantal frame).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State
from phonology     import mk


def _find_pad_span(state: State):
    if len(state.terms) < 2:
        return None
    for ti in range(len(state.terms) - 1):
        anga = state.terms[ti]
        if "anga" not in anga.tags or "bha" not in anga.tags:
            continue
        if not adhikara_in_effect("6.4.130", state, "6.4.1"):
            continue
        if not adhikara_in_effect("6.4.130", state, "6.4.129"):
            continue
        vs = anga.varnas
        for j in range(len(vs) - 2):
            if vs[j].slp1 == "p" and vs[j + 1].slp1 == "A" and vs[j + 2].slp1 == "d":
                return (ti, j + 1)
    return None


def cond(state: State) -> bool:
    return _find_pad_span(state) is not None


def act(state: State) -> State:
    hit = _find_pad_span(state)
    if hit is None:
        return state
    ti, vi = hit
    state.terms[ti].varnas[vi] = mk("a")
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.130",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "pAdaH pat",
    text_dev       = "पादः पत्",
    padaccheda_dev = "पादः पत्",
    why_dev        = "भस्य अङ्गे पाद्-अंशस्य पद्-आदेशः (उदा. सुपाद् + टा)।",
    anuvritti_from = ("6.4.1", "6.4.129"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
