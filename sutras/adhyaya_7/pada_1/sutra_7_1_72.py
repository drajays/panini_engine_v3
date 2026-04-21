"""
7.1.72  नपुंसकस्य झलचः  —  VIDHI

Operational role (v3.6, neuter a-stems like ज्ञान):
  When the aṅga is tagged `napuṃsaka` and the following pratyaya is tagged
  `sarvanamasthana` (from 1.1.42 via śi), insert a nuṃ-āgama on the aṅga.

Minimal implementation:
  - append 'n' to the aṅga (nuṃ's surviving consonant) once.
  - (The classical 'u'/'m' of nuṃ are it/augmental and do not surface here.)

This sets up 6.4.8 to lengthen the aṅga's upadhā and yields forms like
ज्ञानानि.
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
    if "anga" not in anga.tags or "napuṃsaka" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if "sarvanamasthana" not in pr.tags:
        return False
    if anga.meta.get("num_agama_done"):
        return False
    if not anga.varnas:
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    anga.varnas.append(mk("n"))
    anga.meta["num_agama_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.72",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "napuMsakasya JalacaH (num AgamaH)",
    text_dev       = "नपुंसकस्य झलचः",
    padaccheda_dev = "नपुंसकस्य झल्-अचः",
    why_dev        = "नपुंसक-अङ्गस्य सर्वनामस्थाने परे नुम्-आगमः (ज्ञानानि)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

