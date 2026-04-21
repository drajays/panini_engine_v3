"""
Regression tests against data/reference/subanta_gold/tad_pullinga.json.

Note: tyadādi pronouns have no sambodhana (no 8-* cells).
"""
from __future__ import annotations

import pytest

from pipelines.subanta import derive
from phonology.joiner  import slp1_to_devanagari


_CELLS = [f"{v}-{vv}" for v in range(1, 8) for vv in range(1, 4)]


@pytest.mark.parametrize("cell", _CELLS)
def test_tad_cell_matches_gold(tad_gold, cell):
    v, vv = cell.split("-")
    state = derive("tad", int(v), int(vv), linga="pulliṅga")
    produced = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    gold = tad_gold["cells"][cell]["form_dev"]
    assert produced == gold, f"cell {cell}: produced {produced!r}, gold {gold!r}"


def test_tad_has_no_sambodhana():
    with pytest.raises(ValueError):
        derive("tad", 8, 1, linga="pulliṅga")

