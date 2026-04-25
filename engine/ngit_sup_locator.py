"""
engine/ngit_sup_locator.py — locate the *aṅga* Term that bears **7.3.113** / **7.3.114**
when a *stri* **wAp** (or other non-*sup*) Term sits between stem and **ṅit** *sup*.

``cond`` must not assume ``state.terms[-2]`` is always the *aṅga* (Constitution
Art. 2 still holds: no *vibhakti* reads).
"""
from __future__ import annotations

from typing import Optional, Tuple

from engine.state import State
from phonology.sarvanama_syat_7_3_114 import ngit_sup_match


def indices_last_anga_before_ngit_sup(state: State) -> Optional[Tuple[int, int]]:
    """
    Return ``(anga_idx, sup_idx)`` for the rightmost **ṅit** *sup* pratyaya and
    the nearest preceding **prakṛti** *aṅga* Term, or ``None``.
    """
    for j in range(len(state.terms) - 1, -1, -1):
        pr = state.terms[j]
        if pr.kind != "pratyaya" or "sup" not in pr.tags:
            continue
        if not ngit_sup_match(pr.meta.get("upadesha_slp1")):
            continue
        for i in range(j - 1, -1, -1):
            ang = state.terms[i]
            if ang.kind == "prakriti" and "anga" in ang.tags:
                return i, j
    return None
