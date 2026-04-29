"""
8.4.55  खरि च  —  VIDHI (narrow)

Demo slice (भिनत्ति .md):
  Before a following *khar* (here: `t` of `ti`), a preceding `d` (jhal) becomes `t`
  (car/char substitution).

Engine:
  - Tripāḍī zone only.
  - Looks for the sequence `d` followed by a varṇa in KHAR, within the final pada.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import KHAR


def _find(state: State):
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("8_4_55_khari_ca_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "d" and vs[i + 1].slp1 in KHAR:
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
    t.varnas[i] = mk("t")
    t.meta["8_4_55_khari_ca_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.55",
    sutra_type=SutraType.VIDHI,
    text_slp1="Kari ca",
    text_dev="खरि च",
    padaccheda_dev="खरि च",
    why_dev="खर्-वर्णे परे झल्-वर्णस्य चर्त्वम् (डेमो: द् → त्)।",
    anuvritti_from=("8.4.53",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

