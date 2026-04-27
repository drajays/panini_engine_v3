"""
7.3.82  मिदेर्गुणः  —  VIDHI (narrow: mid → med before Syan(y))

Glass-box scope for `medyati`:
  For the dhātu `mid` (after it-lopa from `YimidA~`), before the divādi
  vikaraṇa `Syan` (after it-lopa ⇒ `y`), apply guṇa to the i-vowel (i→e).

This is implemented as an explicit apavāda that can fire even if a generic
guṇa gate would be blocked by k/ṅ-it conditions.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    if len(state.terms) < 2:
        return None
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return None
    if dh.meta.get("7_3_82_mide_guna_done"):
        return None
    # Glass-box: only for this dhātu.
    upa = (dh.meta.get("upadesha_slp1") or "").strip()
    if upa not in {"YimidA~", "mid", "mida~", "mida"}:
        return None
    # Require following vikaraṇa to be shyan-derived (either upadeśa or post-it-lopa y).
    nxt = state.terms[1]
    if nxt.kind != "pratyaya":
        return None
    nup = (nxt.meta.get("upadesha_slp1") or "").strip()
    if nup not in {"Syan", "y"}:
        return None
    # Upadhā vowel is i in "mid".
    for j, v in enumerate(dh.varnas):
        if v.slp1 == "i":
            return (0, j)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, j = hit
    state.terms[ti].varnas[j] = mk("e")
    state.terms[ti].meta["7_3_82_mide_guna_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.82",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "mideH guRaH",
    text_dev       = "मिदेर्गुणः",
    padaccheda_dev = "मिदेः / गुणः",
    why_dev        = "मिद्-धातोः (दिवादिगणे) श्यन्-प्रसङ्गे गुणः (इ→ए) — अपवादः।",
    anuvritti_from = ("7.3.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

