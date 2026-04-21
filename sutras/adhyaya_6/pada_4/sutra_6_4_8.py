"""
6.4.8  सर्वनामस्थाने चासम्बुद्धौ  —  VIDHI

Operational role (v3.6, neuter a-stems like ज्ञानानि):
  After 7.1.72 inserts nuṃ (n) on the aṅga, when the following pratyaya
  is `sarvanamasthana` and NOT sambuddhi, lengthen the aṅga's upadhā-vowel.

Minimal implementation for a-stems ending in -na:
  - if the aṅga ends with ... n + a + n (i.e. final 'n' from nuṃ, and
    the preceding varṇa is the inherent 'a'), change that 'a' to 'A'.

This yields: jYAna + n + i → jYAnAn + i → ज्ञानानि (after joiner).
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
    if "sambuddhi" in pr.tags:
        return False
    if anga.meta.get("sarvanamasthana_upadha_dirgha_done"):
        return False
    if len(anga.varnas) < 3:
        return False
    # Expect ... n a n (where the last n is the nuṃ insertion).
    if anga.varnas[-1].slp1 != "n":
        return False
    if anga.varnas[-2].slp1 != "a":
        return False
    if anga.varnas[-3].slp1 != "n":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    anga.varnas[-2] = mk("A")
    anga.meta["sarvanamasthana_upadha_dirgha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.8",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "sarvanAmasthAne ca asambuddhau",
    text_dev       = "सर्वनामस्थाने चासम्बुद्धौ",
    padaccheda_dev = "सर्वनामस्थाने च असम्बुद्धौ",
    why_dev        = "असम्बुद्धि-सर्वनामस्थाने परे नपुंसक-अङ्गस्य उपधा-अकारस्य दीर्घः (ज्ञानानि)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

