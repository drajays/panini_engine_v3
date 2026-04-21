"""
Regression tests against data/reference/subanta_gold/jnana_napumsaka.json.
"""
from __future__ import annotations

import pytest

from pipelines.subanta import derive
from phonology.joiner  import slp1_to_devanagari


_ALL_CELLS = [f"{v}-{vv}" for v in range(1, 9) for vv in range(1, 4)]


@pytest.mark.parametrize("cell", _ALL_CELLS)
def test_jnana_cell_matches_gold(jnana_gold, cell):
    v, vv = cell.split("-")
    state = derive("jYAna", int(v), int(vv), linga="napuṃsaka")
    produced = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    gold = jnana_gold["cells"][cell]["form_dev"]
    assert produced == gold, f"cell {cell}: produced {produced!r}, gold {gold!r}"

