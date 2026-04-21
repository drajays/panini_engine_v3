"""
tests/conftest.py — pytest fixtures and engine bootstrap.
───────────────────────────────────────────────────────────

Imports `sutras` at session-start so every sūtra file self-registers
into engine.SUTRA_REGISTRY before any test runs.

Provides:
  fresh_state      — an empty State
  rama_stem_state  — State seeded with the 'rāma' prātipadika
  rama_gold        — loaded data/reference/subanta_gold/rama_pullinga.json
  hari_gold        — loaded data/reference/subanta_gold/hari_pullinga.json
  sarva_gold       — loaded data/reference/subanta_gold/sarva_pullinga.json
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
