"""
Regression tests against data/reference/subanta_gold/sarva_pullinga.json.
"""
from __future__ import annotations

import pytest

from phonology.joiner import slp1_to_devanagari
from pipelines.sarva_subanta import derive_sarva_pulliṅga, sarva_cell_key


_ALL_CELLS = [f"{v}-{vv}" for v in range(1, 9) for vv in range(1, 4)]


@pytest.mark.parametrize("cell", _ALL_CELLS)
def test_sarva_cell_matches_gold(sarva_gold, cell):
    v, vv = cell.split("-")
    state = derive_sarva_pulliṅga(int(v), int(vv))
    assert sarva_cell_key(int(v), int(vv)) == cell
    produced = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    gold = sarva_gold["cells"][cell]["form_dev"]
    assert produced == gold, f"cell {cell}: produced {produced!r}, gold {gold!r}"

