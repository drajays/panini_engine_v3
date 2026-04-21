"""
1.1.27  सर्वादीनि सर्वनामानि  —  SAMJNA

Operational role (v3.5):
  - Tag an aṅga as `sarvanama` when its prātipadika upadeśa is in the
    sarvādi-gaṇa list (loaded from data/inputs/sarvadi_slp1.json).

Blindness:
  - cond() reads only Term.meta['upadesha_slp1'] and Term tags.
  - No paradigm coordinate access; no reference/gold access.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional, Set

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


_SARVADI: Optional[Set[str]] = None


def _load_sarvadi() -> Set[str]:
    global _SARVADI
    if _SARVADI is not None:
        return _SARVADI
    path = Path(__file__).parents[3] / "data" / "inputs" / "sarvadi_slp1.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    _SARVADI = set(data.get("sarvadi", []))
    return _SARVADI


def _eligible(state: State):
    sarvadi = _load_sarvadi()
    for t in state.terms:
        if "anga" not in t.tags:
            continue
        if "prātipadika" not in t.tags:
            continue
        if "sarvanama" in t.tags:
            continue
        upa = t.meta.get("upadesha_slp1")
        if not isinstance(upa, str):
            continue
        if upa in sarvadi:
            yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    # Registering the definition is useful for audit (R2 expects registry mutation
    # when the rule is applied).
    state.samjna_registry["sarvanama"] = frozenset(_load_sarvadi())
    for t in _eligible(state):
        t.tags.add("sarvanama")
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.27",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "sarvAdIni sarvanAmAni",
    text_dev       = "सर्वादीनि सर्वनामानि",
    padaccheda_dev = "सर्व-आदीनि सर्वनामानि",
    why_dev        = "सर्वादि-गण-पठित-शब्दाः सर्वनाम-संज्ञकाः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

