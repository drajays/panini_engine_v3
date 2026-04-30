"""
Lexical anchors for **Phit** (``phiṭ``) *prātipadika* lists used in accent demos.

v3 does not mark *udātta* / *anudātta* on ``Varna`` rows; recipes use these
frozensets only inside narrow ``cond`` / ``act`` for **structural** membership
(SLP1 *prātipadika* keys), never for gold-string lookahead.
"""
from __future__ import annotations

from typing import FrozenSet

# Phit 4.18 (user ``prakriya_17`` / Siddhāntakaumudī path): these stems are
# *sarvānudātta* (blocking the *phiṣa* final-*udātta* utsarga).
PHIT_418_SARVANUDATTA_PRATIPADIKA_SLP1: FrozenSet[str] = frozenset(
    {
        "svaN",
        "sama",
        "sima",
        "tya",
        "sapta",
        "stim",
        "ye",
    }
)

__all__ = ["PHIT_418_SARVANUDATTA_PRATIPADIKA_SLP1"]
