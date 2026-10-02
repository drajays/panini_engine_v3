"""
7.2.109  दश्च  —  VIDHI

इदम् का शेष दकार मकार हो जाता है विभक्ति परे (इमौ, इमे, इमम्, इमान्, इमानि …)। हल्-आदि विभक्ति में ७.२.११३ ने इद् का लोप पहले ही कर दिया होता है।

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 7.2.109 (padaccheda: दः च)
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
    if "idam_7_2_109_done" in t.tags or "idam_m_7_2_108" in t.tags:
        return None
    ls = _letters(t)
    return t if ls[:2] == "id" and len(ls) > 2 else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        t.varnas = list(parse_slp1_upadesha_sequence("im")) + list(t.varnas[2:])
        t.tags.add("idam_7_2_109_done")
    return state


SUTRA = SutraRecord(
    sutra_id="7.2.109",
    sutra_type=SutraType.VIDHI,
    text_slp1='daSca',
    text_dev='दश्च',
    padaccheda_dev='दः च',
    why_dev='विभक्ति परे इदम् का द् → म् (अपवाद-क्रम में ७.२.११२, ७.२.११३ के बाद)।',
    anuvritti_from=("6.4.1", "7.2.84"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
