"""*tṛ* → *tarati* — shared *laṭ* spine (BvAdi_951) + *jayati*-style step 9."""
from __future__ import annotations

import sutras  # noqa: F401

from pipelines.tinanta_jayati_gold import run_jayati_gold_through_step
from pipelines.tinanta_tarati_gold import (
    TARATI_DHATU_ROW_ID,
    run_tarati_gold_through_step,
    run_tarati_gold_step9,
)


def test_tarati_checkpoint_after_step1():
    s = run_jayati_gold_through_step(1, dhatu_row_id=TARATI_DHATU_ROW_ID)
    assert s.flat_slp1() == "tF"


def test_tarati_checkpoint_after_step7():
    s = run_jayati_gold_through_step(7, dhatu_row_id=TARATI_DHATU_ROW_ID)
    assert s.flat_slp1() == "tarati"


def test_tarati_checkpoint_after_step8():
    s = run_jayati_gold_through_step(8, dhatu_row_id=TARATI_DHATU_ROW_ID)
    assert s.flat_slp1() == "tarati"


def test_tarati_full_surface():
    s = run_tarati_gold_through_step(9)
    assert s.flat_slp1() == "tarati"


def test_tarati_step9_from_state():
    s8 = run_jayati_gold_through_step(8, dhatu_row_id=TARATI_DHATU_ROW_ID)
    s9 = run_tarati_gold_step9(s8)
    assert s9.flat_slp1() == "tarati"
