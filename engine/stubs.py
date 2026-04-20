"""
engine/stubs.py — Universal stub scaffolding + coverage tracking.
──────────────────────────────────────────────────────────────────

CONSTITUTION v3.1 amendment (promoted from DEFERRED D4).

Why this exists: as the sūtra catalog grows past 100, operators need
to distinguish "not implemented yet" from "implemented but not firing"
from "missing entirely".  A stub SutraRecord fills the first slot:
it exists in SUTRA_REGISTRY, declares its type, but does nothing
beyond logging a STUB step in the trace.

A stub is marked by `rec.meta_is_stub == True`.  The dispatcher
detects this and emits a status="APPLIED" trace row with
type_label="STUB" so paradigm audits can see where gaps are.

coverage_report(registry) returns a dict giving implementation
percentage per SutraType and overall.
"""
from __future__ import annotations

from collections import defaultdict
from typing      import Any, Dict

from engine.state      import State
from engine.sutra_type import SutraRecord, SutraType


def _stub_cond(state: State) -> bool:
    return False  # never fire; placeholder in registry


def _stub_act(state: State) -> State:
    return state  # no-op


def make_stub(
    sutra_id       : str,
    sutra_type     : SutraType,
    text_dev       : str = "[STUB]",
    text_slp1      : str = "STUB",
    padaccheda_dev : str = "[STUB]",
    why_dev        : str = "[STUB — not yet implemented]",
) -> SutraRecord:
    """
    Build a stub SutraRecord that will register cleanly, pass schema
    validation, and do nothing at runtime.  Useful for padding out
    SUTRA_REGISTRY ahead of real implementations.
    """
    # Choose sensible per-type defaults so __post_init__ doesn't raise.
    kwargs: Dict[str, Any] = dict(
        sutra_id       = sutra_id,
        sutra_type     = sutra_type,
        text_slp1      = text_slp1,
        text_dev       = text_dev,
        padaccheda_dev = padaccheda_dev,
        why_dev        = why_dev,
    )

    if sutra_type is SutraType.ADHIKARA:
        # Zero-width adhikāra scope at the stub itself.
        kwargs["adhikara_scope"] = (sutra_id, sutra_id)
    elif sutra_type is SutraType.ATIDESHA:
        kwargs.update(
            atidesha_source = f"stub_src_{sutra_id}",
            atidesha_dest   = f"stub_dst_{sutra_id}",
            atidesha_target = "stub",
        )
    elif sutra_type is SutraType.PRATISHEDHA:
        kwargs["blocks_sutra_ids"] = ("0.0.0",)  # blocks a non-existent rule
    elif sutra_type is SutraType.NIPATANA:
        kwargs["nipatana_form_slp1"] = "stub"

    if sutra_type is not SutraType.ANUVADA:
        kwargs["cond"] = _stub_cond
        kwargs["act"]  = _stub_act

    rec = SutraRecord(**kwargs)
    # Mark as a stub via an attribute we set AFTER dataclass construction.
    # (SutraRecord is a dataclass; setting an attribute is fine even if
    # the dataclass is not frozen.)
    object.__setattr__(rec, "meta_is_stub", True)
    return rec


def is_stub(rec: SutraRecord) -> bool:
    return bool(getattr(rec, "meta_is_stub", False))


def coverage_report(registry: Dict[str, SutraRecord]) -> Dict[str, Any]:
    """
    Return coverage statistics for a SUTRA_REGISTRY-shaped dict.

    Shape:
      {
        "total"          : int,
        "implemented"    : int,
        "stubs"          : int,
        "coverage_pct"   : float,
        "by_type"        : { "VIDHI": {"implemented": n, "stubs": k, ...}, ... },
      }
    """
    total       = len(registry)
    stubs       = sum(1 for r in registry.values() if is_stub(r))
    implemented = total - stubs

    by_type: Dict[str, Dict[str, int]] = defaultdict(
        lambda: {"total": 0, "implemented": 0, "stubs": 0}
    )
    for r in registry.values():
        bt = by_type[r.sutra_type.name]
        bt["total"] += 1
        if is_stub(r):
            bt["stubs"] += 1
        else:
            bt["implemented"] += 1

    for bt in by_type.values():
        bt["coverage_pct"] = (
            round(100.0 * bt["implemented"] / bt["total"], 2)
            if bt["total"] else 0.0
        )

    return {
        "total"        : total,
        "implemented"  : implemented,
        "stubs"        : stubs,
        "coverage_pct" : round(100.0 * implemented / total, 2) if total else 0.0,
        "by_type"      : dict(by_type),
    }
