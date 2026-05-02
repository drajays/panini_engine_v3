"""
7.3.50  ठस्येकः  —  VIDHI (narrow: Tak → ika)

The JSON ``split_prakriyas_11/P018.json`` uses **7.3.50** to realise the surface
for the taddhita **ठक्** as **इक** (ika).

Engine (narrow):
  - If a following taddhita pratyaya has ``upadesha_slp1 == 'Tak'``, replace that
    pratyaya tape with ``ika`` and update ``upadesha_slp1`` to ``ika`` while
    preserving ``upadesha_slp1_original``.

This is intentionally narrow and does not attempt to cover the full *śāstra*
inventory beyond the demo need.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya" or "taddhita" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "Tak":
            continue
        if t.meta.get("7_3_50_Tak_to_ika_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    pr = state.terms[i]
    pr.varnas = list(parse_slp1_upadesha_sequence("ika"))
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "Tak")
    pr.meta["upadesha_slp1"] = "ika"
    pr.meta["7_3_50_Tak_to_ika_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.50",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Thasya ekaH (Tak→ika) (narrow)",
    text_dev       = "ठस्येकः (ठक्→इक) — संक्षेपः",
    padaccheda_dev = "ठस्य / एकः",
    why_dev        = "ठक्-प्रत्ययस्य ‘इक’ आदेशः (P018 narrow demo).",
    anuvritti_from = ("7.3.45",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

