"""
7.2.102  त्यदादीनामः  —  VIDHI

Operational role (v3.7, for `tad`-like tyadādi pronouns):
  When an aṅga is tagged `tyadadi`, replace its final consonant (HAL) with
  the vowel 'a'.

This is a narrow implementation sufficient for तद्:
  tad (t-a-d) → ta (t-a-a) and 6.1.97 will collapse the double 'a'.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import HAL, mk


def _matches(state: State) -> bool:
    if not state.terms:
        return False
    anga = state.terms[0]
    if "anga" not in anga.tags or "tyadadi" not in anga.tags:
        return False
    if not anga.varnas:
        return False
    if anga.meta.get("tyadadi_a_adesha_done"):
        return False
    if anga.varnas[-1].slp1 not in HAL:
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[0]
    anga.varnas[-1] = mk("a")
    anga.meta["tyadadi_a_adesha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.102",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tyadAdInAm aH",
    text_dev       = "त्यदादीनामः",
    padaccheda_dev = "त्यदादीनाम् अः",
    why_dev        = "त्यदादि-गण-शब्दानां विभक्ति-प्रत्यये परे अन्त्य-हल्-स्थानि अकार-आदेशः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

