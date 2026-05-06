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

META_PRE_TRIPADI_P003_A = "corrected_v2_P003_A_8_2_30_arm"


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
    if _find(state) is None:
        return False
    if state.meta.get(META_PRE_TRIPADI_P003_A):
        return True
    return bool(state.tripadi_zone)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, vi = hit
    t = state.terms[ti]
    t.varnas[vi] = mk("k")
    t.meta["8_2_30_cutuku_done"] = True
    state.meta.pop(META_PRE_TRIPADI_P003_A, None)
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.30",
    sutra_type=SutraType.VIDHI,
    text_slp1="coH kuH",
    text_dev="चोः कुः",
    padaccheda_dev="चोः कुः",
    why_dev="झलि/पदान्ते परे च-वर्णस्य क-वर्णादेशः (उक्त-उपपत्ति)। "
             "प००३-ए: त्रिपादी-प्रवेशात् पूर्वम् अनुमतम्।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

