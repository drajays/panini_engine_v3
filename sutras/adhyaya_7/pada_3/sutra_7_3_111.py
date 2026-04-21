"""
7.3.111  घि-अङ्गस्य ङिति गुणः  —  VIDHI

Operational intent for v3.4 (hari-like i-stems):
  - If the aṅga is tagged **ghi** and the following sup upadeśa is one of
    the classic **ṅit/ṅiti** sup pratyayas (identified by their upadeśa id),
    then apply **guṇa** to the aṅga-final hrasva IK vowel.

We implement the minimal guṇa mapping for hrasva i/u (generalizable later):
  i → e
  u → o

Blindness:
  - cond() reads tags, aṅga-final phoneme, and pratyaya.meta['upadesha_slp1'] only.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


# Exclude 'Ni' because the more specific 7.3.119 handles that case (harau).
_NGIT_SUP_UPADESHA = frozenset({"Ne", "Nas", "Nasi"})
_GUNA_MAP = {"i": "e", "u": "o"}


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags or "ghi" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") not in _NGIT_SUP_UPADESHA:
        return False
    if pr.meta.get("ghi_guna_done"):
        return False
    if not anga.varnas:
        return False
    if anga.varnas[-1].slp1 not in _GUNA_MAP:
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    pr   = state.terms[-1]
    anga.varnas[-1] = mk(_GUNA_MAP[anga.varnas[-1].slp1])
    pr.meta["ghi_guna_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.111",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Gi-aNgasya Niti guRaH",
    text_dev       = "घि-अङ्गस्य ङिति गुणः",
    padaccheda_dev = "घि-अङ्गस्य ङिति गुणः",
    why_dev        = "घि-संज्ञक-अङ्गात् परे ङिति-सुप्-प्रत्यये गुणः (हरि → हरे ...)।",
    anuvritti_from = ("7.3.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

