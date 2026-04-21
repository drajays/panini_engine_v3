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

from phonology.varna import AC_DEV, AC_MATRA, HAL_BASE, HAL_DEV


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
    defer_chandrabindu = False
    chandrabindu_after_hal_idx: int | None = None
    n = len(varnas)

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
            if chandrabindu_after_hal_idx is not None and idx == chandrabindu_after_hal_idx:
                out.append(HAL_BASE[slp] + _CHANDRABINDU)
                chandrabindu_after_hal_idx = None
                prev_was_halanta_consonant = False
            else:
                out.append(devv)
                prev_was_halanta_consonant = True
            continue

        # Inherent-a after consonant: Varna(slp1='a', dev='').
        if slp == "a" and devv == "":
            if prev_was_halanta_consonant:
                out[-1] = out[-1][:-1]  # drop the virāma → inherent a
                if defer_chandrabindu:
                    out.append(_CHANDRABINDU)
                    defer_chandrabindu = False
                elif (
                    "anunasika" in (v.tags or set())
                    and idx + 2 < n
                    and varnas[idx + 1].slp1 in HAL_DEV
                    and varnas[idx + 2].slp1 in HAL_DEV
                ):
                    # e.g. SLP1 ``qupac~z`` → … a(anunāsika), c, ṣ — candrabindu is
                    # written on the vowel of the *second* consonant (चँ) even
                    # when there is no explicit inherent ``a`` Varṇa before ``ṣ``.
                    chandrabindu_after_hal_idx = idx + 1
                elif (
                    "anunasika" in (v.tags or set())
                    and idx + 2 < n
                    and varnas[idx + 1].slp1 in HAL_DEV
                    and varnas[idx + 2].slp1 == "a"
                    and varnas[idx + 2].dev == ""
                    and "anunasika" not in (varnas[idx + 2].tags or set())
                ):
                    # Medial cluster vowel carries anunāsika; book orthography
                    # places candrabindu after the following consonant (चँ).
                    defer_chandrabindu = True
                else:
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
