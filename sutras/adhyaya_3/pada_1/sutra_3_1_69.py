"""
3.1.69  दिवादिभ्यः श्यन्  —  VIDHI (apavāda: replace Śap with Śyan for divādi)

Pāṇinian flow:
  3.1.68 (utsarga) first inserts Śap for all dhātus;
  3.1.69 (apavāda) replaces Śap with Śyan for divādi (gaṇa 4) dhātus.

cond: dhātu.meta["gana"] == 4 AND a Śap term is present on the tape.
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


def _dhatu_gana(state: State) -> int | None:
    for t in state.terms:
        if "dhatu" in t.tags:
            g = t.meta.get("gana")
            return int(g) if g is not None else None
    return None


def cond(state: State) -> bool:
    if _dhatu_gana(state) != 4:
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

