"""दण्डहस्त / दधि शीतलम् — **1.1.10** *nājjhalau* blocks *ac*–*hal* *savarṇa* (user note)."""

from __future__ import annotations

import sutras  # noqa: F401

from phonology.savarna import is_savarna
from pipelines.daNDahasta_nAjjhalau_demo import (
    derive_daNDahasta_nAjjhalau_demo,
    derive_dadhi_SItalam_nAjjhalau_demo,
)


def test_is_savarna_nAjjhalou_ac_hal():
    assert not is_savarna("a", "h")
    assert not is_savarna("h", "a")
    assert not is_savarna("i", "S")


def test_daNDahasta_no_dirgha_across_a_h():
    s = derive_daNDahasta_nAjjhalau_demo()
    assert s.flat_slp1() == "daNDahasta"
    assert "6.1.101" not in {r.get("sutra_id") for r in s.trace if r.get("status") == "APPLIED"}


def test_dadhi_SItalam_no_dirgha_across_i_S():
    s = derive_dadhi_SItalam_nAjjhalau_demo()
    assert s.flat_slp1() == "dadhiSItalam"
    assert "6.1.101" not in {r.get("sutra_id") for r in s.trace if r.get("status") == "APPLIED"}
