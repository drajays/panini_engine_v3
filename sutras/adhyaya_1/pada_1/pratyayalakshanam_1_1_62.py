"""
Support for **1.1.62** *pratyayalope pratyayalakṣaṇam* — not a sūtra file.

Sets ``state.paribhasha_gates[PRATYAYALAKSHANAM_GATE]`` when **1.1.62** fires.
Later *vidhi* rules may consult ``pratyayalakshanam_paribhasha_is_active`` when
they need an explicit engine hook for *pratyaya*-nimitta *kārya* after *lopa*.
"""
from __future__ import annotations

from typing import Final

from engine.state import State

# R2-style key: stable across refactors; value is ``True`` once registered.
PRATYAYALAKSHANAM_GATE: Final[str] = "1.1.62_pratyayalope_pratyayalakshanam"


def pratyayalakshanam_paribhasha_is_active(state: State) -> bool:
    return bool(state.paribhasha_gates.get(PRATYAYALAKSHANAM_GATE))
