"""Bhaṭṭikāvya 1.1 (जयमङ्गला) — eight padāni, engine-derived."""
from __future__ import annotations

import pytest

from pipelines.bhattikavya_1_1 import (
    derive_aBUt,
    derive_guNAH,
    derive_nfpaH,
    derive_paraMtapaH,
    derive_sanAtanaH,
    derive_upAgamat,
    derive_varaH,
    derive_vibuDasaKaH,
)


def _applied(s):
    return [x["sutra_id"] for x in s.trace if x.get("status") == "APPLIED" and x.get("sutra_id")]


def test_aBUt():
    s = derive_aBUt()
    assert s.flat_slp1() == "aBUt"
    ids = _applied(s)
    for sid in ("3.2.110", "3.1.43", "3.1.44", "2.4.77", "6.4.71"):
        assert sid in ids


def test_upAgamat():
    s = derive_upAgamat()
    assert s.flat_slp1() == "upAgamat"
    ids = _applied(s)
    assert "3.1.55" in ids and "6.4.71" in ids and "6.1.101" in ids


def test_nfpaH():
    s = derive_nfpaH()
    assert s.flat_slp1() == "nfpaH"
    ids = _applied(s)
    assert "3.2.3" in ids and "6.4.64" in ids


def test_vibuDasaKaH():
    s = derive_vibuDasaKaH()
    assert s.flat_slp1() == "vibuDasaKaH"
    ids = _applied(s)
    assert "3.1.135" in ids and "5.4.91" in ids and "6.4.148" in ids


def test_paraMtapaH():
    s = derive_paraMtapaH()
    assert s.flat_slp1() in {"paraMtapaH", "parentapaH"}
    ids = _applied(s)
    assert "3.2.39" in ids and "6.4.94" in ids and "6.3.67" in ids


def test_guNAH():
    s = derive_guNAH()
    assert s.flat_slp1() in {"guNAH", "guRaH", "guRAH"}
    assert "3.3.16" in _applied(s)


def test_varaH():
    s = derive_varaH()
    assert s.flat_slp1() == "varaH"
    ids = _applied(s)
    assert "3.3.58" in ids and "7.3.84" in ids


def test_sanAtanaH():
    s = derive_sanAtanaH()
    assert s.flat_slp1() == "sanAtanaH"
    ids = _applied(s)
    assert "4.3.23" in ids and "7.1.1" in ids
