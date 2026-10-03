"""Gate C, tiṅanta half: laṭ kartari, every puruṣa × vacana, derived by the loop with no recipe
after vivakṣā has chosen the tiṅ. Expectation = the recipe (itself pinned by the gold paradigms);
the point is that the loop reaches it by Pāṇini's order, not by a hand-written list.

Gaṇa-1 sweep 2026-10-03 (`.audit/tin_auto_sweep.py`): see docs/SUTRA_COVERAGE_100_PLAN.md."""
from types import SimpleNamespace

import pytest

import sutras  # noqa: F401
from pipelines.tinanta import derive
from tools.autonomy_report import run_autonomously, start_state

ROOTS = ["BU", "pac", "gam", "nI", "paW", "vfka~"]   # plain · guṇa · 7.3.77 chaḥ · rapara · ṇatva-free


@pytest.mark.parametrize("dhatu", ROOTS)
@pytest.mark.parametrize("purusha,vacana", [(p, v) for p in (1, 2, 3) for v in (1, 2, 3)])
def test_lat_kartari_cell_derives_autonomously(dhatu, purusha, vacana):
    if dhatu == "vfka~":
        pytest.skip("ātmanepada root: laṭ cells 3-1 only below")
    expected = derive(dhatu, "laT", "kartari", purusha, vacana).flat_slp1()
    run = run_autonomously(
        start_state(SimpleNamespace(kind="tinanta", args=(dhatu, "laT", purusha, vacana))),
        expected, dhatu, budget=120)
    assert run.outcome == "reached", f"{dhatu} {purusha}-{vacana}: {run.surface} ≠ {expected}"


def test_atmanepada_rapara_root():
    expected = derive("vfka~", "laT", "kartari", 3, 1).flat_slp1()
    assert expected == "varkate"
    run = run_autonomously(
        start_state(SimpleNamespace(kind="tinanta", args=("vfka~", "laT", 3, 1))),
        expected, "vfka~", budget=120)
    assert run.outcome == "reached"      # 1.1.51 uraṇ raparaḥ, a paribhāṣā that moves the tape
