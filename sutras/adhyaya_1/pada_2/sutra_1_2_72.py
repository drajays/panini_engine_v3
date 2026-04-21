"""
1.2.72  त्यदादिगणः  —  SAMJNA

Operational role (v3.7):
  - Tag a prātipadika aṅga as `tyadadi` when its upadeśa is in the
    tyadādi-gaṇa list (data/inputs/tyadadi_slp1.json).
  - Also tag it as `sarvanama` (these are pronouns in this scope).

This mirrors the v2 reference engine's preamble behaviour for `tad`.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional, Set

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


_TYADADI: Optional[Set[str]] = None


def _load_tyadadi() -> Set[str]:
    global _TYADADI
    if _TYADADI is not None:
        return _TYADADI
    path = Path(__file__).parents[3] / "data" / "inputs" / "tyadadi_slp1.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    _TYADADI = set(data.get("tyadadi", []))
    return _TYADADI


def _eligible(state: State):
    ty = _load_tyadadi()
    for t in state.terms:
        if "anga" not in t.tags or "prātipadika" not in t.tags:
            continue
        if "tyadadi" in t.tags:
            continue
        upa = t.meta.get("upadesha_slp1")
        if isinstance(upa, str) and upa in ty:
            yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    state.samjna_registry["tyadadi"] = frozenset(_load_tyadadi())
    for t in _eligible(state):
        t.tags.add("tyadadi")
        t.tags.add("sarvanama")
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.2.72",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "tyadAdi gaRaH",
    text_dev       = "त्यदादिगणः",
    padaccheda_dev = "त्यदादि-गणः",
    why_dev        = "त्यदादि-गण-पठित-शब्दाः ‘त्यदादि’ संज्ञकाः (तद्-प्रकारे)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

