"""
3.1.133  ण्वुल्तृचौ  —  VIDHI

Operational role (v3.8, kṛdanta scaffolding):
  - Attach the kṛt-pratyaya **ṇvul** (Nvul) to a dhātu to form an agent noun
    (kartṛ sense), e.g. pac + Nvul.

Architecture notes:
  - The pipeline (not cond) supplies the requested kṛt upadeśa as
    state.meta['krt_upadesha_slp1'].
  - This rule only *attaches* the pratyaya Term; subsequent 1.3.x it rules
    will mark and delete its it markers.

Blindness:
  - cond() reads only tags and allowlisted meta ('krt_upadesha_slp1'), not
    paradigm coordinates.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk


_KRIT: Optional[Dict[str, Any]] = None


def _load_krit() -> Dict[str, Any]:
    global _KRIT
    if _KRIT is not None:
        return _KRIT
    path = Path(__file__).parents[3] / "data" / "inputs" / "krit_pratyaya.json"
    with path.open(encoding="utf-8") as f:
        _KRIT = json.load(f)
    return _KRIT


def _first_dhatu_term(state: State):
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def _matches(state: State) -> bool:
    if not state.terms:
        return False
    dhatu = _first_dhatu_term(state)
    if dhatu is None:
        return False
    # Don't attach if a kṛt pratyaya already present.
    if any(t.kind == "pratyaya" and "krt" in t.tags for t in state.terms):
        return False
    upa = state.meta.get("krt_upadesha_slp1")
    if upa not in _load_krit():
        return False
    if upa in ("Nvul", "lyuw", "tfc"):
        return True
    return False


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    upa = state.meta.get("krt_upadesha_slp1")
    if upa == "Nvul":
        # Nvul (upadeśa): ण् + व् + उ + ल् — SLP1 ``R`` = ण् (see ``HAL_DEV``).
        varnas = [mk("R"), mk("v"), mk("u"), mk("l")]
        tags = {"pratyaya", "krt", "upadesha", "has_initial_n_it"}
        pr = Term(kind="pratyaya", varnas=varnas, tags=tags, meta={"upadesha_slp1": upa})
        state.terms.append(pr)
        return state
    if upa == "lyuw":
        varnas = [mk("l"), mk("y"), mk("u"), mk("w")]
        tags = {"pratyaya", "krt", "upadesha"}
        pr = Term(kind="pratyaya", varnas=varnas, tags=tags, meta={"upadesha_slp1": upa})
        state.terms.append(pr)
        return state
    if upa == "tfc":
        # तृच् — SLP1 ``t`` + ``f`` (ऋ) + ``c`` (इत्, हलन्त्यम्).
        varnas = [mk("t"), mk("f"), mk("c")]
        tags = {"pratyaya", "krt", "upadesha"}
        pr = Term(kind="pratyaya", varnas=varnas, tags=tags, meta={"upadesha_slp1": upa})
        state.terms.append(pr)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.133",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Nvul-tfcau (kartari)",
    text_dev       = "ण्वुल्तृचौ",
    padaccheda_dev = "ण्वुल् तृचौ",
    why_dev        = "कर्तरि अर्थे धातोः ण्वुल्-प्रत्ययः (पाचक इत्यादि)।",
    anuvritti_from = ("3.1.91",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

