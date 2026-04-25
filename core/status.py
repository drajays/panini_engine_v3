"""
core/status.py — status constants for new code.

The engine historically stores status strings in trace steps. Introducing this
module provides a single import surface for *new* code and audits without
rewriting the entire trace system (which would be high-risk).
"""

from __future__ import annotations


class Status:
    APPLIED = "APPLIED"
    AUDIT = "AUDIT"
    SKIPPED = "SKIPPED"
    VACUOUS = "APPLIED_VACUOUS"
    BLOCKED = "BLOCKED"


__all__ = ["Status"]

