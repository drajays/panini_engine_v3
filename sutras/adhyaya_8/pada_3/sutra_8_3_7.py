"""
8.3.7  नश्छव्यप्रशान्  —  VIDHI (narrow: *m* → anusvāra before *c*)

Teaching **P014** step **19** (with **8.4.58** *parasavarṇa*): on the merged
*pada*, dental **m** immediately before **c** becomes **M** (anusvāra), feeding
**8.4.58** *ya*yi *parasavarṇa* (here **Y** = ञ्).

Engine:
  • ``state.meta['corrected_v2_P014_8_3_7_arm']`` (cleared in ``act``)
  • **Tripāḍī**: ``state.tripadi_zone`` must be True (**8.2.1**).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State) -> int | None:
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("8_3_7_m_to_M_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "m" and vs[i + 1].slp1 == "c":
            return i
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    if not state.meta.get("corrected_v2_P014_8_3_7_arm"):
        return False
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[0]
    t.varnas[i] = mk("M")
    t.meta["8_3_7_m_to_M_done"] = True
    state.meta.pop("corrected_v2_P014_8_3_7_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="8.3.7",
    sutra_type=SutraType.VIDHI,
    text_slp1="naS chavy aprASAn",
    text_dev="नश्छव्यप्रशान्",
    padaccheda_dev="नः / छवि / अप्रशान्",
    why_dev="छवि परे नकारस्य अनुस्वारः (P014: म्→ं पूर्वं ययि-परसवर्णे)।",
    anuvritti_from=("8.3.6",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
