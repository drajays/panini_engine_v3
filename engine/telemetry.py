"""
engine/telemetry.py — observer hooks and TraceBuilder for derivation analysis.

CONSTITUTION Art. 5: the dispatcher stays the single entry; hooks must not
mutate state or affect *cond* / *act*. Used for SIG benchmarks, profilers, or
IDE analytics.

Two facilities are provided:

  1. ``apply_rule`` hook — a ``ContextVar``-based callback fired at the end of
     every ``apply_rule()`` call.  Subscribe via ``set_apply_rule_hook``.

  2. ``TraceBuilder`` — a read-only observer that categorises a completed
     derivation's trace into sūtra steps vs structural steps, and provides
     query helpers for downstream tooling.
"""
from __future__ import annotations

import contextvars
from typing import Any, Callable, List, Optional

# (from_sutra_id | None, to_sutra_id, new_state_after_apply)
ApplyRuleHook = Callable[[Optional[str], str, Any], None]

_apply_rule_hook: contextvars.ContextVar[Optional[ApplyRuleHook]] = contextvars.ContextVar(
    "apply_rule_hook", default=None
)


def set_apply_rule_hook(fn: Optional[ApplyRuleHook]) -> contextvars.Token:
    """Register a callback invoked at the end of every ``apply_rule`` (all outcomes)."""
    return _apply_rule_hook.set(fn)


def reset_apply_rule_hook(token: contextvars.Token) -> None:
    _apply_rule_hook.reset(token)


def get_apply_rule_hook() -> Optional[ApplyRuleHook]:
    return _apply_rule_hook.get()


def notify_apply_rule_end(
    from_sutra_id: Optional[str],
    to_sutra_id: str,
    new_state: Any,
) -> None:
    h = _apply_rule_hook.get()
    if h is None:
        return
    try:
        h(from_sutra_id, to_sutra_id, new_state)
    except Exception:
        # Never break derivation for observer bugs
        pass


# ─────────────────────────────────────────────────────────────────────────────
# TraceBuilder — read-only categorised view of a completed derivation trace.
# ─────────────────────────────────────────────────────────────────────────────

_FIRED_STATUSES = frozenset({"APPLIED", "AUDIT", "APPLIED_VACUOUS"})


class TraceBuilder:
    """
    Categorised, read-only view of a completed derivation trace.

    Usage::

        state = derive("BU", "laT", "kartari", 3, 1)
        tb = TraceBuilder.from_state(state)

        for step in tb.sutra_steps:   # only rule applications
            print(step["sutra_id"], step["status"])

        print(tb.fired_sutra_ids())   # ordered list of IDs that actually fired

    The builder does **not** need to be attached before derivation; it reads
    ``state.trace`` after-the-fact.  For streaming / real-time analysis attach
    a hook via ``set_apply_rule_hook`` instead.
    """

    def __init__(self, trace: List[Any]) -> None:
        self._trace: List[Any] = list(trace)

    @classmethod
    def from_state(cls, state: Any) -> "TraceBuilder":
        """Build from a completed ``State`` object."""
        return cls(state.trace)

    # ── categorised views ─────────────────────────────────────────────────────

    @property
    def sutra_steps(self) -> List[Any]:
        """All trace steps that are NOT structural book-keeping."""
        return [s for s in self._trace if s.get("sutra_type") != "STRUCTURAL"]

    @property
    def structural_steps(self) -> List[Any]:
        """All structural trace steps (merges, phase transitions, etc.)."""
        return [s for s in self._trace if s.get("sutra_type") == "STRUCTURAL"]

    @property
    def full_trace(self) -> List[Any]:
        """Complete trace in derivation order."""
        return list(self._trace)

    # ── query helpers ─────────────────────────────────────────────────────────

    def steps_for(self, sutra_id: str) -> List[Any]:
        """All trace steps for a given sūtra ID."""
        return [s for s in self._trace if s.get("sutra_id") == sutra_id]

    def fired_sutra_ids(self) -> List[str]:
        """Ordered list of sūtra IDs whose applications were recorded as fired."""
        return [
            s["sutra_id"]
            for s in self._trace
            if s.get("status") in _FIRED_STATUSES
            and s.get("sutra_type") != "STRUCTURAL"
        ]

    def applied_steps(self) -> List[Any]:
        """Sūtra steps with status APPLIED (non-vacuous mutations)."""
        return [
            s for s in self._trace
            if s.get("status") == "APPLIED"
            and s.get("sutra_type") != "STRUCTURAL"
        ]

    def structural_labels(self) -> List[str]:
        """Labels (sutra_id field) of all structural steps, in order."""
        return [s["sutra_id"] for s in self.structural_steps]

    def __len__(self) -> int:
        return len(self._trace)

    def __repr__(self) -> str:
        return (
            f"TraceBuilder("
            f"{len(self.sutra_steps)} sutra steps, "
            f"{len(self.structural_steps)} structural steps)"
        )
