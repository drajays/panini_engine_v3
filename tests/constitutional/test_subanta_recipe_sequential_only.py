"""
Subanta (declension) pipeline is fixed Aṣṭādhyāyī-kram: ``apply_rule`` in a
recipe-determined order, not a Kaumudī/scheduler “tie-break” (CONSTITUTION Art.3).

- ``pipelines.subanta`` does not use ``engine.resolver`` / *rightmost-wins*
  autonomous disambiguation.
- The post-4.1.2 rule list is a single source of truth: ``SUBANTA_RULE_IDS_POST_4_1_2``
  in ``subanta.py`` and *must* match the sequence used in ``run_subanta_post_4_1_2``.
"""
from __future__ import annotations

import importlib
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[2]


def test_pipelines_subanta_never_imports_resolver():
    p = (ROOT / "pipelines" / "subanta.py").read_text(encoding="utf-8")
    for needle in ("from engine import resolver", "from engine.resolver", "import resolver", "resolve("):
        assert needle not in p, (
            f"pipelines/subanta.py must stay recipe-driven, not {needle!r}"
        )


def test_tinanta_jayati_gold_does_not_import_resolve():
    p = (ROOT / "pipelines" / "tinanta_jayati_gold.py").read_text(encoding="utf-8")
    assert "from engine.resolver" not in p
    assert "import engine.resolver" not in p


def test_subanta_post_4_1_2_list_has_pada_merge_once():
    sm = importlib.import_module("pipelines.subanta")
    t = sm.SUBANTA_RULE_IDS_POST_4_1_2
    assert t.count(sm.PADA_MERGE_STEP) == 1, "pada merge must be scheduled exactly once"


def test_enumerate_candidates_is_sorted_ascending():
    """If autonomous mode is used, candidates must be in numeric id order (v3.0 invariants)."""
    from engine.scheduler import enumerate_candidates
    from engine.state import State, Term
    from phonology import mk
    s = State(terms=[Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})])
    a = enumerate_candidates(s)
    def key(sid: str) -> tuple[int, int, int]:
        p = sid.split(".")
        return int(p[0]), int(p[1]), int(p[2])
    assert a == sorted(a, key=key)
