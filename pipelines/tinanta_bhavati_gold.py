"""
*Bhavati* gold *laṭ* *prathamā* *eka* — same spine as *jayati*
(``pipelines.tinanta_jayati_gold``), *dhātu* **भू** (``BU``, row ``BvAdi_01_0001``).

Steps **1–8** reuse ``run_jayati_gold_through_step(..., dhatu_row_id=…)``.  **Step 9**
matches *jayati*: **8.1.16** → **8.2.1** → **8.2.66** (no **6.1.65** — no initial ``R``).

Checkpoint *SLP1*: ``BU`` after step 1; ``Bavati`` after step 8 (``o`` + ``a`` → ``av``
per **6.1.78**).
"""
from __future__ import annotations

from typing import Final

import sutras  # noqa: F401

from engine.state import State

from pipelines.tinanta_jayati_gold import (
    run_jayati_gold_step8,
    run_jayati_gold_step9,
    run_jayati_gold_through_step,
)

BHAVATI_DHATU_ROW_ID: Final[str] = "BvAdi_01_0001"


def run_bhavati_gold_step9(state: State | None = None) -> State:
    """
    **Step 9** for *bhū* → *bhavati*: Tripāḍī audit only (same rule list as *jayati*).

    If ``state`` is *None*, runs step 8 for ``BvAdi_01_0001`` first.
    """
    s = (
        run_jayati_gold_step8(None, dhatu_row_id=BHAVATI_DHATU_ROW_ID)
        if state is None
        else state
    )
    return run_jayati_gold_step9(s)


def run_bhavati_gold_through_step(n: int, state: State | None = None) -> State:
    """Run steps ``1 .. n`` for *bhū* + *laṭ* *prathamā* *eka*."""
    if n < 1 or n > 9:
        raise ValueError(f"steps 1–9 supported; got n={n!r}")
    if n < 9:
        return run_jayati_gold_through_step(
            n, state, dhatu_row_id=BHAVATI_DHATU_ROW_ID,
        )
    s8 = run_jayati_gold_through_step(
        8, state, dhatu_row_id=BHAVATI_DHATU_ROW_ID,
    )
    return run_bhavati_gold_step9(s8)
