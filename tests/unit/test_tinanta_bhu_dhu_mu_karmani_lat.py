"""
Karmaṇi laṭ ātmanepada — भू / धू / मू nine-cell paradigm (pedagogical set).

Gold surfaces from traditional grammar (शब्द-तुलना with भूवादि *ū*-roots).
"""
from __future__ import annotations

import pytest

from pipelines.tinanta import derive

# (purusha, vacana) → Devanāgarī
_BHU_KARMANI_LAT: dict[tuple[int, int], str] = {
    (3, 1): "भूयते",
    (3, 2): "भूयेते",
    (3, 3): "भूयन्ते",
    (2, 1): "भूयसे",
    (2, 2): "भूयेथे",
    (2, 3): "भूयध्वे",
    (1, 1): "भूये",
    (1, 2): "भूयावहे",
    (1, 3): "भूयामहे",
}

_DHU_KARMANI_LAT: dict[tuple[int, int], str] = {
    (3, 1): "धूयते",
    (3, 2): "धूयेते",
    (3, 3): "धूयन्ते",
    (2, 1): "धूयसे",
    (2, 2): "धूयेथे",
    (2, 3): "धूयध्वे",
    (1, 1): "धूये",
    (1, 2): "धूयावहे",
    (1, 3): "धूयामहे",
}

_MU_KARMANI_LAT: dict[tuple[int, int], str] = {
    (3, 1): "मूयते",
    (3, 2): "मूयेते",
    (3, 3): "मूयन्ते",
    (2, 1): "मूयसे",
    (2, 2): "मूयेथे",
    (2, 3): "मूयध्वे",
    (1, 1): "मूये",
    (1, 2): "मूयावहे",
    (1, 3): "मूयामहे",
}


@pytest.mark.parametrize(
    "dhatu,gold",
    [
        ("BU", _BHU_KARMANI_LAT),
        ("DU", _DHU_KARMANI_LAT),
        ("mU", _MU_KARMANI_LAT),
    ],
)
def test_karmani_lat_atmanepada_paradigm(dhatu: str, gold: dict[tuple[int, int], str]) -> None:
    for (purusha, vacana), expected in gold.items():
        s = derive(dhatu, "laT", "karmani", purusha, vacana)
        assert s.flat_dev() == expected, (
            f"{dhatu} karmani laT {purusha}/{vacana}: got {s.flat_dev()!r}, want {expected!r}"
        )


def test_karmani_lat_not_kartari_parasmaipada() -> None:
    """Kartari भू stays भवति, not karmaṇi भूयते."""
    assert derive("BU", "laT", "kartari", 3, 1).flat_dev() == "भवति"
    assert derive("BU", "laT", "karmani", 3, 1).flat_dev() == "भूयते"
