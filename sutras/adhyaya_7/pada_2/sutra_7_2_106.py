"""
7.2.106  तदोः सः सावनन्त्ययोः  —  VIDHI

Operational role (v3.7, for `tad` nominative singular):
  For the prātipadikas `tad` / `tyad`, before su (s~) in prathamā-ekavacana,
  replace initial 't' with 's'.

We implement a narrow phonemic version:
  - aṅga upadeśa is 'tad' or 'tyad'
  - following sup upadeśa identity is s~ (su)
  - replace the first varṇa 't' → 's'
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


_TARGET_STEMS = frozenset({"tad", "tyad"})


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[0]
    pr   = state.terms[1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") != "s~":
        return False
    if anga.meta.get("tad_to_sa_done"):
        return False
    upa = anga.meta.get("upadesha_slp1")
    if upa not in _TARGET_STEMS:
        return False
    if not anga.varnas:
        return False
    if anga.varnas[0].slp1 != "t":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[0]
    anga.varnas[0] = mk("s")
    anga.meta["tad_to_sa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.106",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tadoH saH sAu anantyayoH (suP pare)",
    text_dev       = "तदोः सः सावनन्त्ययोः",
    padaccheda_dev = "त-दोः सः सौ अनन्त्ययोः",
    why_dev        = "तद्/त्यद्-शब्दयोः सुँ-प्रत्यये परे आद्य-तकारस्य सकारादेशः (सः)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

