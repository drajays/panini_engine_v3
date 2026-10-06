"""
7.2.111  इदोऽय् पुंसि  —  VIDHI

इदम् के इद् को अय् आदेश, सुँ परे, पुंलिङ्ग में (अयम्)। ७.२.११० का अपवाद।

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 7.2.111 (padaccheda: इदः अय् पुंसि)
  Source #2 — ashtadhyayi.com śabda-prakriyā for इदम् (the sūtra path of each cell, all three liṅgas)
Pāṭha: ashtadhyayi.com data.txt row i=72111 (Art. 14).
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
    if "idam_m_7_2_108" not in t.tags or "pulliṅga" not in t.tags or "idam_7_2_111_done" in t.tags:
        return None
    return t if _letters(t)[:2] == "id" else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        t.varnas = list(parse_slp1_upadesha_sequence("ay")) + list(t.varnas[2:])
        t.tags.add("idam_7_2_111_done")
    return state


SUTRA = SutraRecord(
    sutra_id="7.2.111",
    sutra_type=SutraType.VIDHI,
    text_slp1='idoy puMsi',
    text_dev='इदोऽय् पुंसि',
    samagra_slp1="idamaH idaH ay pu~si sO",
    samagra_dev="इदमः इदः अय् पुँसि सौ",
    padaccheda_dev='इदः अय् पुंसि',
    why_dev='सुँ परे पुंलिङ्ग इदम् का इद् → अय् (अयम्)।',
    anuvritti_from=("6.4.1", "7.2.84"),
    apavada_of=("7.2.110",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
