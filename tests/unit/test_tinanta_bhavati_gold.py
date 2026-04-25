"""*bhū* → *bhavati* — shared *laṭ* spine + *jayati*-style Tripāḍī step 9."""
from __future__ import annotations

import sutras  # noqa: F401

from pipelines.tinanta_bhavati_gold import (
    BHAVATI_DHATU_ROW_ID,
    run_bhavati_gold_through_step,
    run_bhavati_gold_step9,
)
from pipelines.tinanta_jayati_gold import run_jayati_gold_through_step


def test_bhavati_checkpoint_after_step1():
    s = run_jayati_gold_through_step(1, dhatu_row_id=BHAVATI_DHATU_ROW_ID)
    assert s.flat_slp1() == "BU"


def test_bhavati_checkpoint_after_step8():
    s = run_jayati_gold_through_step(8, dhatu_row_id=BHAVATI_DHATU_ROW_ID)
    assert s.flat_slp1() == "Bavati"


def test_bhavati_full_surface():
    s = run_bhavati_gold_through_step(9)
    assert s.flat_slp1() == "Bavati"


def test_bhavati_step9_from_state():
    s8 = run_jayati_gold_through_step(8, dhatu_row_id=BHAVATI_DHATU_ROW_ID)
    s9 = run_bhavati_gold_step9(s8)
    assert s9.flat_slp1() == "Bavati"
