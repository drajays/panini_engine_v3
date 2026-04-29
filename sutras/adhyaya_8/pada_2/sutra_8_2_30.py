"""
8.2.30  चोः कुः  —  VIDHI

Operational role (v3.6, demo slice for `1145.md`):
  If a dhātu ends in 'c' (cu-varṇa) and the following sound begins with a
  jhal (e.g. 't'), replace that final 'c' with 'k' (ku-varṇa).

Example:
  u c + t  → u k + t
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import JHAL


def _find(state: State):
    # 1) Intra-term: ... c + JHAL ...
    for ti, t in enumerate(state.terms):
        if t.meta.get("8_2_30_cutuku_done"):
            continue
        vs = t.varnas
        for vi in range(len(vs) - 1):
            if vs[vi].slp1 == "c" and vs[vi + 1].slp1 in JHAL:
                return (ti, vi)
    # 2) Cross-term boundary: X ends with c, next begins with JHAL.
    for i in range(len(state.terms) - 1):
        left = state.terms[i]
        right = state.terms[i + 1]
        if left.meta.get("8_2_30_cutuku_done"):
            continue
        if not left.varnas or left.varnas[-1].slp1 != "c":
            continue
        if not right.varnas or right.varnas[0].slp1 not in JHAL:
            continue
        return (i, len(left.varnas) - 1)
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, vi = hit
    t = state.terms[ti]
    t.varnas[vi] = mk("k")
    t.meta["8_2_30_cutuku_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.30",
    sutra_type=SutraType.VIDHI,
    text_slp1="coH kuH",
    text_dev="चोः कुः",
    padaccheda_dev="चोः कुः",
    why_dev="झलि/पदान्ते परे च-वर्णस्य क-वर्णादेशः (उक्त-उपपत्ति)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

