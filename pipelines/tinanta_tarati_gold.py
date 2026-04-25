"""
*Tarati* gold *laṭ* *prathamā* *eka* — same spine as *jayati* / *bhavati*
(``pipelines.tinanta_jayati_gold``), *dhātu* **तॄ** (``tF``, row ``BvAdi_951``).

``BvAdi_951`` is a **curated** *bhvādi*-style row (``dhatupatha_upadesha.json``)
so **3.1.68** *śap* and **7.3.84** + **1.1.51** (*ṝ* → *ar*) match the *tarati*
pedagogy; the classical **divādi** row ``divAdi_tF`` remains for other demos.

Steps **1–8** reuse ``dhatu_row_id=TARATI_DHATU_ROW_ID`` (step 7 includes **1.1.51**
from the shared ``STEP_7_RULE_IDS``).  **Step 9** matches *jayati* / *bhavati*.
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

TARATI_DHATU_ROW_ID: Final[str] = "BvAdi_951"


def run_tarati_gold_step9(state: State | None = None) -> State:
    """
    **Step 9** for *tṛ* → *tarati*: Tripāḍī audit (same as *jayati*).

    If ``state`` is *None*, runs step 8 for ``BvAdi_951`` first.
    """
    s = (
        run_jayati_gold_step8(None, dhatu_row_id=TARATI_DHATU_ROW_ID)
        if state is None
        else state
    )
    return run_jayati_gold_step9(s)


def run_tarati_gold_through_step(n: int, state: State | None = None) -> State:
    """Run steps ``1 .. n`` for *tṛ* + *laṭ* *prathamā* *eka*."""
    if n < 1 or n > 9:
        raise ValueError(f"steps 1–9 supported; got n={n!r}")
    if n < 9:
        return run_jayati_gold_through_step(
            n, state, dhatu_row_id=TARATI_DHATU_ROW_ID,
        )
    s8 = run_jayati_gold_through_step(
        8, state, dhatu_row_id=TARATI_DHATU_ROW_ID,
    )
    return run_tarati_gold_step9(s8)
