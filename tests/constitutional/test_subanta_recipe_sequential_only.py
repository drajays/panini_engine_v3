"""
Subanta (declension): phase-ordered pools of ``apply_rule`` calls; **conflicts are
settled by ``engine.resolver``** (Art. 3 point 2 / Art. 21 Ladder 1), never by position
in a hand-written list and never inside a sūtra's ``cond`` (Art. 15). Policy change of
2026-10-03: this file used to forbid the resolver here; the ban is replaced by the
requirement below.

- ``pipelines.subanta`` obtains every multi-candidate winner of its scanner from ``engine.resolver``.
  (Debt: 6.1.97 still narrows itself for the *recipe* pipelines — Art. 15 — until tinanta/krdanta/
  taddhita are loop-driven; see docs/SUTRA_COVERAGE_100_PLAN.md.)
- The post-4.1.2 rule list is a single source of truth: ``SUBANTA_RULE_IDS_POST_4_1_2``
  in ``subanta.py`` and *must* match the sequence used in ``run_subanta_post_4_1_2``.
"""
from __future__ import annotations

import importlib
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[2]


def test_pipelines_subanta_conflicts_go_through_the_resolver():
    p = (ROOT / "pipelines" / "subanta.py").read_text(encoding="utf-8")
    assert "from engine.resolver import record_decision, resolve_with_reason" in p
    assert "min(candidates, key=lambda sid: order" not in p, "list position must not break ties"


def test_tinanta_jayati_gold_does_not_import_resolve():
    p = (ROOT / "tools" / "tinanta_jayati_gold.py").read_text(encoding="utf-8")
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
