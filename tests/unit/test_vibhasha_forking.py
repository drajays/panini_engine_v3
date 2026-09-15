"""
tests/unit/test_vibhasha_forking.py — Phase 3: Vibhāṣā Fork Manager isolation tests.

Verifies:
  1. state.fork() produces a deep-isolated copy (tape and meta mutations don't bleed).
  2. exec_vibhasha stores a real State object (the declined branch) in vibhasha_forks.
  3. The primary derivation and the fork diverge independently.
"""
from __future__ import annotations

import sutras  # noqa: F401

import pytest

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _make_lyap_term_with_m() -> Term:
    """Build a lyap pratyaya with an inserted m: l+m+y+a+p."""
    from phonology import mk
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("lyap")),
        tags={"pratyaya", "krt"},
        meta={"upadesha_slp1": "lyap"},
    )
    for i, v in enumerate(pr.varnas):
        if v.slp1 == "l":
            pr.varnas.insert(i + 1, mk("m"))
            break
    return pr


class TestForkTapeIsolation:
    def test_mutating_primary_varnas_does_not_affect_fork(self):
        s = State(terms=[_make_lyap_term_with_m()], meta={}, trace=[])
        fork = s.fork()

        fork_slp1_before = fork.flat_slp1()

        # Mutate primary tape
        s.terms[0].varnas.pop(1)  # remove the m

        fork_slp1_after = fork.flat_slp1()
        assert fork_slp1_before == fork_slp1_after, (
            "fork's tape was affected by primary mutation"
        )

    def test_mutating_fork_varnas_does_not_affect_primary(self):
        s = State(terms=[_make_lyap_term_with_m()], meta={}, trace=[])
        primary_before = s.flat_slp1()

        fork = s.fork()
        fork.terms[0].varnas.pop(1)

        assert s.flat_slp1() == primary_before, (
            "primary tape was affected by fork mutation"
        )


class TestForkMetaIsolation:
    def test_mutating_primary_meta_does_not_affect_fork(self):
        s = State(terms=[], meta={"key": "original"}, trace=[])
        fork = s.fork()

        s.meta["key"] = "changed"

        assert fork.meta.get("key") == "original", (
            "fork meta was affected by primary meta mutation"
        )

    def test_mutating_fork_meta_does_not_affect_primary(self):
        s = State(terms=[], meta={"key": "original"}, trace=[])
        fork = s.fork()

        fork.meta["key"] = "fork_changed"

        assert s.meta.get("key") == "original", (
            "primary meta was affected by fork meta mutation"
        )

    def test_fork_vibhasha_forks_reset(self):
        s = State(terms=[], meta={}, trace=[])
        s.vibhasha_forks.append({"sutra_id": "dummy", "choice_made": False, "alternative": ""})
        fork = s.fork()

        assert fork.vibhasha_forks == [], (
            "fork should start with empty vibhasha_forks"
        )

    def test_fork_carries_forked_from_marker(self):
        s = State(terms=[], meta={}, trace=[])
        fork = s.fork()

        assert fork.meta.get("forked_from") == id(s), (
            "fork should record id(parent) in meta['forked_from']"
        )


class TestExecVibhashaStoresForkState:
    def test_vibhasha_fork_stored_as_state(self):
        pr = _make_lyap_term_with_m()
        s = State(terms=[pr], meta={}, trace=[])

        # 6.4.38 is VIBHASHA with vibhasha_default=True — will apply and store fork
        s_after = apply_rule("6.4.38", s)

        assert len(s_after.vibhasha_forks) == 1, (
            "exec_vibhasha should have stored one fork"
        )
        fork = s_after.vibhasha_forks[0]
        assert isinstance(fork, State), (
            f"vibhasha_forks[0] should be a State, got {type(fork)}"
        )

    def test_fork_tape_is_pre_lopa(self):
        pr = _make_lyap_term_with_m()
        s = State(terms=[pr], meta={}, trace=[])
        s_after = apply_rule("6.4.38", s)

        fork = s_after.vibhasha_forks[0]
        # Fork is the declined branch — m should still be present
        assert "m" in [v.slp1 for t in fork.terms for v in t.varnas], (
            "declined fork should still carry the m (pre-lopa tape)"
        )

    def test_primary_tape_is_post_lopa(self):
        pr = _make_lyap_term_with_m()
        s = State(terms=[pr], meta={}, trace=[])
        s_after = apply_rule("6.4.38", s)

        # Primary derivation has m removed
        slp1_chars = [v.slp1 for t in s_after.terms for v in t.varnas]
        assert "m" not in slp1_chars, (
            "primary derivation should have m removed after 6.4.38 lopa"
        )

    def test_applied_and_skipped_meta_flags(self):
        pr = _make_lyap_term_with_m()
        s = State(terms=[pr], meta={}, trace=[])
        s_after = apply_rule("6.4.38", s)

        fork = s_after.vibhasha_forks[0]
        assert s_after.meta.get("6.4.38_applied_vibhasha") is True
        assert fork.meta.get("6.4.38_skipped_vibhasha") is True

    def test_clone_survives_state_in_vibhasha_forks(self):
        pr = _make_lyap_term_with_m()
        s = State(terms=[pr], meta={}, trace=[])
        s_after = apply_rule("6.4.38", s)

        cloned = s_after.clone()
        assert len(cloned.vibhasha_forks) == 1
        assert isinstance(cloned.vibhasha_forks[0], State), (
            "clone() must deep-copy State objects in vibhasha_forks"
        )
        # Verify isolation after clone
        cloned.vibhasha_forks[0].meta["x"] = "mutated"
        assert "x" not in s_after.vibhasha_forks[0].meta, (
            "cloned fork must be isolated from original fork"
        )
