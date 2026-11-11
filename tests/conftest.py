"""
tests/conftest.py — pytest fixtures and engine bootstrap.
───────────────────────────────────────────────────────────

Imports `sutras` at session-start so every sūtra file self-registers
into engine.SUTRA_REGISTRY before any test runs.

Provides:
  fresh_state      — an empty State
  rama_stem_state  — State seeded with the 'rāma' prātipadika
  rama_gold        — loaded data/reference/subanta_gold/rama_pullinga.json
  rADA_strI_gold   — loaded data/reference/subanta_gold/rADA_strilinga.json
  hari_gold        — loaded data/reference/subanta_gold/hari_pullinga.json
  sarva_gold       — loaded data/reference/subanta_gold/sarva_pullinga.json
  anya_gold        — loaded data/reference/subanta_gold/anya_pullinga.json
  jnana_gold       — loaded data/reference/subanta_gold/jnana_napumsaka.json
  tad_gold         — loaded data/reference/subanta_gold/tad_pullinga.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

# Make the repo root importable.
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

# Load all sūtras.
import sutras  # noqa: F401  (side-effect: fills SUTRA_REGISTRY)

from engine          import SUTRA_REGISTRY, State, Term
from phonology       import mk
from phonology.varna import mk_inherent_a


@pytest.fixture
def fresh_state():
    return State()


@pytest.fixture
def rama_stem_state():
    # r a m a
    varnas = [mk("r"), mk_inherent_a(), mk("m"), mk_inherent_a()]
    stem = Term(
        kind   = "prakriti",
        varnas = varnas,
        tags   = {"prātipadika", "anga", "upadesha"},
        meta   = {"upadesha_slp1": "rAma"},
    )
    s = State(terms=[stem])
    s.meta["linga"] = "pulliṅga"
    return s


@pytest.fixture(scope="session")
def rama_gold():
    path = _ROOT / "data" / "reference" / "subanta_gold" / "rama_pullinga.json"
    with path.open(encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def rADA_strI_gold():
    path = _ROOT / "data" / "reference" / "subanta_gold" / "rADA_strilinga.json"
    with path.open(encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def hari_gold():
    path = _ROOT / "data" / "reference" / "subanta_gold" / "hari_pullinga.json"
    with path.open(encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def sarva_gold():
    path = _ROOT / "data" / "reference" / "subanta_gold" / "sarva_pullinga.json"
    with path.open(encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def anya_gold():
    path = _ROOT / "data" / "reference" / "subanta_gold" / "anya_pullinga.json"
    with path.open(encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def jnana_gold():
    path = _ROOT / "data" / "reference" / "subanta_gold" / "jnana_napumsaka.json"
    with path.open(encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def tad_gold():
    path = _ROOT / "data" / "reference" / "subanta_gold" / "tad_pullinga.json"
    with path.open(encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def all_sutra_ids():
    return sorted(SUTRA_REGISTRY.keys(),
                  key=lambda s: tuple(int(p) for p in s.split(".")))


# ── speed tiers ─────────────────────────────────────────────────────────────
# A full run is hours because a few thousand tests each run whole derivations. Tiers keep the proof (everything) and
# the loop (the fast majority) apart:
#     pytest -n8 --tier=fast tests/      # skips tests recorded as ≥ --slow-secs (default 5 s); unknown tests run
#     pytest -n8 --tier=slow tests/      # only those
#     pytest -n8 --record-durations tests/   # (re)writes sig/test_durations.json — do this on every full run
# Nothing is deselected unless sig/test_durations.json measured it slow, so a new test is always in the fast tier.
_DUR_PATH = _ROOT / "sig" / "test_durations.json"
_DUR: dict[str, float] = {}


def pytest_addoption(parser):
    g = parser.getgroup("tiers")
    g.addoption("--tier", choices=("fast", "slow"), default=None, help="run only the fast or only the slow tier")
    g.addoption("--slow-secs", type=float, default=5.0, help="a test measured at least this long is 'slow'")
    g.addoption("--record-durations", action="store_true", help="merge measured call times into sig/test_durations.json")


def pytest_collection_modifyitems(config, items):
    tier = config.getoption("--tier")
    if not tier or not _DUR_PATH.exists():
        return
    known = json.loads(_DUR_PATH.read_text(encoding="utf-8"))
    cut = config.getoption("--slow-secs")
    keep, drop = [], []
    for it in items:
        slow = known.get(it.nodeid, 0.0) >= cut
        (keep if slow == (tier == "slow") else drop).append(it)
    if drop:
        config.hook.pytest_deselected(items=drop)
        items[:] = keep


def pytest_runtest_logreport(report):
    if report.when == "call":
        _DUR[report.nodeid] = round(report.duration, 2)


def pytest_sessionfinish(session, exitstatus):
    cfg = session.config
    if hasattr(cfg, "workerinput") or not cfg.getoption("--record-durations") or not _DUR:
        return
    old = json.loads(_DUR_PATH.read_text(encoding="utf-8")) if _DUR_PATH.exists() else {}
    old.update(_DUR)
    _DUR_PATH.write_text(json.dumps(dict(sorted(old.items())), indent=0) + "\n", encoding="utf-8")
