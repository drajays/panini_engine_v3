"""
tests/unit/test_prakriya_audit.py — guardrails for *prakriyā* (derivation) policy.

Failing tests here mean: registry corruption, pathway drift, or preflight
helper mismatch — not necessarily individual *sūtra* bugs (see feature tests).
"""
from __future__ import annotations

import re

import pytest

import sutras  # noqa: F401  (load registry)
from engine.gates         import asiddha_violates, is_blocked
from engine.registry      import SUTRA_REGISTRY, register_sutra
from engine.state         import State, Term
from pipelines.preflight_lopa_samjna import (
    PREFLIGHT_LOPA_LUK_1_1_6X,
    apply_preflight_luk_samjna_block,
)
from pipelines.subanta    import (
    META_SALIYA_TADDHITA_SUBANTA_CONTINUATION,
    build_initial_state,
    run_subanta_pipeline,
)


def test_sutra_registry_unique_ids_enforced() -> None:
    """`register_sutra` must reject a second `sutra_id` (one file per sūtra)."""
    with pytest.raises(ValueError, match="duplicate"):
        register_sutra(SUTRA_REGISTRY["1.1.1"])


def test_all_registry_ids_match_one_sutra_file() -> None:
    """Every key in SUTRA_REGISTRY is `d.d.d` and should map to one module path (heuristic)."""
    assert SUTRA_REGISTRY, "registry empty after import sutras"
    for sid in SUTRA_REGISTRY:
        assert re.match(r"^\d+\.\d+\.\d+$", sid), f"non-standard id: {sid!r}"


def test_preflight_luk_block_matches_subanta_sequence() -> None:
    """Shared preflight tuple is the canonical 1.1.60–1.1.63 order."""
    assert PREFLIGHT_LOPA_LUK_1_1_6X == (
        "1.1.60", "1.1.61", "1.1.62", "1.1.63",
    )


def test_apply_preflight_luk_block_round_trip() -> None:
    """`apply_preflight_luk_samjna_block` actually exercises the four sūtra ids."""
    s0 = build_initial_state("rAma", 1, 1, "pulliṅga")
    s0 = apply_preflight_luk_samjna_block(s0)
    tail = [x.get("sutra_id") for x in s0.trace[-4:]]
    assert tail == list(PREFLIGHT_LOPA_LUK_1_1_6X)


def test_salIya_continuation_skips_preflight_luk_in_subanta() -> None:
    """`derive_salIyaH` path must not double-schedule 1.1.60–1.1.63 in subanta preflight."""
    s = build_initial_state("SAlIya", 1, 1, "pulliṅga")
    s.meta[META_SALIYA_TADDHITA_SUBANTA_CONTINUATION] = True
    s1 = run_subanta_pipeline(s)
    pre_42 = [x.get("sutra_id") for x in s1.trace if x.get("sutra_id") == "4.1.2"]
    assert pre_42, "4.1.2 should run"
    idx_42 = next(i for i, t in enumerate(s1.trace) if t.get("sutra_id") == "4.1.2")
    pre_ids = {t.get("sutra_id") for t in s1.trace[:idx_42]}
    for sid in PREFLIGHT_LOPA_LUK_1_1_6X:
        assert sid not in pre_ids, f"unexpected preflight {sid} when salIya continuation"


def test_gates_module_exports_conflict_checks() -> None:
    s = State(terms=[Term(kind="pada", varnas=[], tags=set(), meta={})])
    s.tripadi_zone = True
    # In Tripāḍī zone: non-Tripāḍī sūtra is asiddha; Tripāḍī sūtra is allowed.
    assert asiddha_violates("8.2.7", s) is False
    assert asiddha_violates("1.1.1", s) is True
    assert is_blocked("0.0.0", s) is False


def test_structural_merge_id_not_in_registry() -> None:
    assert "__MERGE__" not in SUTRA_REGISTRY


def test_subanta_entry_derive_uses_apply_rule() -> None:
    """Light smoke: public subanta `derive` completes for rAma 1-1 (single surface path)."""
    from pipelines.subanta import derive

    s = derive("rAma", 1, 1)
    assert s.flat_slp1()
    assert any(
        t.get("sutra_id") == "4.1.2" for t in s.trace
    )
