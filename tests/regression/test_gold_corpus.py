"""
tests/regression/test_gold_corpus.py
──────────────────────────────────────

Regression tests against data/reference/subanta_gold/rama_pullinga.json.

v3.3 status: ALL 24 of 24 cells match classical gold.
"""
from __future__ import annotations

import pytest

from pipelines.subanta import derive
from phonology.joiner  import slp1_to_devanagari


_ALL_CELLS = [f"{v}-{vv}" for v in range(1, 9) for vv in range(1, 4)]


@pytest.mark.parametrize("cell", _ALL_CELLS)
def test_rama_cell_matches_gold(rama_gold, cell):
    v, vv = cell.split("-")
    state = derive("rAma", int(v), int(vv))
    produced = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    gold = rama_gold["cells"][cell]["form_dev"]
    assert produced == gold, f"cell {cell}: produced {produced!r}, gold {gold!r}"
