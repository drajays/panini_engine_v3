"""
engine — the fixed core of Pāṇini Engine v3.

Public API (v3.1):
    from engine import (
        SutraType, SutraRecord, State, Term, Varna, apply_rule,
        SUTRA_REGISTRY, register_sutra, TraceStep,
        # v3.1 amendments:
        R1_EXEMPT, NIPATANA_FROZEN,
        set_phase, PhaseError,
        run_to_fixed_point, FixedPointError,
        RecipeConflictError,
        make_stub, coverage_report,
        SIGCollector,
    )

Everything else is internal. Sūtra files import only these symbols.
"""
from engine.sutra_type  import (
    SutraType, SutraRecord, SUTRA_TYPE_CONTRACTS,
    R1_EXEMPT, NIPATANA_FROZEN,
)
from engine.state       import State, Term, Varna
from engine.dispatcher  import apply_rule
from engine.registry    import SUTRA_REGISTRY, register_sutra
from engine.trace       import TraceStep
from engine.phase       import set_phase, PhaseError, is_tripadi_sutra
from engine.fixed_point import run_to_fixed_point, FixedPointError, MAX_ANGAKARYA_SWEEPS
from engine.errors      import RecipeConflictError
from engine.stubs       import make_stub, is_stub, coverage_report
from engine.sig         import SIGCollector

__all__ = [
    "SutraType", "SutraRecord", "SUTRA_TYPE_CONTRACTS",
    "State", "Term", "Varna",
    "apply_rule",
    "SUTRA_REGISTRY", "register_sutra",
    "TraceStep",
    # v3.1:
    "R1_EXEMPT", "NIPATANA_FROZEN",
    "set_phase", "PhaseError", "is_tripadi_sutra",
    "run_to_fixed_point", "FixedPointError", "MAX_ANGAKARYA_SWEEPS",
    "RecipeConflictError",
    "make_stub", "is_stub", "coverage_report",
    "SIGCollector",
]
