"""
phonology/tokenizer.py — surface Devanāgarī → List[Varna].
────────────────────────────────────────────────────────────

The inverse of phonology/joiner.py.  USED ONLY BY TESTS (forward and
backward) — the engine itself never tokenizes a surface; it always
starts from an upadeśa varṇa list built via phonology.varna.mk().

Rules:
  • Standalone vowel chars (अ आ इ ई ...)  → Varna(slp1, AC_DEV[slp1])
  • Consonant + virāma ('क्')               → Varna(slp1, HAL_DEV[slp1])
  • Consonant + mātrā ('का', 'कि')         → two Varnas:
       1) Varna(slp1='k', dev='क्')  — halanta form
       2) Varna(slp1='A', dev='आ')   — standalone vowel
     (We use halanta + standalone as the CANONICAL internal form,
      even though the SURFACE writes a conjunct.  The joiner reverses
      this cleanly.)
  • Consonant by itself ('क')               → Varna(slp1='k', dev='क्') +
                                              Varna(slp1='a', dev='')
  • Anusvāra ('ं') → Varna('M', 'ं')
  • Visarga  ('ः') → Varna('H', 'ः')
"""
from __future__ import annotations

from typing import List

from engine.state     import Varna
from phonology.varna  import AC_DEV, AC_MATRA, HAL_DEV


_VIRAMA = "्"

# Reverse maps.
_DEV_TO_SLP1_VOWEL    = {v: k for k, v in AC_DEV.items()}
_MATRA_TO_SLP1        = {v: k for k, v in AC_MATRA.items() if v}
_DEV_TO_SLP1_CONSONANT = {v[:-1]: k for k, v in HAL_DEV.items()}  # 'क' → 'k'


def devanagari_to_varnas(text: str) -> List[Varna]:
    """
    Tokenize a Devanāgarī string to an internal Varna list.
    """
    out: List[Varna] = []
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        # Consonant base?
        if ch in _DEV_TO_SLP1_CONSONANT:
            slp1 = _DEV_TO_SLP1_CONSONANT[ch]
            # Halanta form 'क्' in our canonical mk().
            halanta = HAL_DEV[slp1]
            # Look ahead: virāma?
            if i + 1 < n and text[i+1] == _VIRAMA:
                out.append(Varna(slp1=slp1, dev=halanta, tags=set()))
                i += 2
                continue
            # Mātrā?
            if i + 1 < n and text[i+1] in _MATRA_TO_SLP1:
                vslp1 = _MATRA_TO_SLP1[text[i+1]]
                out.append(Varna(slp1=slp1, dev=halanta, tags=set()))
                out.append(Varna(slp1=vslp1, dev=AC_DEV[vslp1], tags=set()))
                i += 2
                continue
            # Bare consonant → inherent a.
            out.append(Varna(slp1=slp1, dev=halanta, tags=set()))
            out.append(Varna(slp1="a", dev="", tags=set()))
            i += 1
            continue

        # Standalone vowel?
        if ch in _DEV_TO_SLP1_VOWEL:
            slp1 = _DEV_TO_SLP1_VOWEL[ch]
            out.append(Varna(slp1=slp1, dev=ch, tags=set()))
            i += 1
            continue

        # Anusvāra / visarga.
        if ch == "ं":
            out.append(Varna(slp1="M", dev="ं", tags=set()))
            i += 1
            continue
        if ch == "ः":
            out.append(Varna(slp1="H", dev="ः", tags=set()))
            i += 1
            continue

        # Unrecognized — skip quietly; tests will catch.
        i += 1

    return out
