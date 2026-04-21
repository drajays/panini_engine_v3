"""
Regression tests against data/reference/subanta_gold/hari_pullinga.json.
"""
from __future__ import annotations

import pytest

from pipelines.subanta import derive
from phonology.joiner  import slp1_to_devanagari


_ALL_CELLS = [f"{v}-{vv}" for v in range(1, 9) for vv in range(1, 4)]


@pytest.mark.parametrize("cell", _ALL_CELLS)
def test_hari_cell_matches_gold(hari_gold, cell):
    v, vv = cell.split("-")
    state = derive("hari", int(v), int(vv))
    produced = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    gold = hari_gold["cells"][cell]["form_dev"]
    assert produced == gold, f"cell {cell}: produced {produced!r}, gold {gold!r}"

