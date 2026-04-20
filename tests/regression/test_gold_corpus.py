"""
tests/regression/test_gold_corpus.py
──────────────────────────────────────

Regression tests against data/reference/subanta_gold/rama_pullinga.json.

v3.2 status: 19 of 24 cells match gold.  Still-failing cells are
explicitly noted with the specific sūtra that needs implementing.
When a new sūtra flips an xfail cell to green, move it from
_XFAIL_CELLS to _PASSING_CELLS.
"""
from __future__ import annotations

import pytest

from pipelines.subanta import derive
from phonology.joiner  import slp1_to_devanagari


# Cells that produce the exact gold form — 19 of 24.
_PASSING_CELLS = [
    "1-1", "1-2",
    "2-1", "2-2",
    "3-1", "3-2",
    "4-1", "4-2", "4-3",
    "5-1", "5-2", "5-3",
    "6-1", "6-2", "6-3",
    "7-1", "7-2",
    "8-1", "8-2",
]


# Cells that do NOT yet match gold.  Each carries a note about the
# missing sūtra(s).  Move to _PASSING_CELLS when the fix lands.
_XFAIL_CELLS = {
    "1-3": "jas pratyaya substitution (→ās) not yet implemented",
    "2-3": "Sas pratyaya substitution (→ān) not yet implemented",
    "3-3": "a+Bis → E (vṛddhi) pathway needs a narrow override",
    "7-3": "ṣatva (s → ṣ after i/e) — 8.3.59 not yet implemented",
    "8-3": "jas pratyaya substitution (same as 1-3)",
}


@pytest.mark.parametrize("cell", _PASSING_CELLS)
def test_rama_cell_matches_gold(rama_gold, cell):
    v, vv = cell.split("-")
    state = derive("rAma", int(v), int(vv))
    produced = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    gold = rama_gold["cells"][cell]["form_dev"]
    assert produced == gold, f"cell {cell}: produced {produced!r}, gold {gold!r}"


@pytest.mark.parametrize("cell,note", list(_XFAIL_CELLS.items()))
def test_rama_cell_known_gap(rama_gold, cell, note):
    """Document the 5 known gaps. xfail until rules are added."""
    v, vv = cell.split("-")
    state = derive("rAma", int(v), int(vv))
    produced = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    gold = rama_gold["cells"][cell]["form_dev"]
    if produced == gold:
        return  # cell secretly works — consider moving it to _PASSING_CELLS
    pytest.xfail(f"cell {cell}: {note} — got {produced!r}, expected {gold!r}")
