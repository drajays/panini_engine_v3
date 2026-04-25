"""
tests/backward/test_replay_integrity.py
─────────────────────────────────────────

Constitution Article 9 — Backward testability.

Given a forward derivation's trace, re-apply each APPLIED sūtra step
from the initial state and assert the final rendered form equals the
one originally recorded.  This catches:

  • engine paths that mutate state outside apply_rule()
  • trace rows whose form_after lies
  • non-deterministic sūtras (cond() reading hidden globals)
"""
from __future__ import annotations

import pytest

from engine             import apply_rule
from engine.sig         import replay_subanta_trace
from pipelines.subanta  import derive, build_initial_state


def test_replay_subanta_trace_matches_full_derive():
    """Trace replay (including merge) is bitwise identical to a single ``derive``."""
    s = derive("rAma", 3, 2)
    r = replay_subanta_trace("rAma", 3, 2, s.trace)
    assert r.render() == s.render()
    s2 = derive("hari", 1, 1)
    r2 = replay_subanta_trace("hari", 1, 1, s2.trace)
    assert r2.render() == s2.render()


def test_dik_samasa_compound_path_is_deterministic():
    """
    Dik *uttarapūrvā* demo: internal *sup* **luk** (2.4.71) and the second
    **2.1.3** bookkeeping step are engine-specific; a naïve ``apply_rule`` re-run
    from the initial vigraha is not required to match (state/meta differ). We
    still require **forward** runs to be deterministic and surface-identical.
    """
    from pipelines.dik_uttarapurva_demo import caturthi_preset, derive_dik_caturthi_compound

    p = caturthi_preset("uttarA_pUrvA")
    a = derive_dik_caturthi_compound(p, verbose=False)
    b = derive_dik_caturthi_compound(p, verbose=False)
    assert a.render() == b.render() and a.flat_slp1() == b.flat_slp1()
    assert [st["sutra_id"] for st in a.trace] == [st["sutra_id"] for st in b.trace]

@pytest.mark.parametrize("v,vv", [(1, 1), (2, 1), (4, 1), (6, 3), (7, 3)])
def test_forward_is_deterministic(v, vv):
    """Running derive twice yields identical final forms and traces."""
    s1 = derive("rAma", v, vv)
    s2 = derive("rAma", v, vv)
    assert s1.render() == s2.render()
    assert len(s1.trace) == len(s2.trace)
    for a, b in zip(s1.trace, s2.trace):
        assert a["sutra_id"]   == b["sutra_id"]
        assert a["form_before"] == b["form_before"]
        assert a["form_after"]  == b["form_after"]


@pytest.mark.parametrize("v,vv", [(1, 1), (4, 1), (6, 3)])
def test_replay_applied_steps_reaches_same_form(v, vv):
    """
    Take the APPLIED sūtra ids from the trace (skipping __MERGE__ and
    SKIPPED rows), re-apply them from the initial state, and compare.

    v3.2 fix: only replay steps BEFORE __MERGE__ — post-merge steps
    (tripāḍī, ṇatva) operate on a merged-pada-tagged Term structure
    that fresh_state + apply_rule cannot reproduce without the merge
    itself.  So we compare pre-merge state against pre-merge replay.
    """
    original = derive("rAma", v, vv)

    # Find __MERGE__ index.
    merge_idx = next(
        (i for i, st in enumerate(original.trace) if st["sutra_id"] == "__MERGE__"),
        None,
    )
    from engine.trace import TRACE_STATUSES_FIRED

    # Pre-merge fired sūtras (APPLIED / APPLIED_VACUOUS / AUDIT).
    pre_merge_trace = (original.trace[:merge_idx]
                       if merge_idx is not None
                       else original.trace)
    applied_ids = [
        step["sutra_id"]
        for step in pre_merge_trace
        if step.get("status") in TRACE_STATUSES_FIRED
        and not step["sutra_id"].startswith("__")
    ]
    replayed = build_initial_state("rAma", v, vv)
    for sid in applied_ids:
        replayed = apply_rule(sid, replayed)

    if merge_idx is not None:
        expected_before_merge = original.trace[merge_idx]["form_before"]
        assert replayed.render() == expected_before_merge, (
            f"replay divergence for ({v},{vv}): "
            f"got {replayed.render()!r}, expected {expected_before_merge!r}"
        )
    else:
        assert replayed.render() == original.render()
