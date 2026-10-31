"""Scharf 2022 review of Rajpopat: the counter-derivations (papers/DEEP_scharf_krishnan.md, A1-A6). Passing cases are ordinary
tests; A1 (bhavya from root as) is a strict xfail with its cause."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta
from pipelines.subanta import derive as subanta
from pipelines.tinanta import derive as tinanta


def test_bhavanti():
    assert tinanta("BU", "laT", "kartari", 3, 3).flat_slp1() == "Bavanti"


@pytest.mark.parametrize("stem", ["ajA", "aja"])
def test_ajabhih(stem):
    assert subanta(stem, 3, 3, "strīliṅga").flat_slp1() == "ajABiH"


def test_trayanam():
    assert subanta("tri", 6, 3, "pulliṅga").flat_slp1() == "trayARAm"


def test_edhante():
    assert tinanta("eDa~", "laT", "kartari", 3, 3).flat_slp1() == "eDante"


def test_cetati():
    assert tinanta("citI~", "laT", "kartari", 3, 1).flat_slp1() == "cetati"


def _bhavya_readings():
    return {b.surface_slp1 for b in explore(lambda: derive_krdanta("Adadi_02_0060", 1, 1, "napuṃsaka", krt="kftya"))}


def test_bhavya_from_as():
    assert "Bavyam" in _bhavya_readings()


def test_asya_not_derived():
    """Rajpopat's *Asya (from as + ṇyat) must not be derived either."""
    assert "Asyam" not in _bhavya_readings()
