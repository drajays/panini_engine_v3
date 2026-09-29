"""
tests/regression/test_samsaadhanii_gita_tinanta.py
──────────────────────────────────────────────────

Every tiṅanta of the Bhagavad Gītā, as tagged by Saṃsādhanī (source #17,
Tier-4 oracle), is fed to ``pipelines.tinanta.derive`` with the tagged
dhātu / lakāra / prayoga / puruṣa / vacana / pada / upasargas. The cells the
engine already derives exactly are locked in
``samsaadhanii_gita_tinanta_baseline.json``; this test keeps them derived.

Progress: ``python3 -m tools.samsaadhanii_coverage --write-baseline`` after a
fix grows the list. Snapshot: ``python3 -m tools.fetch_samsaadhanii_ereaders``.
"""
from __future__ import annotations

import pytest

from tools.samsaadhanii_coverage import derive_cell, load_baseline, load_cells
from tools.samsaadhanii_tags import parse_tinanta_tag

_CELLS = {c.cell_id: c for c in load_cells()}
_BASELINE = load_baseline()


def test_snapshot_tags_mostly_resolve_to_engine_inputs():
    rows = list(_CELLS.values())
    resolved = [c for c in rows if not c.row["unresolved"]]
    assert len(resolved) / len(rows) >= 0.9, (
        f"only {len(resolved)}/{len(rows)} Saṃsādhanī tags map to derive() inputs"
    )


def test_tag_parser_reads_upasarga_pada_and_gana():
    c = parse_tinanta_tag("अभि_हन्1{कर्मणि;लङ्;प्र;बहु;आत्मनेपदी;अभि_हनँ;अदादिः}")
    assert (c.dhatu_upadesha_slp1, c.gana, c.upasargas) == ("hana~", 2, ["aBi"])
    assert (c.prayoga, c.lakara, c.purusha, c.vacana, c.pada) == ("karmani", "laG", 3, 3, "atmane")
    assert c.unresolved is None


@pytest.mark.parametrize("cell_id", _BASELINE)
def test_locked_gita_tinanta_still_derives(cell_id):
    cell = _CELLS.get(cell_id)
    assert cell is not None, f"{cell_id} vanished from the snapshot — rebuild the baseline"
    produced = derive_cell(cell.row).flat_slp1()
    assert produced == cell.word_slp1, (
        f"{cell.word} [{', '.join(cell.refs[:3])}]: produced {produced!r}, "
        f"attested {cell.word_slp1!r} ({cell.row['tag']})"
    )
