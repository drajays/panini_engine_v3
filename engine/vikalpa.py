"""
engine/vikalpa.py — विभाषा: every branch is an output.

A वा / विभाषा sūtra is not a coin toss the engine resolves privately. It is one
rule with two legitimate readings, and a derivation that shows only one of them
has hidden half the grammar. ``रामः शेते`` is both *rāmaḥ śete* and
*rāmaś śete*; a learner needs to see both, and the sūtra that licenses each.

Two pieces:

``choose({sutra_id: bool})``
    A context manager that fixes the choice for named optional rules. The
    dispatcher consults it after the recipe step and before the sūtra's own
    ``vibhasha_default``, so any pipeline can be re-run down the other branch
    without changing its code.

``explore(run)``
    Runs a derivation, sees which optional rules it actually reached, then
    re-runs it down every combination and returns the distinct results. The
    branch count is bounded: an engine that silently explores 2^20 paths has
    stopped being auditable.
"""
from __future__ import annotations

import itertools
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Callable, Iterator

_POLICY: dict[str, bool] = {}

MAX_OPTIONAL_RULES = 6           # 2**6 = 64 branches, an auditable ceiling


def policy_choice(sutra_id: str, default: bool) -> bool:
    """The dispatcher's hook: an explicit choice, else the sūtra's default."""
    return _POLICY.get(sutra_id, default)


@contextmanager
def choose(choices: dict[str, bool]) -> Iterator[None]:
    """Fix the reading of named विभाषा rules for the duration of the block."""
    previous = dict(_POLICY)
    _POLICY.update(choices)
    try:
        yield
    finally:
        _POLICY.clear()
        _POLICY.update(previous)


def optional_rules_reached(state: Any) -> list[str]:
    """The विभाषा sūtras this derivation actually put a question to."""
    seen: list[str] = []
    for step in getattr(state, "trace", ()):
        if step.get("sutra_type") != "VIBHASHA":
            continue
        sid = step.get("sutra_id")
        if sid and sid not in seen:
            seen.append(sid)
    return seen


@dataclass(frozen=True)
class Branch:
    """One complete derivation, and the readings that produced it."""

    choices: tuple[tuple[str, bool], ...]
    surface_slp1: str
    surface_dev: str
    state: Any

    def describe(self) -> str:
        if not self.choices:
            return f"{self.surface_dev} ({self.surface_slp1})"
        taken = ", ".join(
            f"{sid} {'प्रवृत्तम्' if yes else 'न प्रवृत्तम्'}" for sid, yes in self.choices
        )
        return f"{self.surface_dev} ({self.surface_slp1})  ←  {taken}"


def explore(run: Callable[[], Any], *, limit: int = MAX_OPTIONAL_RULES) -> list[Branch]:
    """Every distinct surface this derivation can legitimately produce.

    ``run`` must be a zero-argument callable that performs the derivation, so
    it can be replayed once per combination.
    """
    first = run()
    optional = optional_rules_reached(first)[:limit]
    if not optional:
        return [Branch((), first.flat_slp1(), first.flat_dev(), first)]

    seen: dict[str, Branch] = {}
    for combination in itertools.product([True, False], repeat=len(optional)):
        choices = dict(zip(optional, combination))
        with choose(choices):
            try:
                state = run()
            except Exception:
                continue                  # a branch the engine cannot walk yet
        surface = state.flat_slp1()
        if surface not in seen:
            seen[surface] = Branch(tuple(choices.items()), surface,
                                   state.flat_dev(), state)
    return list(seen.values())
