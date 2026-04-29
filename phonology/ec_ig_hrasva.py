"""
phonology/ec_ig_hrasva.py — *एच्* → *इक्* resolver shared across operational rules.

Architectural note (engine convention):
  **1.1.48** (*एच इग्घ्रस्वादेशे*) is not duplicated ad hoc inside VIDHI rules;
  instead, whenever another rule requests “hrasva” on an *एच्*-class vowel and the
  output must remain inside the *इक्* domain, those paths call this tiny kernel.

Call sites (non-exhaustive, demo slices):
  • **6.4.92** *mitāṃ hrasvaḥ* — mit dhātu penultimate *एच्* before ṇic (हेड्→हिड्).
  • **1.2.47** *hrasvo napuṃsake …* — neuter prātipadika **final** *एच्* (अतिरै→अतिरि).
  • **1.1.48** — explicit ``apply_rule("1.1.48")`` still wraps the same mutation when a
    recipe arms it (dependency-injector pattern).

Future hooks such as **7.1.59** / **7.4.59**-class augment placements can call this
helper whenever they need *एच्* shortening without introducing a second notion of
“what counts as hrasva for एच्”.
"""
from __future__ import annotations

from typing import Optional

# Narrow Velthuis / internal-SLP1 slice used by current demos.
_EC_TO_IK = frozenset({"e", "E", "o", "O"})


def ec_ig_replacement_slp1(ch: str) -> Optional[str]:
    """If ``ch`` is treated as *एच्* here, return its *इक्* substitute; else ``None``."""
    if ch == "e" or ch == "E":
        return "i"
    if ch == "o" or ch == "O":
        return "u"
    return None


def is_ec_class_for_demo(ch: str) -> bool:
    return ch in _EC_TO_IK
