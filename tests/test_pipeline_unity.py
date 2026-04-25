"""
Pipeline unity: *śālīya* / *mālīya* / subanta *spine* come from
``core.canonical_pipelines``; ``engine.resolver`` is the *only* multi-rule
arbitration path (structural *asiddha* / *pratiṣedha* / *rajpopat*).
"""
from __future__ import annotations

import inspect
from pathlib import Path

import sutras  # noqa: F401

from core import canonical_pipelines as cp
from pipelines import subanta
from pipelines import taddhita_salIya as ts


def test_taddhita_salIya_reexports_from_core() -> None:
    for name in (
        "build_salIya_initial_state",
        "build_malIya_initial_state",
        "derive_salIya",
        "derive_mAlIya",
        "derive_salIyaH",
    ):
        assert getattr(ts, name) is getattr(cp, name)


def test_taddhita_module_has_no_apply_rule() -> None:
    src = Path(ts.__file__).read_text(encoding="utf-8")
    assert "apply_rule" not in src
    assert "SutraRecord" not in src


def test_salIya_mAlIya_same_sutra_spine() -> None:
    a, b = cp.derive_salIya(), cp.derive_mAlIya()
    sida = [x.get("sutra_id") for x in a.trace]
    sidb = [x.get("sutra_id") for x in b.trace]
    assert sida == sidb
    assert a.flat_slp1() == "SAlIya" and b.flat_slp1() == "mAlIya"


def test_subanta_post_sourced_from_core() -> None:
    import core.canonical_pipelines as ccp
    assert subanta.subanta_post_4_1_2 is ccp.subanta_post_4_1_2
    assert "canonical_pipelines" in (subanta.run_subanta_pipeline.__doc__ or "")


def test_p13_14_15_exhausts_post_4_1_2() -> None:
    t = subanta.SUBANTA_RULE_IDS_POST_4_1_2
    i0 = t.index("8.2.1")
    a = t[:i0]
    b = t[i0 : i0 + 3]
    c = t[i0 + 3 :]
    # Canonical split must match the full tuple
    assert tuple(a) + tuple(b) + tuple(c) == t


def test_no_second_resolver_in_canonical() -> None:
    src = inspect.getsource(cp)
    assert "def resolve" not in src
    assert "UnresolvedConflict" not in src
