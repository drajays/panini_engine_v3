"""
Support for **1.1.60** *lopa* saṃjñā — not a sūtra file.

*Lopa* (operational deletion of a *varṇa* or group) is **named** by this saṃjñā;
actual elision is performed by *vidhi* sūtras (e.g. **1.3.9** *tasya lopaḥ* for *it*,
**8.2.23**, **6.1.68**, …) that consult *it* tags / state, not by re-invoking 1.1.60.

Constitution Art. 2: helpers here do not read *vibhakti* / *lakāra* coordinates.
"""
from __future__ import annotations

from typing import Final

from engine.state import State

# R2 payload after successful ``apply_rule("1.1.60", ...)`` — definiens token.
LOPA_REGISTER_VALUE: Final[frozenset[str]] = frozenset({"1.1.60_sTAne_adarSanam"})

LOPA_SAMJNA_KEY: Final[str] = "lopa"


def lopa_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get(LOPA_SAMJNA_KEY) == LOPA_REGISTER_VALUE
