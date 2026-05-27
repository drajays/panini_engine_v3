"""
Smoke + gold spot-checks: भू × 10 lakāras × 9 cells (kartari parasmaipada).

Ensures the all-lakāra Web UI grid (/tinanta/all) has no regressions on the
canonical bhvādi spine.
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive

_LAKARAS = (
    "laT", "liT", "luT", "lRT", "loT", "laG", "liG", "AsIrliG", "luG", "lRG",
)

# Spot-check 3sg (full paradigms covered in per-lakāra test modules).
_BHU_KARTARI_3SG = {
    "laT": "भवति",
    "liT": "बभूव",
    "luT": "भविता",
    "lRT": "भविष्यति",
    "loT": "भवतु",
    "laG": "अभवत्",
    "liG": "भवेत्",
    "AsIrliG": "भूयात्",
    "luG": "अभूत्",
    "lRG": "अभविष्यत्",
}


@pytest.mark.parametrize("lakara", _LAKARAS)
def test_bhu_kartari_all_lakaras_9_cells_non_empty(lakara: str) -> None:
    for purusha in (3, 2, 1):
        for vacana in (1, 2, 3):
            state = derive("BU", lakara, "kartari", purusha, vacana)
            assert state.flat_dev(), f"empty surface {lakara} {purusha}-{vacana}"


@pytest.mark.parametrize("lakara,expected", list(_BHU_KARTARI_3SG.items()))
def test_bhu_kartari_3sg_gold(lakara: str, expected: str) -> None:
    assert derive("BU", lakara, "kartari", 3, 1).flat_dev() == expected


@pytest.mark.parametrize("lakara", _LAKARAS)
def test_bhu_karmani_lrg_no_not_implemented(lakara: str) -> None:
    if lakara != "lRG":
        return
    assert derive("BU", "lRG", "karmani", 3, 1).flat_dev() == "अभाविष्यते"
