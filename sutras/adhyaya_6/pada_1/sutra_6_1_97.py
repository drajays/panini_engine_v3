"""
6.1.97  अतो गुणे  —  VIDHI

Operational role (v3.7, tyadādi pronouns like तद्):
  After 7.2.102 makes a final 'a', the aṅga may contain adjacent 'a' + 'a'
  at its tail (e.g. tad → t a a). This rule performs pararūpa-style
  ekādeśa by removing the first of the two identical 'a' sounds.

We implement narrowly:
  - only when aṅga is tagged `tyadadi`
  - find consecutive 'a''a' inside the aṅga and delete the earlier one
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find_pair(state: State):
    if not state.terms:
        return None
    anga = state.terms[0]
    if "anga" not in anga.tags or "tyadadi" not in anga.tags:
        return None
    if anga.meta.get("ato_gune_pararupa_done"):
        return None
    for i in range(len(anga.varnas) - 1):
        if anga.varnas[i].slp1 == "a" and anga.varnas[i + 1].slp1 == "a":
            return i
    return None


def cond(state: State) -> bool:
    return _find_pair(state) is not None


def act(state: State) -> State:
    i = _find_pair(state)
    if i is None:
        return state
    anga = state.terms[0]
    del anga.varnas[i]
    anga.meta["ato_gune_pararupa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.97",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ataH guRe",
    text_dev       = "अतो गुणे",
    padaccheda_dev = "अतः गुणे",
    why_dev        = "त्यदादि-शब्देषु अकार-द्वय-संयोगे पर-रूप-एकादेशः (त + अ + अ → त + अ)।",
    anuvritti_from = ("6.1.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

