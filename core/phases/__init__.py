"""
core/phases — Phase orchestration modules that call apply_rule.

Sutra ID literals are permitted here (per CONSTITUTION Art. 7 — canonical
orchestration code lives in core/, not engine/).
"""
from core.phases.tripadi import execute_tripadi_phase

__all__ = ["execute_tripadi_phase"]
