"""
phonology/joiner.py — Varṇa list → Devanāgarī surface string.
──────────────────────────────────────────────────────────────

Rules (pure mechanical):

  1. Consonant Varna (dev ends in '्') followed by a vowel Varna:
       strip the virāma, append the vowel's mātrā.
  2. Consonant Varna followed by inherent-a Varna (dev == ""):
       strip the virāma, append nothing (inherent a).
  3. Consonant Varna followed by another consonant Varna:
       emit the first as-is (halanta), then the second.
  4. Vowel Varna at start-of-word: emit standalone form.
  5. Vowel Varna after a consonant: should never happen unless the
     consonant is already written halanta — in that case, emit a
     full vowel (rare; flags a bug-upstream).
"""
from __future__ import annotations

from typing import List

from phonology.varna import AC_DEV, AC_MATRA, HAL_DEV


_VIRAMA = "्"
# Devanāgarī candrabindu — same anunāsika signal as SLP1 '~' on vowels in upadeśa.
_CHANDRABINDU = "\u0901"


def _maybe_anunasika_chandrabindu(v) -> str:
    tags = getattr(v, "tags", None) or set()
    return _CHANDRABINDU if "anunasika" in tags else ""


def slp1_to_devanagari(varnas: List) -> str:
    """
    `varnas` is a list of Varna (engine.state.Varna) instances.
    """
    out: List[str] = []
    prev_was_halanta_consonant = False

    for idx, v in enumerate(varnas):
        slp  = v.slp1
        devv = v.dev

        # Consonant?
        if slp in HAL_DEV:
            # Correct conjunct: keep the virāma on the EARLIER consonant
            # (which will be rendered by the font as the conjunct glyph
            # via the virāma-ligation rule), and append the next halanta.
            # We do NOT strip the virāma here — that only happens
            # when a VOWEL follows the final halanta.
            out.append(devv)
            prev_was_halanta_consonant = True
            continue

        # Inherent-a after consonant: Varna(slp1='a', dev='').
        if slp == "a" and devv == "":
            if prev_was_halanta_consonant:
                out[-1] = out[-1][:-1]  # drop the virāma → inherent a
                # ँ is written right after the vowel that is anunāsika — never moved
                # (Ga~wa → घँट and Gawa~ → घटँ are different upadeśas).
                out.append(_maybe_anunasika_chandrabindu(v))
            else:
                out.append(AC_DEV["a"])
                out.append(_maybe_anunasika_chandrabindu(v))
            prev_was_halanta_consonant = False
            continue

        # Regular vowel.
        if slp in AC_DEV:
            if prev_was_halanta_consonant:
                # Replace virāma with mātrā.
                out[-1] = out[-1][:-1] + AC_MATRA[slp]
            else:
                out.append(AC_DEV[slp])
            out.append(_maybe_anunasika_chandrabindu(v))
            prev_was_halanta_consonant = False
            continue

        # Anusvāra / visarga / anything special — emit as-is.
        out.append(devv)
        prev_was_halanta_consonant = False

    return "".join(out)
