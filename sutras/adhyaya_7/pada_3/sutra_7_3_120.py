"""
7.3.120  (घि-अङ्गस्य) टा → ना  —  VIDHI

Operational intent for v3.4 (hari-like i-stems):
  - When a **ghi** aṅga is followed by sup upadeśa **ṭā** (SLP1: wA),
    replace the pratyaya with **nA**.

This enables:
  hari + ṭā → hari + nA → hari nA → (8.4.2) hariṇā

Blindness:
  - cond() keys only off tags + pratyaya.meta['upadesha_slp1'].
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags or "ghi" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") != "wA":
        return False
    if pr.meta.get("ta_to_na_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = state.terms[-1]
    pr.varnas = [mk("n"), mk("A")]
    pr.meta["ta_to_na_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "wA")
    pr.meta["upadesha_slp1"] = "nA"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.120",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Gi-aNgasya wA nA",
    text_dev       = "घि-अङ्गस्य टा ना",
    padaccheda_dev = "घि-अङ्गस्य टा → ना",
    why_dev        = "घि-संज्ञक-अङ्गात् परे टा-प्रत्यये ‘ना’ आदेशः (हरि-इत्यादौ हरिणा)।",
    anuvritti_from = ("7.3.111",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

