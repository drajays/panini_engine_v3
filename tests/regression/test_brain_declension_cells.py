"""Declension cells of ashtadhyayi.com's own prakriyās (brain: derivations kind='subanta', docs/data/subanta_gauge.json) for the stems
whose rules this batch wrote: 7.1.84 · 7.1.90 · 7.1.92 · 7.1.93 · 7.2.85 · 7.2.115 (non-dhātu aṅga) · 7.3.118 · 6.1.93 · 6.1.110 ·
6.1.112 · 6.1.131 · 6.4.77 · 6.4.79 · 6.4.80 · 6.4.82 · 6.4.83 · 6.4.84 · 6.4.85. A cell passes when the engine's form (any
liṅga, any वा branch) is the brain's — the brain is the reference (AGENTS.md), Vidyut only a validator."""
import json
import pathlib

import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.subanta import derive

CELLS = json.loads((pathlib.Path(__file__).parent / "data" / "brain_declension_cells.json").read_text(encoding="utf-8"))
LINGA = ("pulliṅga", "strīliṅga", "napuṃsaka")


@pytest.mark.parametrize("stem,vib,vac,want", CELLS, ids=[f"{c[0]}-{c[1]}-{c[2]}-{c[3]}" for c in CELLS])
def test_brain_cell(stem, vib, vac, want):
    got = set()
    for lg in LINGA:
        try:
            got |= {b.surface_slp1 for b in explore(lambda: derive(stem, vib, vac, linga=lg))}
        except Exception:
            continue
    assert want in got, sorted(got)[:6]


def test_6_4_85_blocks_yan_for_bhu_and_sudhi():
    """na bhūsudhiyoḥ: svayambhuvaḥ (uvaṅ), not *svayambhvaḥ — 6.4.85 is BLOCKED-by-name on 6.4.82 / 6.4.83."""
    s = derive("svaBU", 1, 3, linga="pulliṅga")          # sva + bhū: anekāc and asaṃyogapūrva, so 6.4.83 would give *svabhvaḥ
    assert s.flat_slp1() == "svaBuvaH"
    assert {"6.4.82", "6.4.83"} <= s.blocked_sutras
    assert any(r["sutra_id"] == "6.4.83" and r["status"] == "BLOCKED" for r in s.trace)
