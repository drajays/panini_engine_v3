"""
7.3.119  (घि-अङ्गात्) ङि परे ...  —  VIDHI

Operational intent for v3.4 (hari-like i-stems):
  - When a **ghi** aṅga is followed by sup upadeśa **ṅi** (SLP1: Ni),
    perform the classic locative-singular outcome:

      hari + ṅi  →  har + au   (harau)

We implement the minimal mechanical transformation:
  - Replace aṅga-final hrasva IK (i/u) with 'a'
  - Replace the pratyaya with 'O' (au)

Blindness:
  - cond() reads only tags + upadeśa identity.
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
    if pr.meta.get("upadesha_slp1") != "Ni":
        return False
    if pr.meta.get("ngi_to_au_done"):
        return False
    if not anga.varnas:
        return False
    if anga.varnas[-1].slp1 not in {"i", "u"}:
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    pr   = state.terms[-1]
    anga.varnas[-1] = mk("a")   # hrasva IK → a (minimal scope for hari-type)
    pr.varnas = [mk("O")]       # ṅi → au
    pr.meta["ngi_to_au_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "Ni")
    pr.meta["upadesha_slp1"] = "O"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.119",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Gi-aNgAt Ni pare aNgasya a, NyaH au",
    text_dev       = "घि-अङ्गात् ङि परे (अङ्गस्य अ, ङ्यः औ)",
    padaccheda_dev = "घि-अङ्गात् ङि परे — अङ्ग-परिवर्तनम् + प्रत्यय-आदेशः",
    why_dev        = "घि-अङ्गात् ङि-प्रत्यये परे ‘हरौ’ इत्यादि-रूपसिद्ध्यर्थम् (अन्तिम-इक् → अ, ङि → औ)।",
    anuvritti_from = ("7.3.111",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

