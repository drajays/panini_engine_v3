"""
Support for **1.3.10** *samānām anudeśaḥ yathāsaṅkhyam* — not a sūtra file.

Sets ``state.paribhasha_gates[YATHASANKHYAM_GATE]`` when **1.3.10** fires.
``yathasankhyam_paribhasha_is_active`` is for *vidhi* code that must align two
same-length lists by ordinal position (*anudeśa* = the stated relation).
"""
from __future__ import annotations

from typing import Final

from engine.state import State

YATHASANKHYAM_GATE: Final[str] = "1.3.10_samAnAm_anudesa_yathAsaNKyam"


def yathasankhyam_paribhasha_is_active(state: State) -> bool:
    return bool(state.paribhasha_gates.get(YATHASANKHYAM_GATE))
