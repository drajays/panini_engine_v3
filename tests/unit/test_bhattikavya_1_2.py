"""Bhaṭṭikāvya 1.2 (जयमङ्गला) — nine padāni, engine-derived."""
from __future__ import annotations

from pipelines.bhattikavya_1_1 import (
    derive_aDyEzwa,
    derive_apArIt,
    derive_araMsta,
    derive_ayazwa,
    derive_nyavaDIt,
    derive_samamaMsta,
    derive_samUlaGAtam,
    derive_vedAH,
    derive_vyajezwa,
)


def _applied(s):
    return [x["sutra_id"] for x in s.trace if x.get("status") == "APPLIED" and x.get("sutra_id")]


def test_vedAH():
    s = derive_vedAH()
    assert s.flat_slp1() in {"vedAH", "vedAH"}
    assert s.flat_slp1() == "vedAH"
    assert "3.1.134" in _applied(s)
    assert "7.3.86" in _applied(s)


def test_aDyEzwa():
    s = derive_aDyEzwa()
    assert s.flat_slp1() == "aDyEzwa"
    ids = _applied(s)
    assert "6.4.72" in ids and "6.1.90" in ids


def test_ayazwa():
    s = derive_ayazwa()
    assert s.flat_slp1() == "ayazwa"
    ids = _applied(s)
    assert "8.2.36" in ids and "8.2.26" in ids


def test_apArIt():
    s = derive_apArIt()
    assert s.flat_slp1() == "apArIt"
    assert "7.2.1" in _applied(s)


def test_samamaMsta():
    s = derive_samamaMsta()
    assert s.flat_slp1() in {"samamaMsta", "samamansta"}
    assert "7.2.10" in _applied(s)


def test_vyajezwa():
    s = derive_vyajezwa()
    assert s.flat_slp1() == "vyajezwa"
    assert "1.3.19" in _applied(s)


def test_araMsta():
    s = derive_araMsta()
    assert s.flat_slp1() == "araMsta"
    # रम्'s म् before स् is apadānta: 8.3.24 (Kāśikā आक्रंस्यते), not 8.3.23.
    assert "8.3.24" in _applied(s)


def test_samUlaGAtam():
    s = derive_samUlaGAtam()
    assert s.flat_slp1() == "samUlaGAtam"
    ids = _applied(s)
    assert "3.4.36" in ids and "7.3.54" in ids and "7.3.32" in ids


def test_nyavaDIt():
    s = derive_nyavaDIt()
    assert s.flat_slp1() == "nyavaDIt"
    ids = _applied(s)
    assert "2.4.43" in ids and "6.4.48" in ids
    assert "8.2.28" in ids and "6.1.77" in ids
