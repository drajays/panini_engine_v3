"""
3.4.21  समानकर्तृकयोः पूर्वकाले  —  VIDHI (narrow: attach ktvā placeholder)

Engine (glass-box):
  This sūtra is represented as a narrow “attach kṛt ktvā” step when the recipe
  arms it via ``state.meta['3_4_21_ktvA_arm']``.

  It appends a pratyaya ``Term`` whose surface tape is modelled as ``itvA`` with
  ancestry marker ``upadesha_slp1_original='ktvA'`` (same convention as existing
  ktvā demos).  It does not handle full semantic eligibility.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not state.meta.get("3_4_21_ktvA_arm"):
        return False
    if not any("dhatu" in t.tags for t in state.terms):
        return False
    # Only once per derivation.
    return not any((t.meta.get("upadesha_slp1_original") or "") == "ktvA" for t in state.terms)


def act(state: State) -> State:
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("itvA")),
        tags={"pratyaya", "krt", "ardhadhatuka"},
        meta={"upadesha_slp1": "itvA", "upadesha_slp1_original": "ktvA"},
    )
    state.terms.append(pr)
    state.meta["3_4_21_ktvA_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.21",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "samAnakartrukayoH pUrvakAle (ktvA)",
    text_dev       = "समानकर्तृकयोः पूर्वकाले (क्त्वा)",
    padaccheda_dev = "समानकर्तृकयोः / पूर्वकाले",
    why_dev        = "समानकर्तृक-पूर्वकाले क्त्वा-प्रत्यय-स्थापनम् (नैरोप्य-डेमो)।",
    anuvritti_from = ("3.1.1", "3.1.2", "3.1.3", "3.1.91"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

