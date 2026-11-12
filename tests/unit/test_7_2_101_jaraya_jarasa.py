"""7.2.101 jarAyA jarasanyatarasyAm — jarA may become jaras before a vowel-initial vibhakti (vA); not before bhyAm / su."""
import pytest
from engine.vikalpa import explore
from pipelines.subanta import derive


def _forms(v, n):
    return {b.surface_slp1 for b in explore(lambda: derive("jarA", v, n, "strīliṅga"))}


@pytest.mark.parametrize("v,n,both", [
    (3, 1, {"jarasA", "jarayA"}), (4, 1, {"jarase", "jarAyE"}), (1, 2, {"jarasO", "jare"}), (6, 3, {"jarasAm", "jarARAm"}),
])
def test_both_readings(v, n, both):
    assert both <= _forms(v, n)


def test_not_before_a_consonant():
    assert not any(f.startswith("jaras") for f in _forms(3, 2))       # jarAByAm only
