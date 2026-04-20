"""
engine/errors.py — shared exception types.
────────────────────────────────────────────

CONSTITUTION v3.1 amendment.  Exceptions live here so every subsystem
can raise them without creating circular imports.

  R1Violation / R2Violation / R3Violation  → engine/r1_check.py
  PhaseError                                → engine/phase.py
  FixedPointError                           → engine/fixed_point.py
  RecipeConflictError                       → here (no natural home)
"""
from __future__ import annotations


class RecipeConflictError(RuntimeError):
    """
    Raised when two recipe steps claim mutation rights over the same
    varṇa position at the same state, or when two sūtras fire
    simultaneously with conflicting outputs that the resolver cannot
    disambiguate.

    Per CONSTITUTION Article 1 (mechanical blindness) the engine
    NEVER silently picks a winner in a genuine conflict — it raises
    this and asks the recipe author / resolver table to decide
    explicitly.

    Attributes:
      sutra_ids    : tuple of conflicting sūtra ids
      position     : (term_idx, varna_idx) of the contested position
      detail       : human-readable explanation
    """

    def __init__(self, sutra_ids, position=None, detail: str = ""):
        self.sutra_ids = tuple(sutra_ids)
        self.position  = position
        self.detail    = detail
        msg = (
            f"recipe conflict: sūtras {self.sutra_ids!r} both want to "
            f"mutate position {self.position!r}"
        )
        if detail:
            msg += f" — {detail}"
        super().__init__(msg)
