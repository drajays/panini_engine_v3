"""
engine/telemetry.py — optional global hooks for ``apply_rule`` (observer-only).

CONSTITUTION Art. 5: the dispatcher stays the single entry; hooks must not
mutate state or affect *cond* / *act*. Used for SIG benchmarks, profilers, or
IDE analytics.
"""
from __future__ import annotations

import contextvars
from typing import Any, Callable, Optional

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
