"""*ṇī* → *nayati* — shared *laṭ* gold spine (steps 1–8) + *nayati* step 9."""
from __future__ import annotations

import sutras  # noqa: F401

from tools.tinanta_jayati_gold import run_jayati_gold_through_step
from tools.tinanta_nayati_gold import (
    NAYATI_DHATU_ROW_ID,
    run_nayati_gold_through_step,
    run_nayati_gold_step9,
)


def test_nayati_checkpoint_after_step1():
    s = run_jayati_gold_through_step(1, dhatu_row_id=NAYATI_DHATU_ROW_ID)
    assert s.flat_slp1() == "RI"


def test_nayati_checkpoint_after_step8():
    s = run_jayati_gold_through_step(8, dhatu_row_id=NAYATI_DHATU_ROW_ID)
    assert s.flat_slp1() == "Rayati"


def test_nayati_full_surface():
    s = run_nayati_gold_through_step(9)
    assert s.flat_slp1() == "nayati"


def test_nayati_step9_idempotent_when_passed_state():
    s8 = run_jayati_gold_through_step(8, dhatu_row_id=NAYATI_DHATU_ROW_ID)
    s9 = run_nayati_gold_step9(s8)
    assert s9.flat_slp1() == "nayati"
