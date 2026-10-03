"""
*Tarati* gold *laṭ* *prathamā* *eka* — *dhātu* **तॄ** (``tF``, row ``BvAdi_951``).

Same nine-step spine as *jayati* (``tools.tinanta_jayati_gold``); only the
``dhatu_row_id`` differs.  Step 7 yields *ṝ* → *ar* via **7.3.84** + **1.1.51**;
no step-9-specific rule is needed.
"""
from __future__ import annotations

from typing import Final

import sutras  # noqa: F401

from engine.state import State
from tools.tinanta_jayati_gold import run_jayati_gold_through_step

TARATI_DHATU_ROW_ID: Final[str] = "BvAdi_951"


def run_tarati_gold_through_step(n: int, state: State | None = None) -> State:
    """Run steps ``1 .. n`` for *tṝ* + *laṭ* *prathamā* *eka* (``n`` … *ti*)."""
    return run_jayati_gold_through_step(n, state, dhatu_row_id=TARATI_DHATU_ROW_ID)
