"""
tests/unit/test_sutra_type_contracts.py
─────────────────────────────────────────

Every SutraRecord in the registry honours its SUTRA_TYPE_CONTRACTS
entry.  We check:
  • SAMJNA / PARIBHASHA / VIDHI / NIYAMA / VIBHASHA have cond+act.
  • PRATISHEDHA has either blocks_sutra_ids or a cond+act, or both.
  • ADHIKARA has a well-formed scope tuple.
  • ATIDESHA has source, dest, target all set.
  • NIPATANA has nipatana_form_slp1 set.

SutraRecord.__post_init__ already enforces most of this; these tests
double-check at the registry level, after `sutras` import.
"""
from __future__ import annotations

import pytest

from engine import SUTRA_REGISTRY, SutraType
import sutras  # noqa: F401


def _by_type(t: SutraType):
    return [r for r in SUTRA_REGISTRY.values() if r.sutra_type is t]


def test_all_types_represented():
    present = {r.sutra_type for r in SUTRA_REGISTRY.values()}
    for t in SutraType:
        assert t in present, f"SutraType.{t.name} has no representative sūtra"


def test_samjna_has_cond_and_act():
    for r in _by_type(SutraType.SAMJNA):
        assert r.cond is not None, f"{r.sutra_id}: SAMJNA needs cond"
        assert r.act  is not None, f"{r.sutra_id}: SAMJNA needs act"


def test_paribhasha_has_cond_and_act():
    for r in _by_type(SutraType.PARIBHASHA):
        assert r.cond is not None
        assert r.act  is not None


def test_vidhi_has_cond_and_act():
    for r in _by_type(SutraType.VIDHI):
        assert r.cond is not None
        assert r.act  is not None


def test_niyama_has_cond_and_act():
    for r in _by_type(SutraType.NIYAMA):
        assert r.cond is not None
        assert r.act  is not None


def test_vibhasha_has_cond_and_act():
    for r in _by_type(SutraType.VIBHASHA):
        assert r.cond is not None
        assert r.act  is not None


def test_adhikara_has_scope():
    for r in _by_type(SutraType.ADHIKARA):
        start, end = r.adhikara_scope
        assert start and end, f"{r.sutra_id}: ADHIKARA needs non-empty scope"


def test_atidesha_has_triple():
    for r in _by_type(SutraType.ATIDESHA):
        assert r.atidesha_target
        assert r.atidesha_source
        assert r.atidesha_dest


def test_nipatana_has_form():
    for r in _by_type(SutraType.NIPATANA):
        assert r.nipatana_form_slp1, f"{r.sutra_id}: NIPATANA needs form"


def test_pratishedha_has_blocks_or_act():
    for r in _by_type(SutraType.PRATISHEDHA):
        assert r.blocks_sutra_ids or r.act is not None, (
            f"{r.sutra_id}: PRATISHEDHA must declare blocks or an act"
        )
