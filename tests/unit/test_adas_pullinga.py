"""अदस् pulliṅga vs ashtadhyayi.com shabdaprakriya (8.2.80/81, 7.2.106/107, 7.1.11).

3-1 अमुना is a known gap: it needs 7.3.120 to run after 8.2.80, against the
Tripāḍī asiddha ordering the engine enforces.
"""
import pytest

import sutras  # noqa: F401
from pipelines.subanta import derive

GOLD = {
    (1, 1): "asO", (1, 2): "amU", (1, 3): "amI",
    (2, 1): "amum", (2, 2): "amU", (2, 3): "amUn",
    (3, 2): "amUByAm", (3, 3): "amIBiH",
    (4, 1): "amuzmE", (4, 2): "amUByAm", (4, 3): "amIByaH",
    (5, 1): "amuzmAt", (5, 2): "amUByAm", (5, 3): "amIByaH",
    (6, 1): "amuzya", (6, 2): "amuyoH", (6, 3): "amIzAm",
    (7, 1): "amuzmin", (7, 2): "amuyoH", (7, 3): "amIzu",
}


@pytest.mark.parametrize("cell", sorted(GOLD))
def test_adas_cell(cell):
    assert derive("adas", *cell, "pulliṅga").flat_slp1() == GOLD[cell]
