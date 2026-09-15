"""
engine/phases — Universal derivation phase modules.

Note: execute_tripadi_phase lives in core/phases/tripadi.py (sutra ID literals
are forbidden in engine/ per constitutional test). Re-exported here for callers
that import from engine.phases.

Exposes:
  pada_merger.pada_merge()         — universal structural term-merge
  execute_tripadi_phase()          — full Tripāḍī spine (core/phases/tripadi.py)
"""
from engine.phases.pada_merger import pada_merge
from core.phases.tripadi import execute_tripadi_phase

__all__ = ["pada_merge", "execute_tripadi_phase"]
