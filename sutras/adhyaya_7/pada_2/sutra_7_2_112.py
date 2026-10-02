"""
7.2.112  अनाप्यकः  —  VIDHI

टा / ओस् (आप्) परे अककार इदम् का इद् → अन् (अनेन, अनयोः, अनया)। इदकम् में नहीं।

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 7.2.112 (padaccheda: अन आपि अकः)
  Source #2 — ashtadhyayi.com śabda-prakriyā for इदम् (the sūtra path of each cell, all three liṅgas)
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import ANGATVA, adesha_substitute_varnas
from phonology.varna import parse_slp1_upadesha_sequence

_SAU = "s~"                       # su, by upadeśa identity (Art. 2)
_AP_SUPS = frozenset({"wA", "os"})  # the sups 7.2.112 calls āp: ṭā (also as its ādeśa ina) and os


def _idam(state: State):
    """(index, aṅga, sup) for the idam aṅga followed by its sup, else None."""
    for i, t in enumerate(state.terms[:-1]):
        if "anga" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "idam":
            nxt = state.terms[i + 1]
            if "sup" in nxt.tags and nxt.varnas:
                return i, t, nxt
    return None


def _sup_identity(sup) -> str:
    return (sup.meta.get("upadesha_slp1_original") or sup.meta.get("upadesha_slp1") or "").strip()


def _letters(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _site(state: State):
    r = _idam(state)
    if r is None:
        return None
    i, t, sup = r
    if "idam_7_2_112_done" in t.tags or "idam_7_2_109_done" in t.tags or "idam_m_7_2_108" in t.tags:
        return None
    if _sup_identity(sup) not in _AP_SUPS:
        return None
    return t if _letters(t)[:2] == "id" and len(_letters(t)) > 2 else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        t.varnas = list(parse_slp1_upadesha_sequence("an")) + list(t.varnas[2:])
        t.tags.add("idam_7_2_112_done")
    return state


SUTRA = SutraRecord(
    sutra_id="7.2.112",
    sutra_type=SutraType.VIDHI,
    text_slp1='anApyakaH',
    text_dev='अनाप्यकः',
    padaccheda_dev='अन आपि अकः',
    why_dev='आप् (टा / ओस्) परे अकक्-रहित इदम् का इद् → अन्।',
    anuvritti_from=("6.4.1", "7.2.84"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
