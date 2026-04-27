"""
3.1.69  दिवादिभ्यः श्यन्  —  VIDHI (narrow: replace Sap with Syan)

Glass-box scope for `medyati`:
  When a pipeline marks a divādi-dhātu and a `Sap` vikaraṇa has been inserted
  (3.1.68), replace that `Sap` term with `Syan`.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _find_sap(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "Sap":
            return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("3_1_69_syan_arm"):
        return False
    return _find_sap(state) is not None


def act(state: State) -> State:
    i = _find_sap(state)
    if i is None:
        return state
    syan = Term(
        kind="pratyaya",
        # Use SyaN so the trailing nasal (N) can be it (1.3.3), yielding **ya** after lopa.
        varnas=parse_slp1_upadesha_sequence("SyaN"),
        tags={"pratyaya", "vikarana", "upadesha"},
        meta={"upadesha_slp1": "Syan"},
    )
    state.terms[i] = syan
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.69",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "divAdibhyaH Syan",
    text_dev       = "दिवादिभ्यः श्यन्",
    padaccheda_dev = "दिवादिभ्यः / श्यन्",
    why_dev        = "दिवादिगणीय-धातोः सार्वधातुके कर्तरि शप्-अपवादः — श्यन्-विकरणः।",
    anuvritti_from = ("3.1.67", "3.1.91"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

