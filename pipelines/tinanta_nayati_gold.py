"""
*Na*yati* gold *laṭ* *prathamā* *eka* — same nine-step spine as *jayati*
(``pipelines.tinanta_jayati_gold``), *dhātu* **णीञ्** (``RIY``, row ``BvAdi_950``).

Steps **1–8** are shared rule chains (``dhatu_row_id``); **step 9** differs:

- **8.1.16** (*pad* *adhikāra*)
- **6.1.65** *ṇo naḥ* — initial ``R`` (ण्) of the *aṅga* becomes ``n`` (न्), yielding
  ``nayati``.  (Pedagogy often cites Tripāḍī *ṇ*–*n* allusions; the engine applies
  **6.1.65** here and it must run **before** **8.2.1** so it is not *asiddha* outside
  Tripāḍī once the zone is open.)
- **8.2.1** (Tripāḍī) → **8.2.66** (skip on this shape)

See ``pipelines.tinanta_bhavati_gold`` (*bhū*) and ``pipelines.tinanta_tarati_gold`` (*tṛ*).
"""
from __future__ import annotations

from typing import Final, Tuple

import sutras  # noqa: F401

from engine.state import State

from pipelines.tinanta_jayati_gold import (
    apply_rule_chain,
    run_jayati_gold_step8,
    run_jayati_gold_through_step,
)

NAYATI_DHATU_ROW_ID: Final[str] = "BvAdi_950"

STEP_9_NAYATI_RULE_IDS: Final[Tuple[str, ...]] = (
    "8.1.16",
    "6.1.65",
    "8.2.1",
    "8.2.66",
)


def run_nayati_gold_step9(state: State | None = None) -> State:
    """
    **Step 9** for *ṇī* → *nayati*: **8.1.16** → **6.1.65** → **8.2.1** → **8.2.66**.

    If ``state`` is *None*, runs ``run_jayati_gold_step8`` with ``BvAdi_950`` first.
    """
    s = (
        run_jayati_gold_step8(None, dhatu_row_id=NAYATI_DHATU_ROW_ID)
        if state is None
        else state
    )
    s = apply_rule_chain(s, STEP_9_NAYATI_RULE_IDS)
    s.meta["gold_nayati_step9"] = {
        "pada_adhikAra_8_1_16"   : True,
        "Ro_naH_6_1_65"         : True,
        "tripadi_8_2_1"         : True,
        "8_2_66_sasajuzo_ruH"   : "COND-FALSE (no pada-final s)",
    }
    return s


def run_nayati_gold_through_step(n: int, state: State | None = None) -> State:
    """Run steps ``1 .. n`` for *ṇī* + *laṭ* *prathamā* *eka* (``n`` … *ti*)."""
    if n < 1 or n > 9:
        raise ValueError(f"steps 1–9 supported; got n={n!r}")
    if n < 9:
        return run_jayati_gold_through_step(
            n, state, dhatu_row_id=NAYATI_DHATU_ROW_ID,
        )
    s8 = run_jayati_gold_through_step(
        8, state, dhatu_row_id=NAYATI_DHATU_ROW_ID,
    )
    return run_nayati_gold_step9(s8)
