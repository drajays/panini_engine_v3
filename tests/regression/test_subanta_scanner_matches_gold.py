"""The resolver-driven subanta scanner (``derive(..., autonomous_scanner=True)``) reproduces every cell
of every vendored paradigm: no hand-written list breaks a tie, the whole tripāḍī is the pool, and the
Ladder-1 layers (apavāda → antaraṅga → para) settle contention (ROADMAP C2/C4).

Default stays the recipe until the trace-shape tests that pin it are regenerated together
(docs/SUTRA_COVERAGE_100_PLAN.md, "subanta flip")."""
import glob
import json

import pytest

import sutras  # noqa: F401
from pipelines.subanta import derive

GOLD = sorted(glob.glob("data/reference/shabda_gold/*.json"))


@pytest.mark.parametrize("path", GOLD, ids=lambda p: p.split("/")[-1].split("_")[0])
def test_scanner_reproduces_every_attested_cell(path):
    with open(path, encoding="utf-8") as fp:
        data = json.load(fp)
    wrong = []
    for cell, forms in data["cells"].items():
        vibhakti, vacana = map(int, cell.split("-"))
        got = derive(data["stem_slp1"], vibhakti, vacana, linga=data["linga"], autonomous_scanner=True).flat_dev()
        if got not in forms:
            wrong.append((cell, got, forms))
    assert not wrong, wrong
