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

_POLICY: dict[str, "bool | int"] = {}

MAX_OPTIONAL_RULES = 6           # 2**6 = 64 branches, an auditable ceiling


def policy_choice(sutra_id: str, default: bool) -> bool:
    """The dispatcher's hook: an explicit choice, else the sūtra's default."""
    return bool(_POLICY.get(sutra_id, default))


def policy_pick(state: Any, sutra_id: str, options: int, default: int = 0) -> int:
    """A sūtra that lists several affixes or forms side by side (तव्यत्तव्यानीयरः, ण्वुल्तृचौ, तुमुन्ण्वुलौ) leaves the choice among them to the
    reading: ``choose({sid: i})`` takes the i-th (0-based); the default is the first. The sūtra tells the state how many it offered so that
    :func:`explore` can walk every one."""
    state.meta.setdefault("vikalpa_multi", {})[sutra_id] = options
    pick = _POLICY.get(sutra_id, default)
    return int(pick) % options if not isinstance(pick, bool) else default


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


def multiway_reached(state: Any) -> list[tuple[str, int]]:
    """The side-by-side lists (policy_pick) this derivation put a question to: [(sūtra id, how many)]."""
    return sorted((getattr(state, "meta", {}) or {}).get("vikalpa_multi", {}).items())


def optional_rules_reached(state: Any) -> list[str]:
    """The विभाषा sūtras this derivation actually put a question to.

    A विभाषा whose own condition was false is not an option the derivation
    faced — it is simply inapplicable, like any other rule that declines. Only
    a rule that fired, or that was held back by the choice, counts: otherwise
    every subanta would report 1.4.5 वाऽऽमि as a branch point merely because
    the scheduler walked past it.
    """
    seen: list[str] = []
    for step in getattr(state, "trace", ()):
        if step.get("sutra_type") != "VIBHASHA":
            continue
        if step.get("skip_reason") == "COND-FALSE":
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
    seen: dict[str, Branch] = {}
    todo: list[dict] = [{}]
    while todo:                           # a choice can open a rule the first walk never reached (3.1.124 declined → 3.1.96): expand on demand
        choices = todo.pop()
        with choose(choices):
            try:
                state = run()
            except Exception:
                continue                  # a branch the engine cannot walk yet
        axes = {sid: [True, False] for sid in optional_rules_reached(state)[:limit]}
        axes.update({sid: list(range(n)) for sid, n in multiway_reached(state)})
        new = [sid for sid in axes if sid not in choices]
        if new:
            sid = new[0]
            todo.extend({**choices, sid: v} for v in axes[sid])
            continue
        surface = state.flat_slp1()
        if surface not in seen:
            seen[surface] = Branch(tuple(choices.items()), surface, state.flat_dev(), state)
    return list(seen.values())
