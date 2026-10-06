"""
7.2.108  इदमो मः  —  VIDHI

इदम्-शब्दस्य सुँ-प्रत्यये परे मकारस्य मकारादेशः — ७.२.१०२ (त्यदादीनामः) का अपवाद, अतः अन्तिम म् बना रहता है (अयम्, इयम्; नपुंसक में सुँ का लुक् पहले हो जाता है)।

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 7.2.108 (padaccheda: इदमः मः)
  Source #2 — ashtadhyayi.com śabda-prakriyā for इदम् (the sūtra path of each cell, all three liṅgas)
Pāṭha: ashtadhyayi.com data.txt row i=72108 (Art. 14).
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
    if (sup.meta.get("upadesha_slp1") or "").strip() != _SAU or "napuṃsaka" in t.tags:
        return None  # neuter su is luk'd by 7.1.23 (earlier in the Aṣṭādhyāyī): there is no sau left
    if "idam_m_7_2_108" in t.tags or not t.varnas or t.varnas[-1].slp1 != "m":
        return None
    return t


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        adesha_substitute_varnas(t, "idam", state, sutra_id="7.2.108", gunadharmas=frozenset({ANGATVA}))
        t.tags.add("idam_m_7_2_108")  # the final m stands: 7.2.102 (final → a) is displaced
    return state


SUTRA = SutraRecord(
    sutra_id="7.2.108",
    sutra_type=SutraType.VIDHI,
    text_slp1='idamo maH',
    text_dev='इदमो मः',
    samagra_slp1="idamaH sO maH",
    samagra_dev="इदमः सौ मः",
    padaccheda_dev='इदमः मः',
    why_dev='इदम्-शब्दस्य सौ परे अन्त्य मकार को मकार ही (७.२.१०२ का अपवाद)।',
    anuvritti_from=("6.4.1", "7.2.84"),
    apavada_of=("7.2.102",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
