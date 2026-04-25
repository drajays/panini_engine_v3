"""
engine/r1_check.py — Red Flag Invariants.
──────────────────────────────────────────

Per CONSTITUTION.md Article 5.  These checks run in the dispatcher
after every rule application; they catch silent-no-op bugs at the
earliest possible moment.
"""
from __future__ import annotations

from engine.sutra_type import SUTRA_TYPE_CONTRACTS, SutraRecord, SutraType
from engine.state      import State


class R1Violation(RuntimeError):
    """Raised when a non-exempt sūtra fires but form is unchanged."""


class R2Violation(RuntimeError):
    """Raised when a SAMJNA fires without writing to samjna_registry."""


class R3Violation(RuntimeError):
    """Raised when a PARIBHASHA fires without setting a gate."""


class R4Violation(RuntimeError):
    """Raised when an ADHIKARA's scope does not cover the current sūtra."""


def check_r1(
    rec          : SutraRecord,
    form_before  : str,
    form_after   : str,
) -> None:
    """
    A VIDHI / NIYAMA / NIPATANA / non-optional form-mutating sūtra
    that reported success but left the form unchanged is a BUG.
    """
    if getattr(rec, "r1_form_identity_exempt", False):
        return
    contract = SUTRA_TYPE_CONTRACTS[rec.sutra_type]
    if contract["r1_exempt"]:
        return
    if not contract["mutates_form"]:
        return
    if form_before == form_after:
        raise R1Violation(
            f"[R1] {rec.sutra_id} ({rec.sutra_type.name}) fired but form unchanged: "
            f"{form_before!r}"
        )


def check_r2(rec: SutraRecord,
             samjna_registry_before: dict,
             samjna_registry_after : dict) -> None:
    if rec.sutra_type is not SutraType.SAMJNA:
        return
    if samjna_registry_before == samjna_registry_after:
        raise R2Violation(
            f"[R2] {rec.sutra_id} (SAMJNA) fired but samjna_registry unchanged"
        )


def check_r3(rec: SutraRecord,
             paribhasha_gates_before: dict,
             paribhasha_gates_after : dict) -> None:
    if rec.sutra_type is not SutraType.PARIBHASHA:
        return
    if paribhasha_gates_before == paribhasha_gates_after:
        raise R3Violation(
            f"[R3] {rec.sutra_id} (PARIBHASHA) fired but paribhasha_gates unchanged"
        )
