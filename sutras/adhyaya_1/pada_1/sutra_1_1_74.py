"""
1.1.74  त्यदादीनि च  (tyadAdIni ca)  —  SAMJNA

Anuvṛtti: sarvanāma (from 1.1.27 sarvādīni sarvanāmāni)

Classical role:
  "The tyadādi words (tyad etc.) also [get sarvanāma-saṃjñā]."

  The tyadādi-gaṇa contains: tyad, tad, yad, etad, idam, adas, kim.
  These pronouns were not listed in the sarvādi-gaṇa (1.1.27) and are
  granted sarvanāma-saṃjñā separately by this sūtra.

  The practical consequence is that all rules that apply to sarvanāmans
  (e.g., case-suffix substitutions, the ghī-ṅīṣ rules, etc.) extend to
  tyad, tad, yad, etad, idam, adas, and kim as well.

v3 engine role:
  - Loads tyadādi list from data/inputs/tyadadi_slp1.json at module level
    (lazy singleton).
  - cond() checks for any Term with "anga" + "prātipadika" tags whose
    upadesha_slp1 is in the tyadādi list AND "sarvanama" not already set.
  - act() adds "sarvanama" to eligible Terms and registers the word-set
    in samjna_registry for audit.
  - No paradigm coordinate access; no surface Devanāgarī; no arm flags.
  - r1_form_identity_exempt=True (pure SAMJNA, no surface rewrite).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing  import Optional, Set

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


_TYADADI: Optional[Set[str]] = None


def _load_tyadadi() -> Set[str]:
    global _TYADADI
    if _TYADADI is not None:
        return _TYADADI
    path = Path(__file__).parents[3] / "data" / "inputs" / "tyadadi_slp1.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    _TYADADI = set(data.get("tyadadi", []))
    return _TYADADI


def _eligible(state: State):
    tyadadi = _load_tyadadi()
    for t in state.terms:
        if "anga" not in t.tags:
            continue
        if "prātipadika" not in t.tags:
            continue
        if "sarvanama" in t.tags:
            continue
        upa = t.meta.get("upadesha_slp1")
        if not isinstance(upa, str):
            continue
        if upa in tyadadi:
            yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    state.samjna_registry["1_1_74_tyadAdi"] = frozenset(_load_tyadadi())
    for t in _eligible(state):
        t.tags.add("sarvanama")
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.1.74",
    sutra_type              = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1               = "tyadAdIni ca",
    text_dev                = "त्यदादीनि च",
    padaccheda_dev          = "त्यद्-आदीनि / च",
    why_dev                 = (
        "त्यद्-आदि-गण-पठिताः शब्दाः (त्यद्, तद्, यद्, एतद्, इदम्, अदस्, किम्) "
        "सर्वनाम-संज्ञकाः च — १.१.२७ अनुवृत्त्या। "
        "तेन एतेष्वपि सर्वनाम-विषयकाः विधयः प्रवर्तन्ते।"
    ),
    anuvritti_from          = ("1.1.27",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
